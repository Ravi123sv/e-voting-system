
# E-Voting System

A complete web-based E-Voting System built using Python, HTML, and modular folder structure. The platform supports voter authentication using Aadhaar, OTP verification, candidate listing, vote booking, and an admin dashboard for control and results tracking.

---

## 🗂️ Project Structure

```

e-voting-system/
├── index.html              # Main landing page
├── scriptname.py           # Main Python backend
├── otp/                    # OTP verification module
├── aadhaar/                # Aadhaar-based voter ID checks
├── booking/                # Voting booking logic
├── confirmation/           # Vote confirmation screen
├── candidates/             # Candidate listing & vote capture
├── admin/                  # Admin dashboard and controls
├── www/                    # Static files (JS, CSS, media)
├── .venv/                  # Virtual environment (not pushed)
├── .vscode/                # Editor configs
├── .pytest\_cache/          # Pytest cache (can ignore)
└── README.md

````

---

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask or Django)
- **Security:** OTP, Aadhaar check (simulated or actual API)
- **Tools:** Pytest, virtualenv

---

## 🔐 Features

- 🔐 Aadhaar-based voter authentication
- 📩 OTP verification module
- 🗳️ Candidate voting and booking system
- ✅ Confirmation & success screens
- 👤 Admin panel for vote management
- 📦 Modular structure for scalability

---

## 🚀 How to Run

1. Clone the repository  
2. Set up virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
````

3. Run the server:

```bash
python scriptname.py
```

4. Open `http://localhost:5000` in your browser

---

## 📘 Notes

* This project is for educational purposes only
* Simulated Aadhaar and OTP logic unless integrated with real services
* Modular folders help isolate responsibilities cleanly

---

## 👤 Author

**Ravi Sai Vinay M**
GitHub: [@Ravi123sv](https://github.com/Ravi123sv)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
Use for learning, research, or academic demos only.

```
