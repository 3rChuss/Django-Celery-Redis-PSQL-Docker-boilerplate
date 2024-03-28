#!/bin/sh

until cd /apps/backend
do
    echo "Waiting for server volume..."
done

/opt/venv/bin/celery -A backend worker --loglevel=info --concurrency 1 -E
