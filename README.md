# LinkUp — Django Social Media App

A real-time social media backend built with **Django**, **Django REST Framework**, and **Django Channels**, fully containerized using **Docker Compose** with PostgreSQL and Redis.

This project is designed to be easy to run locally and ready for further scaling.

---

## Features

* User authentication
* User profiles
  n- Create, edit, delete posts
* Likes and interactions
* Real-time chat (WebSockets with Django Channels + Redis)**
* REST API for frontend clients
* PostgreSQL database
* Dockerized development environment

---

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Realtime:** Django Channels + Daphne
* **Database:** PostgreSQL
* **Cache / Broker:** Redis
* **Containerization:** Docker & Docker Compose

---

## Requirements

You need:

* Docker
* Docker Compose

---

## Getting Started (Docker Compose)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/linkup.git
cd linkup
```

---

### 2. Build and run the project

```bash
docker compose up --build
```

The app will be available at:

```
http://localhost:8001/
```

---

## Services Overview

Your app runs with three containers:

| Service | Description                   | Port        |
| ------- | ----------------------------- | ----------- |
| web     | Django + Daphne (ASGI server) | 8001 → 8000 |
| db      | PostgreSQL database           | 5432        |
| redis   | Redis for Channels / cache    | 6379        |

---

## Environment Variables Used

These are provided via `docker-compose.yml`:

```env
POSTGRES_DB=linkupdb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432

REDIS_URL=redis://redis:6379
```

---

## Startup Flow (Important for understanding the project)

When the `web` container starts, it automatically runs:

```bash
python wait_for_db.py
python manage.py migrate
daphne -b 0.0.0.0 -p 8000 a_core.asgi:application
```

This means:

* The app waits for PostgreSQL to be ready
* Runs migrations automatically
* Starts the ASGI server using **Daphne** (required for WebSockets)

No manual setup needed after `docker compose up`.

---

## Create Superuser

To access Django admin:

```bash
docker compose exec web python manage.py createsuperuser
```

Admin panel:

```
http://localhost:8001/admin/
```

---

## Project Structure (simplified)

```
linkup/
│
├── a_chat/
├── a_core/          # Core project (settings, ASGI, URLs)
├── a_home/          # Your Django apps (posts, users, etc.)
├── a_users/
├── media/
├── static/
├── templates/
├── .dockerignore
├── manage.py
├── wait_for_db.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Example API Endpoints (adjust to your project)

| Method | Endpoint              | Description   |
| ------ | --------------------- | ------------- |
| POST   | /api/auth/register/   | Register user |
| POST   | /api/auth/login/      | Login         |
| GET    | /api/posts/           | List posts    |
| POST   | /api/posts/           | Create post   |
| POST   | /api/posts/{id}/like/ | Like post     |

---

## Future Ideas

* Notifications system
* Media uploads (S3 / Cloudinary)
* Frontend client (React / Next.js)
* Deployment with Docker + Nginx

---

## Contributing

Pull requests are welcome:

1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Open a PR

---

If you find this project helpful, consider giving it a star⭐!
