#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

# Only create superuser if doesn't exist
if [[ -z "${SKIP_SUPERUSER}" ]]; then
  python manage.py createsuperuser --noinput --email admin@example.com || true
fi