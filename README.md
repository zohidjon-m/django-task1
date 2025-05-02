
# 🏗️ Django Tenant Config API

This is a simple Django REST API that allows you to retrieve configuration details for tenants by ID.

---

## 🚀 Features

- Django + Django REST Framework
- SQLite (default for development)
- API endpoint: `GET /api/tenants/<id>/`
- Unit tests for success and error cases

---

## 🛠️ Setup Instructions

### 1. Clone the project

```bash
git clone <your-repo-url>
cd tenantproject
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist yet, you can create one:
```bash
pip freeze > requirements.txt
```

Or manually install:
```bash
pip install django djangorestframework
```

---

## ⚙️ Run the Server

```bash
python manage.py migrate
python manage.py runserver
```

Server will start at:  
👉 http://127.0.0.1:8000

---

## 📡 API Usage

### ✅ Get tenant by ID

```
GET /api/tenants/<id>/
```

#### Sample Response:

```json
{
  "id": 1,
  "name": "Tenant A",
  "domain": "tenant-a.com",
  "config_json": {
    "enable_feature_x": true,
    "theme": "dark"
  }
}
```

---

## 🧪 Running Tests

```bash
python manage.py test tenants
```

This will run all unit tests defined in `tenants/tests.py`.

---

## 👤 Admin Panel (Optional)

To use Django Admin to manage tenants:

1. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

2. Log in at:
   👉 http://127.0.0.1:8000/admin

---

## 📂 Project Structure

```
tenantproject/
├── tenantproject/       # Django project settings
├── tenants/             # Main app with models, views, tests
├── db.sqlite3           # Dev database
├── manage.py
```

---

## 📌 Tech Stack

- Python 3.11+
- Django 5.x
- Django REST Framework
- SQLite (dev only — PostgreSQL required for Task 2)

---

