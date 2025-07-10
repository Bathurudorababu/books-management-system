# 📚 Books Management API

A backend system built with **FastAPI** and **MongoDB** (via Motor) that supports:

- 🔐 JWT-based user authentication
- 🧾 Secure password hashing
- 📘 Book creation, listing, deletion (user-specific)
- ✅ Async operations using motor
- 🆔 UUID-based IDs
- 🔒 Token expiration & validation

---

## ⚙️ Tech Stack

- **FastAPI** (backend framework)
- **MongoDB** with Motor (async DB access)
- **Pydantic** (data validation)
- **Passlib** (password hashing)
- **Python-Jose** (JWT handling)
- **UUID** (for unique IDs)

---

## 📦 API Features

### 🔐 Authentication Endpoints

| Method | Endpoint       | Description                   |
|--------|----------------|-------------------------------|
| POST   | /auth/signup | Register a new user           |
| POST   | /auth/login  | Login and get access token    |
| GET    | /auth/me     | Get current logged-in user    |

### 📘 Book CRUD (JWT Protected)

| Method | Endpoint             | Description                        |
|--------|----------------------|------------------------------------|
| POST   | /books/            | Create a new book                  |
| GET    | /books/            | List all books (optionally by genre) |
| GET    | /books/{id}        | Get a book by ID                   |
| DELETE | /books/{id}        | Delete a book (if you are creator) |

---


## 🛠️ Setup Instructions

### 1. Clone the Repository

To begin, clone the repository to your local machine:

```bash
git clone https://github.com/Bathurudorababu/books-management-system.git
cd user-management-backend-api
```

### 2. Replace the mongourl link and secretkey in .env file with yours if needed
- MONGO_URL = your url
- SECRET_KEY = your secret key

### 3. Run the following command 
uvicorn app.main:app --reload

### 4. Access the Application
- 🚀 **FastAPI Backend**:  
  [http://localhost:8000](http://localhost:8000)

- 📘 **Swagger UI (API Docs)**:  
  [http://localhost:8000/docs](http://localhost:8000/docs)

## 📬 Contact

Feel free to open issues or contribute to the repository.

Happy coding! 🚀
