# 🎉 Event Management APIs

A functional Django REST APIs for managing events and attendee registrations — built with clean architecture and best practices.

---

## 🚀 Features

- ✅ Create & list upcoming events
- ✅ Register attendees to events
- ✅ Prevent duplicate registrations
- ✅ Avoid overbooking based on max capacity
- ✅ View attendees per event
- ✅ Pagination support
- ✅ Django admin for event management
- ✅ Fully documented Swagger UI & ReDoc
- ✅ Comprehensive unit test coverage using `pytest`

---

## 🛠️ Tech Stack

- Python 3.11
- Django 5.2
- Django REST Framework
- drf-spectacular (OpenAPI docs)
- SQLite (default) or PostgreSQL-ready
- Pytest & pytest-cov (for tests & coverage)

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/GargAnshu9468/event_management.git
cd event_management
```

### 2️⃣ Create & Activate Virtual Environment

- On Windows

```bash
python -m venv ems_env
ems_env\Scripts\activate
```

- On macOS/Linux

```bash
python3 -m venv ems_env
source ems_env/bin/activate
```

### 3️⃣ Install Requirements

- On Windows

```bash
pip install -r requirements.txt
```

- On macOS/Linux

```bash
pip3 install -r requirements.txt
```

### 4️⃣ Make & Apply Migrations

- On Windows

```bash
python manage.py makemigrations
python manage.py migrate
```

- On macOS/Linux

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 5️⃣ Run Development Server

- On Windows

```bash
python manage.py runserver
```

- On macOS/Linux

```bash
python3 manage.py runserver
```

---

## 📚 API Documentation

- Swagger UI: [`/swagger/`](http://127.0.0.1:8000/swagger/)
- Schema: [`/schema/`](http://127.0.0.1:8000/schema/)
- ReDoc: [`/redoc/`](http://127.0.0.1:8000/redoc/)

---

## 🧪 Running Tests & Coverage

```bash
pytest
```

- HTML report: `htmlcov/index.html`

---

## 🔐 Django Admin

- URL: [`/admin/`](http://127.0.0.1:8000/admin/)

To create a superuser:

- On Windows

```bash
python manage.py createsuperuser
```

- On macOS/Linux

```bash
python3 manage.py createsuperuser
```

---

## 📂 Project Structure

```
event_management/
├── events/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── event_management/
│   ├── settings.py
│   ├── urls.py
├── tests/
│   └── test_event.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
```
---

## 💡 Assumptions

- Attendee uniqueness is based on email per event.
- Start and end times are timezone-aware (default IST).
- Default pagination: 10 items per page.
- SQLite used by default, PostgreSQL ready.

---

## 🧠 Author

**Anshu Garg**
Senior Python Developer
📧 a.kgarg9050@gmail.com

---
