#!/bin/bash

echo "Building project"
python3.11.2 -m pip install -r requirements.txt

echo "Make migrations"
python3.11.2 manage.py makemigrations
python3.11.2 manage.py migrate

echo "Collecting static"
python3.11.2 manage.py collectstatic