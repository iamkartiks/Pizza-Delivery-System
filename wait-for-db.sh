#!/bin/sh

while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 5
done

# python manage.py runserver 0.0.0.0:8000