#!/bin/bash

echo "Building project"
python3.10 -m pip install -r requirements.txt

echo "Make migrations"
python3.10 manage.py makemigrations
python3.10 manage.py migrate

echo "Collecting static"
python3.10 manage.py collectstatic