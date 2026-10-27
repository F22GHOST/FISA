# 🔵 NYCRP NYPD — Personnel Database

> A classified personnel management system for the NYCRP NYPD department in ERLC Roleplay, built with Django.(Note: This Website is not affialated with the New york Police Department or any Law Enforcement Agency in the World. This is just a Database for a Emergency Response:Liberty County Roblox Roleplay Server.)

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat-square)
![Django](https://img.shields.io/badge/Django-5.x-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## 📋 About

The NYCRP NYPD Personnel Database is an internal management system for the NYPD department in the ERLC Roblox roleplay server. It allows directors and admins to manage agents, track divisions, assign ranks, and maintain personnel files for every member of the department.

---

## ✨ Features

- 🔐 **Secure Login System** — Each agent has their own login account
- 👤 **Personnel Files** — Detailed profiles for every officer including rank, division, callsign and more
- 🗂️ **Employee Directory** — Full list of all officer with search and filter
- 🏅 **Rank Hierarchy** — Full rank system from Trainee to Commisioner
- 🚨 **ESU Division Tracking** — Emergency Service Unit members are flagged on their profile
- 🛡️ **Admin Panel** — Directors can add, edit and remove agents
- 🎨 **Classified-Style UI** — Dark classified database aesthetic throughout

---

## 🖥️ Screenshots

> Login Page — `http://127.0.0.1:8000/login/`

> Employee Directory — `http://127.0.0.1:8000/employees/`

> Personnel File — `http://127.0.0.1:8000/employees/<id>/`

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/nycrp-fbi.git
cd nycrp-fbi
```

2. **Create a virtual environment**
```bash
python -m venv venv
```

3. **Activate the virtual environment**

Windows:
```bash
venv\Scripts\activate
```
Mac/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install django
```

5. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create a superuser (Director account)**
```bash
python manage.py createsuperuser
```

7. **Run the server**
```bash
python manage.py runserver
```

8. **Open the app**
```
http://127.0.0.1:8000/
```

---

## 📁 Project Structure

```
FISA/
├── FISA/                   # Main project folder
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL routes
│   └── wsgi.py
├── employees/              # Employees app
│   ├── templates/
│   │   └── employees/
│   │       ├── base.html           # Main layout
│   │       ├── login.html          # Login page
│   │       ├── employee_list.html  # Agent directory
│   │       └── employee_detail.html # Personnel file
│   ├── models.py           # Database models
│   ├── views.py            # Page logic
│   ├── urls.py             # App URL routes
│   └── admin.py            # Admin panel config
└── manage.py
```

---

## 👮 How To Add An Officer

1. Go to `http://127.0.0.1:8000/admin/`
2. Log in with your director account
3. Click **Users** → **Add User** and create their login credentials
4. Click **Employees** → **Add Employee** and fill in their:
   - Roleplay name
   - Roblox username
   - Discord username
   - Callsign / Badge number
   - Rank
   - Division(s)
   - ESU status
   - Personnel file notes

---

## 🔒 Access Levels

| Role | Access |
|------|--------|
| Command Team / Admin | Full superuser access — add, edit, remove agents via `/admin/` |
| Employee | View employee directory and personnel files |
| Unauthenticated | Login page only |

---

## 🛠️ Built With

- [Python](https://python.org)
- [Django](https://djangoproject.com)
- [SQLite](https://sqlite.org) — default database
- HTML / CSS — custom Classified-style UI

---

## 📜 License

This project is for internal NYCRP NYPD department use only. Not for public distribution.

---

## 👥 Credits

Built and maintained by the NYCRP NYPD Officer F22GHOST.

> *"Fidelis Ad Mortem"*
