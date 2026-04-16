TaskMaster API



TaskMaster API is a RESTful backend application built with FastAPI.

It provides secure user authentication using JWT and task management functionality with database persistence.

Overview



This project demonstrates:

JWT authentication (OAuth2 Password Flow)

Password hashing using bcrypt

Protected API routes

Task creation and retrieval

Database modeling with SQLAlchemy

Tech Stack

Python 3

FastAPI

SQLAlchemy

SQLite

Pydantic

python-jose (JWT)

Passlib (bcrypt)

Uvicorn

Installation

Clone repository

git clone https://github.com/your-username/taskmaster-api.git

cd taskmaster-api

Create virtual environment

python -m venv venv

Activate virtual environment (Windows)

venv\Scripts\activate

Install dependencies

pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose python-dotenv python-multipart pydantic[email]

Run the application



uvicorn app.main:app –reload –port 8001



Open in browser:

http://127.0.0.1:8001/docs

Authentication Flow

Register user

Login

Click Authorize in Swagger

Use protected endpoints

Endpoints



Authentication:

POST /auth/register

POST /auth/login



Tasks:

GET /tasks

POST /tasks

Author



Gheorghe-Gabriel Iancu

