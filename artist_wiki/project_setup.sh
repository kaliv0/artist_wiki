#!/usr/bin/env bash

echo "Creating virtual environment"
python3 -m venv env
source env/bin/activate

echo "Installing dependencies"
pip3 install -r requirements.txt

echo "Creating migrations"
#python3 manage.py makemirations
python3 manage.py migrate

echo "Seeding database"
fixture=$(ls seed/)
python3 manage.py loaddata seed/"$fixture"

echo "Setting up admin"
python3 manage.py shell <<<"from django.contrib.auth.models import User
User.objects.filter(is_superuser=True).delete()"
python3 manage.py createsuperuser

echo "Starting application"
python3 manage.py runserver
