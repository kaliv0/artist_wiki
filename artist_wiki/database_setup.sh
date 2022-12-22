#!/usr/bin/env bash

echo "Migrating to database"
python3 manage.py migrate

fixtures=$(ls seed/)
while IFS= read -r fixture; do
  python3 manage.py loaddata seed/"$fixture"
done <<<"$fixtures"

echo "Setting up admin"
python3 manage.py shell <<<"from django.contrib.auth.models import User
User.objects.filter(is_superuser=True).delete()"
python3 manage.py createsuperuser

echo "All set"
