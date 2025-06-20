# Blog Project

This is a **simple Blog API** implemented in **FastAPI with JWT authentication and CRUD operations for blogs and users**.  
The application uses **Postgres** as a database and **bcrypt** for password hashing.

---

## 🔹Features

- User registration and authentication
- JWT authentication with password hashing
- CRUD operations for blogs
- Blog ownership validation
- Database ORM with **SQLAlchemy**
- Schema validation with **Pydantic**
- Exception handling with proper **HTTP codes**

---

## 🔹Tech Stack

- **Python 3.9+**
- **FastAPI**
- **Postgres**
- **SQLAlchemy**
- **Alembic** (optional for migrations)
- **bcrypt** for password hashing
- **PyJWT (jose)** for JWT tokens
- **Passlib** for password context

---

## 🔹Project Structure

```
Project Root/
├── alembic/
│ ├─ env.py
├── blog/
│ ├─ repository/
│   └── blog.py
│   └── user.py
│ ├─ routers/
│   └── __init__.py
│   └── authentication.py
│   └── blog.py
│   └── user.py
│ ├─ __init__.py
│ ├─ database.py
│ ├─ hashing.py
│ ├─ main.py
│ ├─ models.py
│ ├─ oauth2.py
│ ├─ schemas.py
│ ├─ token.py
├── alembic.ini
├── requirements.txt
├── main.py
├── README.md
```

---

## 🔹Installation

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/AntoEvaniyose/Blog-Project.git
cd Book Fast API
```

2️⃣ **Create and activate a virtual environment (optional but recommended):**

```bash
python3 -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3️⃣ **Install the required packages:**

```bash
pip install -r requirements.txt
```

---

## 🔹Environment

- Update PostgreSQL credentials:

  🔸 In **`blog/database.py`**
  ```python
  SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost:port/database_name"
  ```

  🔸 In **`alembic.ini`**, set the `sqlalchemy.url`:
  ```ini
  sqlalchemy.url = postgresql://username:password@localhost:port/database_name
  ```


- Update `SECRET_KEY` and `ALGORITHM` in **`blog/token.py`**
```python
SECRET_KEY = "<your_secret_key>"
ALGORITHM = "HS256"
```

---

## 🔹Running the Application

```bash
uvicorn blog.main:app --reload
```
---

## 📘 API Endpoints

### 🔹 User Routes

| Method  | Endpoint        | Description                |
|---------|------------------|----------------------------|
| `POST`  | `/user/`         | Register a new user        |
| `GET`   | `/user/{id}`     | Get a specific user by ID  |

### 🔹 Blog Routes

| Method  | Endpoint         | Description                            |
|---------|------------------|----------------------------------------|
| `GET`   | `/blog/`         | Get all blogs                          |
| `POST`  | `/blog/`         | Create a new blog                      |
| `GET`   | `/blog/{id}`     | Get a specific blog by ID              |
| `PUT`   | `/blog/{id}`     | Update a blog (only if owner)          |
| `DELETE`| `/blog/{id}`     | Delete a blog (only if owner)          |

### 🔹 Auth Route

| Method  | Endpoint   | Description                  |
|---------|------------|------------------------------|
| `POST`  | `/login`   | Login and get access token   |


---
