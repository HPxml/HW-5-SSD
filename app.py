from flask import Flask, request, make_response, redirect, render_template, g, abort
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm, TransferForm

# Import business logic for accounts and users
from bin.account_service import get_balance, do_transfer
from user_service import get_user_with_credentials, logged_in

app = Flask(__name__)

# Set a secret key for session management and CSRF protection
# ⚠️ In production, use secrets.token_hex(32)
app.config['SECRET_KEY'] = 'yoursupersecrettokenhere'
app.config['WTF_CSRF_ENABLED'] = True

# Enable CSRF protection
csrf = CSRFProtect(app)

@app.route("/", methods=['GET'])
def home():
    # Redirect to login if the user is not authenticated
    if not logged_in():
        form = LoginForm()
        return render_template("login.html", form=form)
    return redirect('/dashboard')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "GET":
        return render_template("login.html", form=form)

    if not form.validate_on_submit():
        return render_template("login.html", form=form, error="Invalid submission")

    email = form.email.data
    password = form.password.data

    user = get_user_with_credentials(email, password)
    if not user:
        return render_template("login.html", form=form, error="Invalid credentials")

    response = make_response(redirect("/dashboard"))
    response.set_cookie("auth_token", user["token"])
    return response, 303

@app.route("/dashboard", methods=['GET'])
def dashboard():
    # Restrict dashboard to authenticated users only
    if not logged_in():
        form = LoginForm()
        return render_template("login.html", form=form)
    return render_template("dashboard.html", email=g.user)

@app.route("/details", methods=['GET'])
def details():
    # Ensure user is logged in before accessing sensitive account info
    if not logged_in():
        form = LoginForm()
        return render_template("login.html", form=form)

    account_number = request.args['account']

    return render_template(
        "details.html",
        user=g.user,
        account_number=account_number,
        balance=get_balance(account_number, g.user)
    )

@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    form = TransferForm()

    if request.method == "GET":
        return render_template("transfer.html", form=form)

    if not logged_in():
        form = LoginForm()
        return render_template("login.html", form=form)

    if not form.validate_on_submit():
        return render_template("transfer.html", form=form, error="Invalid input or CSRF token missing")

    source = form.from_account.data
    target = form.to_account.data
    amount = form.amount.data

    available_balance = get_balance(source, g.user)
    if available_balance is None:
        abort(404, "Account not found")
    if amount > available_balance:
        abort(400, "You don't have that much")

    if not do_transfer(source, target, amount):
        abort(400, "Something bad happened")

    return redirect("/dashboard"), 303

@app.route("/logout", methods=['GET'])
def logout():
    response = make_response(redirect("/dashboard"))
    response.delete_cookie('auth_token')
    return response, 303
