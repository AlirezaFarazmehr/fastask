
# 📝 ToDo App with FastAPI

A lightweight and simple ToDo management application built using **FastAPI**, **SQLite**, and a basic HTML frontend.

---

## 🧰 Technologies Used:
- Python 3.10
- FastAPI 🚀
- SQLite 🗃️
- HTML (static UI)
- Uvicorn (for running the server)
- SQLAlchemy (ORM)

---

## ⚙️ How to Run the Project:

1. Clone or download the repository:
```bash
git clone https://github.com/Alirezafarazmehr/fastask.git
cd fastask
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
uvicorn main:app --reload
```

5. Open your browser and go to:
```
http://127.0.0.1:8000/
```

---

## 📂 Project Structure:

```
├── crud.py              # CRUD operations
├── database.py          # Database setup
├── main.py              # FastAPI entry point
├── models.py            # Data models
├── static/index.html    # Simple HTML frontend
├── requirements.txt     # List of Python packages
├── tasks.db             # SQLite database
└── .gitignore
```

---

## ✅ Features:

- Add new tasks
- View task list
- Delete tasks
- Basic frontend for testing

---

## ✨ Author

Developed by [Alireza Farazmehr] 💻
