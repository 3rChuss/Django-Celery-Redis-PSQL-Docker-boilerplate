# Django + DRF + Celery + Redis + PostgresSQL + Docker + NGINX ===>>> BOILERPLATE <<<===

This project consists of two main applications: `backend` and `frontend`.

## Backend

The backend application is located in the `/apps/backend` directory. It is built with Python, Django, Django Rest Framework, Celery, Redis, and PostgreSQL.

### Features

- Admin Panel: Django's built-in admin panel is used for administrative tasks.
- API: Django Rest Framework is used to build the API.
- Task Queue: Celery along with Redis is used for task queue management.
- Database: PostgreSQL is used as the primary database.

The API documentation can be accessed at `/api/swagger`.

## Frontend

The frontend application is located in the `/apps/frontend` directory. It is built with Vite and React.

## Docker

The `docker` directory contains Dockerfiles for the backend, frontend, and Nginx. Docker is used to containerize the applications and Nginx is used as a reverse proxy.

## Getting Started

To get a local copy up and running, follow these steps:

1. Clone the repository
2. Navigate to the project directory
3. Run `docker-compose up`

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

## License

Distributed under the MIT License. See `LICENSE` for more information.
