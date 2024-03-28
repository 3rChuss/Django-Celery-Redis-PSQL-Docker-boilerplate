#!/bin/bash

APP_PORT=${PORT:-8000}

echo "Waiting for postgres..."
sleep 5
echo "Postgres started"

echo "Running migrations"
/opt/venv/bin/python manage.py makemigrations --noinput
/opt/venv/bin/python manage.py migrate --noinput
echo "Migrations complete"

echo "Creating superuser"
/opt/venv/bin/python manage.py superuser || true
echo "Superuser created"

echo "Generate api documentation"
/opt/venv/bin/python manage.py spectacular --color --file schema.yml
echo "Api documentation generated"

echo "Collecting static files"
/opt/venv/bin/python manage.py collectstatic --noinput

echo "Starting server"
/opt/venv/bin/gunicorn backend.wsgi:application --bind "0.0.0.0:${APP_PORT}" --workers 4 --threads 4 --worker-class gthread --worker-tmp-dir /dev/shm --worker-connections 1000 --timeout 60 --log-level info --log-file -