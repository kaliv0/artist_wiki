#!/usr/bin/env bash

echo "Migrating to database"
python3 manage.py migrate

echo "Seeding database"
fixture="seed/db.json"
python3 manage.py loaddata "$fixture"

echo "Setting up admin"
python3 manage.py shell <<<"from django.contrib.auth.models import User
User.objects.filter(is_superuser=True).delete()"
python3 manage.py createsuperuser

echo "All set"
