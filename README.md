
# 🔐 Secure Flask Web Application

This project is a secure web application built with the Flask framework as part of a web security course. It demonstrates secure user authentication, CSRF and XSS protection, user enumeration defense, and secure transfer functionality — all while using JWT-based sessions and minimal UI styling.

---

## ✨ Features

- 🔐 **User Authentication** with PBKDF2 password hashing (via Passlib)
- 🍪 **JWT Session Management** using cookies
- 🔒 **CSRF Protection** using Flask-WTF
- 🚫 **XSS Protection** via auto-escaped Jinja2 templates
- 🛡️ **SQL Injection Defense** using parameterized queries
- 👤 **User Enumeration Defense** on login
- 💸 **Asset Transfer Functionality** (with validation)
- 🎨 **Minimal Styling** for user interface
- 🎉 **Fun Animations / Effects** (optional)

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Flask**
- **Flask-WTF**
- **WTForms**
- **Passlib**
- **SQLite** (for simplicity)
- **JWT (via PyJWT)**

---

## 🏗️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/secure-flask-app.git
   cd secure-flask-app
   ```

2. **Create virtual environment**

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   export FLASK_ENV=development
   flask run
   ```

5. Visit `http://localhost:5000` in your browser.

---

## 🧪 Security Defenses Explained

| Vulnerability      | Defense Mechanism                                  |
|--------------------|-----------------------------------------------------|
| Password cracking  | PBKDF2 hashing with salt (via `passlib.hash`)       |
| Session hijacking  | JWT tokens stored in cookies with expiration        |
| CSRF attacks       | Flask-WTF CSRF token auto-included in forms         |
| XSS attacks        | Jinja2 templates escape all variables by default    |
| SQL Injection      | All queries use `?` placeholders, no string concat  |
| User Enumeration   | Login always returns "Invalid credentials"          |
| Broken Validation  | All inputs validated via WTForms + custom checks    |

---

## 📂 File Structure

```
secure-flask-app/
│
├── app.py                 # Main Flask app with route logic
├── user_service.py        # Auth + session handling
├── forms.py               # Flask-WTF form definitions
├── templates/             # HTML templates (login, dashboard, etc.)
├── bank.db                # SQLite DB for users/accounts
└── static/                # Optional CSS or JS if needed
```

---

## 📸 Screenshots (Optional)

> Add screenshots or GIFs here to show transfer animations or UI if you have any.

---

## 🧾 License

MIT License. This project is for educational purposes only.

---

## 🙏 Acknowledgements

Thanks to Professor [Your Instructor’s Name] and the LMU CMSI-662 Web Security course for the guidance and base structure.
