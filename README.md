# Title: Task Manager API

A simple **Task Manager API** built with **Django** and **Django Ninja**.
All API endpoints are prefixed with `api/v1/`. Allows users to manage tasks with full **CRUD operations**, **filtering**, **mark as completed**, and **JWT authentication & authorization**. Test cases are also included to ensure API reliability.

---

## Features

* **User Authentication**

  * Signup
  * Login
  * Logout
* **Task Management**

  * Create, Read, Update, Delete tasks
  * Mark tasks as completed
  * Filter tasks by title, description, and completion status
  * Pagination support
* **Testing**

  * Test cases included in `test.py`

---

## Requirements

* Python 3.10+
* pip
* Virtual environment

---

## Step-by-Step Setup

### 1. Install Python

Download Python from [python.org](https://www.python.org/downloads/) and make sure to **Add Python to PATH** during installation.

Check installation:

```bash
python --version
pip --version
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/rkgupta7463/Task-Manager.git
cd task-manager
```

---

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

* **Windows:**

```bash
venv\Scripts\activate
```

* **Linux/Mac:**

```bash
source venv/bin/activate
```

---

### 4. Install Dependencies

If `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

If not, manually install:

```bash
pip install django
django-ninja
djangorestframework
djangorestframework-simplejwt
```

---

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

---

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000
```

---

## API Endpoints (prefixed with `api/v1/`)

### User Authentication

| Method | Endpoint          | Description         |
| ------ | ----------------- | ------------------- |
| POST   | `/api/v1/signup/` | Create a new user   |
| POST   | `/api/v1/login/`  | Login existing user |
| POST   | `/api/v1/logout/` | Logout user         |

---

### Task Endpoints

| Method | Endpoint                        | Description                |
| ------ | ------------------------------- | -------------------------- |
| GET    | `/api/v1/tasks/`                | List all tasks (paginated) |
| GET    | `/api/v1/tasks/{task_id}/`      | Retrieve task details      |
| POST   | `/api/v1/tasks/`                | Create a new task          |
| PUT    | `/api/v1/tasks/{task_id}/`      | Update a task              |
| DELETE | `/api/v1/tasks/{task_id}/`      | Delete a task              |
| PATCH  | `/api/v1/mark/tasks/{task_id}/` | Mark a task as completed   |

---

### Task Filtering

| Method | Endpoint                 | Description                                                        |
| ------ | ------------------------ | ------------------------------------------------------------------ |
| GET    | `/api/v1/filters/tasks/` | Filter tasks by query and completion status (pagination supported) |

Query parameters:

* `query` → search by task title or description
* `completed` → `true` or `false`
* `offset` → start index for pagination
* `limit` → number of tasks per page

Example:

```
/api/v1/filters/tasks/?query=meeting&completed=false&offset=0&limit=10
```

---

## JWT Authentication

1. Login to get a JWT token:

```http
POST /api/v1/login/
{
  "email": "your-email",
  "password": "your-password"
}
```

2. Use the token in **Authorization header** for protected endpoints:

```
Authorization: Bearer <your-token>
```

---

## Example API Requests

**Create Task**

```http
POST /api/v1/tasks/
Authorization: Bearer <token>
{
  "title": "Finish project",
  "description": "Complete the Django Ninja task manager",
 "completed":true
}
```

**Mark Task Completed**

```http
PATCH /api/v1/mark/tasks/1/
Authorization: Bearer <token>
{
  "completed": true
}
```

**Filter Tasks**

```http
GET /api/v1/filters/tasks/?query=project&completed=false&offset=0&limit=5
Authorization: Bearer <token>
```

---

## Testing

Run test cases:

```bash
python manage.py test
```

Test cases are located in `test.py` and cover:

* Task creation, retrieval, update, deletion
* Filtering tasks
* Marking tasks completed
* Authentication endpoints

---

## Pagination

All task listing endpoints support pagination using `offset` and `limit` parameters.

```http
/api/v1/tasks/?offset=0&limit=10
```

---

## Technologies Used

* Python 3.10+
* Django
* Django Ninja
* JWT Authentication
* SQLite 

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Make changes
3. Submit a pull request

---

## License

This project is licensed under the **MIT License**.
