#!/bin/bash

# Temporary.
dos2unix /app/.env

. /app/venv/bin/activate

. /app/.env

python /app/src/manage.py collectstatic -c --noinput

python /app/src/manage.py runserver 0.0.0.0:8000
