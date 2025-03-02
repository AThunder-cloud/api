# FastAPI + SQLite Example

A FastAPI-based backend with SQLite, following a structured architecture (Controller-Service-Repository).

---

## Features
- 🚀 FastAPI for high-performance APIs  
- 🗄️ SQLite as the database  
- 🏗️ Structured architecture (Controller → Service → Repository)  
- ⚡ Async SQLAlchemy for database operations  
- ✅ Pydantic for request validation  

---

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/fastapi-project.git
cd fastapi-project
```

### 2. Create & Activate Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run Database Migrations
```sh
alembic upgrade head
```

### 5. Start the FastAPI Server
```sh
uvicorn main:app --reload
```

---

## Project Structure
```
app/
│── controllers/        # API Endpoints (Controllers)
│   ├── user_controller.py
│
│── services/           # Business Logic (Services)
│   ├── user_service.py
│
│── repositories/       # Database Queries (Repositories)
│   ├── user_repository.py
│
│── models/             # Database Models
│   ├── user.py
│
│── schemas/            # Pydantic Schemas (DTOs)
│   ├── user_schemas.py
│
│── db/                 # Database Configuration
│   ├── database.py
│
│── main.py             # FastAPI Entry Point
│── requirements.txt    # Dependencies
│── .gitignore          # Git Ignore File
│── README.md           # Documentation
```

---

## API Endpoints
### User API
| Method | Endpoint | Description |
|--------|---------|------------|
| `POST` | `/api/users` | Create a new user |
| `GET`  | `/api/users` | Get all users |
| `DELETE` | `/api/users/{id}` | Delete a user |

---

## Example API Calls
### Create a User
```sh
curl -X 'POST' 'http://127.0.0.1:8000/api/users' \
-H 'Content-Type: application/json' \
-d '{
  "name": "John Doe",
  "email": "john@example.com"
}'
```

### Get All Users
```sh
curl -X 'GET' 'http://127.0.0.1:8000/api/users'
```

### Delete a User
```sh
curl -X 'DELETE' 'http://127.0.0.1:8000/api/users/1'
```

---

## Running with Docker (Optional)
If you want to run the project in **Docker**, use:
```sh
docker-compose up --build
```

---

## License
This project is open-source under the **MIT License**.

---

## Contributing
1. Fork the repository  
2. Create a new branch (`feature/new-feature`)  
3. Commit your changes  
4. Open a pull request  

---

## Contact
📧 **Email**: arpitsingh7802@gmail.com  
🐙 **GitHub**: [AThunder-cloud](https://github.com/AThunder-cloud)  

