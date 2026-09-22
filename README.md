# Flask REST API

A hands-on RESTful API project built with **Python and Flask**, following the **REST APIs with Flask and Python** course by Packt on Coursera.

The project explores backend API development, database management, authentication, data validation, API testing, and deployment concepts using modern Python tools.

## 🚀 Features

* RESTful API development with Flask
* CRUD operations for resources
* SQLAlchemy ORM for database interaction
* Database relationships, including one-to-many and many-to-many
* Marshmallow schemas for serialization and validation
* User registration and authentication
* JWT-based authentication with Flask-JWT-Extended
* Protected API endpoints
* JSON request and response handling
* API error handling
* API testing
* Docker containerization
* PostgreSQL database integration
* Background task processing with Redis and RQ
* Email notifications
* Deployment concepts using Render

## 🛠️ Technologies & Tools

* **Python**
* **Flask**
* **Flask-Smorest**
* **SQLAlchemy**
* **Marshmallow**
* **Flask-JWT-Extended**
* **PostgreSQL**
* **SQLite**
* **Redis**
* **RQ**
* **Docker**
* **Git & GitHub**
* **Insomnia**
* **Render**

## 📁 Project Structure

```text
flask-rest-api/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── resources/
│   ├── item.py
│   ├── store.py
│   ├── tag.py
│   └── user.py
│
├── models/
│   ├── item.py
│   ├── store.py
│   ├── tag.py
│   └── user.py
│
├── schemas/
│   ├── item.py
│   ├── store.py
│   ├── tag.py
│   └── user.py
│
└── migrations/
```

> The exact structure may vary depending on the stage of the project.

## 🔑 Main Concepts

### REST API

The project demonstrates how to build RESTful endpoints using HTTP methods such as:

* `GET` — retrieve resources
* `POST` — create resources
* `PUT` / `PATCH` — update resources
* `DELETE` — remove resources

### SQLAlchemy

SQLAlchemy is used as the ORM for interacting with the database through Python models rather than writing raw SQL for every operation.

The project includes relationships between resources and demonstrates how related records can be created, retrieved, and managed.

### Marshmallow

Marshmallow schemas are used to:

* Validate incoming data
* Serialize database objects
* Deserialize JSON requests
* Control which fields can be read or written

### Authentication

JWT authentication is implemented using **Flask-JWT-Extended**.

Authenticated users can access protected endpoints by providing a valid JWT token.

## 🧪 API Testing

The API endpoints are tested using **Insomnia**.

Example operations include:

```http
GET /items
GET /items/<item_id>
POST /items
PUT /items/<item_id>
DELETE /items/<item_id>
```

Authentication-protected endpoints require a valid JWT access token.

## 🐳 Docker

The application can be containerized using Docker.

Build the image:

```bash
docker build -t flask-rest-api .
```

Run the container:

```bash
docker run -p 5000:5000 flask-rest-api
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/flask-rest-api.git
cd flask-rest-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
flask run
```

The API will normally be available at:

```text
http://127.0.0.1:5000
```

## 🔐 Environment Variables

Sensitive information should not be hard-coded into the source code.

Example:

```env
DATABASE_URL=your_database_url
JWT_SECRET_KEY=your_secret_key
```

Create a `.env` file locally and add it to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

## 📚 What I Learned

Through this project, I gained practical experience with:

* Designing RESTful APIs
* Flask backend development
* CRUD operations
* ORM-based database development
* Database relationships
* Request validation and serialization
* JWT authentication
* API testing
* Docker containerization
* PostgreSQL
* Background task processing
* Git and GitHub workflow
* Backend application deployment

## 🎯 Purpose

This repository is part of my backend development and machine learning engineering learning journey.

I am building these skills to develop and deploy **production-oriented APIs for web applications and machine learning models**.

## 📖 Course

Based on:

**REST APIs with Flask and Python in 2024**
Provider: **Packt**
Platform: **Coursera**

The course covers Flask REST API development, SQLAlchemy CRUD operations, JWT authentication, Docker, API testing, background tasks, and deployment.

## 👨‍💻 Author

**Anas Ibrahim**

Computer Science Undergraduate | Python | Flask | Machine Learning | AI

---

⭐ If you find this project useful, feel free to explore the repository and its implementation.
