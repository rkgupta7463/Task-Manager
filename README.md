# Task Manager API

A simple **Task Manager API** built with **Django** and **Django Ninja (For RESTAPI)**.
All API endpoints are prefixed with `api/v1/`. This API allows users to manage tasks with full **CRUD operations**, **filtering**, **marking tasks as completed**, and **JWT authentication & authorization**. Test cases are included to ensure API reliability.

---

### 🔐 Role-based Access Control

* **Superuser (Admin)**: Can perform all CRUD operations on any task (create, read, update, delete tasks created by any user).

* **Regular User**: Can only manage their own tasks (create tasks, update only their tasks, delete their tasks, filter their tasks).

---

## Features

### User Authentication

* Signup
* Login
* Logout

### Task Management

* Create, Read, Update, Delete tasks
* Mark tasks as completed
* Filter tasks by title, description, and completion status
* Pagination support

### Testing

* Test cases included in `test.py`

---

## Requirements

* Python 3.10+
* pip
* Virtual environment

---

## Step-by-Step Setup

### 1. Install Python

Download Python from [python.org](https://www.python.org/downloads/) and ensure **Add Python to PATH** is selected.

Check installation:

```bash
python --version
pip --version
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/rkgupta7463/Task-Manager.git
cd Task-Manager
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

Or manually install:

```bash
pip install django django-ninja PyJWT
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

To view interactive API documentation:

```
http://127.0.0.1:8000/api/docs
```

---

## API Endpoints (prefixed with `api/v1/`)

### User Authentication

| Method | Endpoint   | Description         |
| ------ | ---------- | ------------------- |
| POST   | `api/v1/signup/` | Create a new user   |
| POST   | `api/v1/login/`  | Login existing user |
| POST   | `api/v1/logout/` | Logout user         |

---

### Task Endpoints

| Method | Endpoint                 | Description                |
| ------ | ------------------------ | -------------------------- |
| GET    | `api/v1/tasks/`                | List all tasks (paginated) |
| GET    | `api/v1/tasks/{task_id}/`      | Retrieve task details      |
| POST   | `api/v1/tasks/`                | Create a new task          |
| PUT    | `api/v1/tasks/{task_id}/`      | Update a task              |
| DELETE | `api/v1/tasks/{task_id}/`      | Delete a task              |
| PATCH  | `api/v1/mark/tasks/{task_id}/` | Mark a task as completed   |

---

### Task Filtering

| Method | Endpoint          | Description                                                        |
| ------ | ----------------- | ------------------------------------------------------------------ |
| GET    | `api/v1/filters/tasks/` | Filter tasks by query and completion status (pagination supported) |

Query parameters:

* `query` → search by task title or description
* `completed` → `true` or `false`
* `offset` → start index for pagination
* `limit` → number of tasks per page

Example:

```
/api/v1/filters/tasks/?query=project&completed=false&offset=0&limit=5
```

---

## Example Requests & Responses

### 1. Signup

**URL:** 

`/api/v1/signup/`

**Method:** POST

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "password123",
  "full_name": "John Doe",
  "phone_no": "1234567890"
}
```

**Response:**

```json
{
  "status": true,
  "message": "User created successfully",
  "access_token": "<jwt-token>",
  "data": {
    "id": 1,
    "email": "user@example.com",
    "full_name": "John Doe",
    "phone_number": "1234567890"
  }
}
```

---

### 2. Login

**URL:** `/api/v1/login/`

**Method:** POST

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**

```json
{
  "status": true,
  "message": "Login successful",
  "token": "<jwt-token>",
  "user_detail": {
    "id": 1,
    "email": "user@example.com",
    "full_name": "John Doe",
    "phone_number": "1234567890"
  }
}
```

---

### 3. Logout

**URL:** `/api/v1/logout/`

**Method:** POST

**Headers:**

```
Authorization: Bearer <jwt-token>
```

**Response:**

```json
{
  "status": true,
  "message": "Logout successful",
  "data": null
}
```

---

### 4. Task Management

**List Tasks**

**URL:** `/api/v1/tasks/`

**Method:** GET

**Headers:** `Authorization: Bearer <jwt-token>`

**Query Parameters:** `offset=0`, `limit=10`

**Response:**

```json
{
  "status": true,
  "message": "Tasks fetched successfully",
  "data": [
    {
      "id": 1,
      "title": "Finish project",
      "description": "Complete the Django Ninja task manager",
      "completed": false,
      "created_at": "2025-09-30T15:44:46.477Z",
      "updated_at": "2025-09-30T15:44:46.260Z"
    }
  ]
}
```

**Retrieve Task**

**URL:** `/api/v1/tasks/{task_id}/`

**Method:** GET

**Response:**

```json
{
  "status": true,
  "message": "Task details fetched",
  "data": {
    "id": 1,
    "title": "Finish project",
    "description": "Complete the Django Ninja task manager",
    "completed": false,
    "created_at": "2025-09-30T15:44:46.477Z",
    "updated_at": "2025-09-30T15:44:46.260Z"
  }
}
```

**Create Task**

**URL:** `/api/v1/tasks/`

**Method:** POST

**Request Body:**

```json
{
  "title": "Finish project",
  "description": "Complete the Django Ninja task manager",
  "completed": true
}
```

**Response:**

```json
{
  "status": true,
  "message": "Task created successfully",
  "data": {
    "id": 1,
    "title": "Finish project",
    "description": "Complete the Django Ninja task manager",
    "completed": true,
    "created_at": "2025-09-30T15:44:46.477Z",
    "updated_at": "2025-09-30T15:50:46.260Z"
  }
}
```

**Update Task**

**URL:** `/api/v1/tasks/{task_id}/`

**Method:** PUT

**Request Body:**

```json
{
  "title": "Finish project ASAP",
  "description": "Complete task quickly",
  "completed": true
}
```

**Response:**

```json
{
  "status": true,
  "message": "Task updated successfully",
  "data": {
    "id": 1,
    "title": "Finish project ASAP",
    "description": "Complete task quickly",
    "completed": true,
    "created_at": "2025-09-30T15:44:46.477Z",
    "updated_at": "2025-09-30T15:50:46.260Z"
  }
}
```

**Delete Task**

**URL:** `/api/v1/tasks/{task_id}/`

**Method:** DELETE

**Response:**

```json
{
  "status": true,
  "message": "Task deleted successfully",
  "data":  {
    "id": null,
    "title": "Finish project ASAP",
    "description": "Complete task quickly",
    "completed": false,
    "created_at": "2025-09-30T15:44:46.477Z",
    "updated_at": "2025-09-30T15:50:46.260Z"
  }
}
```

**Mark Task Completed**

**URL:** `/api/v1/mark/tasks/{task_id}/`

**Method:** PATCH

**Request Body:**

```json
{
  "completed": true
}
```

**Response:**

```json
{
  "status": true,
  "message": "Task marked as completed",
  "data": {
    "id": 1,
    "title": "Finish project ASAP",
    "description": "Complete task quickly",
    "completed": true,
    "created_at": "2025-09-30T15:44:46.477Z",
    "updated_at": "2025-09-30T15:50:46.260Z"
  }
}
```

---

### 5. Task Filtering

**URL:** `/api/v1/filters/tasks/`

**Method:** GET

**Query Parameters:**

* `query` → search by title/description
* `completed` → true or false
* `offset` → start index
* `limit` → number of tasks

**Example:**

```
/api/v1/filters/tasks/?query=project&completed=false&offset=0&limit=5
```

**Response:**

```json
{
  "status": true,
  "message": "Filtered tasks fetched",
  "data": [
    {
      "id": 1,
      "title": "Finish project ASAP",
      "description": "Complete task quickly",
      "completed": false,
      "created_at": "2025-09-30T15:44:46.477Z",
      "updated_at": "2025-09-30T15:50:46.260Z"
    }
  ]
}
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

All task listing endpoints support pagination using `offset` and `limit` parameters:

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
