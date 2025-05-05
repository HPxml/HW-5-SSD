# 💎 Secure Gem Vault

A secure Flask-based web application where users log in and manage "gems" instead of money — including viewing balances and transferring assets. Designed for both learning and secure software practices.

---

##  Features

-  Secure login with CSRF protection
-  Password hashing with salted hashes
-  “Gems” system instead of traditional balance
-  Transfer functionality with validation
-  Protection against XSS/CSRF
-  Clean, consistent UI with minimal CSS
-  Success messages with auto-redirects

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
## 🗂️ Project Structure

```
.
├── app.py                  # Main Flask app
├── forms.py                # WTForms for login and transfer
├── user_service.py         # Handles user logic
├── bank.db                 # SQLite DB
├── bin/
│   ├── account_service.py  # Business logic for transfers
│   ├── createdb.py         # DB setup script
│   ├── makeaccounts.py     # Optional: demo account creator
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── transfer.html
│   ├── details.html
└── static/
    └── style.css           # Shared CSS (optional)
```

---

## 🚀 Getting Started

1. **Install dependencies**
   ```bash
   pip install flask flask-wtf
   ```

2. **Set up the database**
   ```bash
   python bin/createdb.py
   python bin/makeaccounts.py  # optional: demo accounts
   ```

3. **Run the app**
   ```bash
   python app.py
   ```

4. **Open in browser**
   Visit `http://localhost:5000`

---

## 🛠 Configuration

Make sure your `SECRET_KEY` is secure in production:

```python
app.config['SECRET_KEY'] = 'yoursupersecrettokenhere'  # replace with secrets.token_hex(32)
```

---

## 📸 Screenshots

![alt text](<GEMVAULT (1).png>)
![alt text](<GEMVAULT (2).png>)
![alt text](<GEMVAULT (3).png>)
![alt text](<GEMVAULT (4).png>)
![alt text](<GEMVAULT (5).png>)
![alt text](<GEMVAULT (6).png>)
![alt text](<GEMVAULT (7).png>)
![alt text](<GEMVAULT (8).png>)
![alt text](<GEMVAULT (10).png>)
![alt text](<GEMVAULT (9).png>)

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
## 📚 Learning Goals

This app demonstrates:
- Secure form handling in Flask
- CSRF protection via Flask-WTF
- Frontend feedback for better UX
- Flask routing and templating
- Clean and simple design with custom CSS
## 🧾 License

MIT License. This project is for educational purposes only.

---
