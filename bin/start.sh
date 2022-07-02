#!/bin/bash

# Temporary.
dos2unix /app/.env

. /app/venv/bin/activate

. /app/.env

/app/src/manage.py collectstatic -c --noinput

/app/src/manage.py runserver 0.0.0.0:8000
