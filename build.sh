#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# para que se genere la carpeta de archivos
python manage.py collectstatic --no-input


# y lo mismo 
python manage.py migrate

