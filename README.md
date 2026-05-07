# 🔵 NYCRP FBI — Personnel Database

> A classified personnel management system for the NYCRP FBI department in ERLC Roleplay, built with Django.(Note: This Website is not affialated with the Federal Bureau of Investigation or any Federal Agency in the World. This is just a Database for a Emergency Response:Liberty County Roblox Roleplay Server.)

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat-square)
![Django](https://img.shields.io/badge/Django-5.x-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## 📋 About

The NYCRP FBI Personnel Database is an internal management system for the FBI department in the ERLC Roblox roleplay server. It allows directors and admins to manage agents, track divisions, assign ranks, and maintain personnel files for every member of the department.

---

## ✨ Features

- 🔐 **Secure Login System** — Each agent has their own login account
- 👤 **Personnel Files** — Detailed profiles for every agent including rank, division, callsign and more
- 🗂️ **Employee Directory** — Full list of all agents with search and filter
- 🏅 **Rank Hierarchy** — Full rank system from Trainee to Director
- 🚨 **HRT Division Tracking** — Hostage Rescue Team members are flagged on their profile
- 🛡️ **Admin Panel** — Directors can add, edit and remove agents
- 🎨 **FBI-Style UI** — Dark classified database aesthetic throughout

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

## 👮 How To Add An Agent

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
   - HRT status
   - Personnel file notes

---

## 🏅 Ranks

| Rank | Level |
|------|-------|
| Director | 6 |
| Deputy Director | 5 |
| Supervisor | 4 |
| Senior Agent | 3 |
| Agent | 2 |
| Trainee | 1 |

---

## 🗂️ Divisions

- **Command** — Senior leadership
- **HRT** — Hostage Rescue Team
- **Tactical** — Field operations
- **Cyber** — Digital investigations
- **General** — General agents

---

## 🔒 Access Levels

| Role | Access |
|------|--------|
| Director / Admin | Full access — add, edit, remove agents via `/admin/` |
| Agent | View employee directory and personnel files |
| Unauthenticated | Login page only |

---

## 🛠️ Built With

- [Python](https://python.org)
- [Django](https://djangoproject.com)
- [SQLite](https://sqlite.org) — default database
- HTML / CSS — custom FBI-style UI

---

## 📜 License

This project is for internal NYCRP FBI department use only. Not for public distribution.

---

## 👥 Credits

Built and maintained by the NYCRP FBI Command Staff.

> *Fidelity — Bravery — Integrity*
