#!/bin/bash

NAME="HoneyBeeHive"                                  # Name of the application
DJANGODIR=/var/projects/hbh/HoneyBeeHive             # Django project directory
DJANGO_SETTINGS_MODULE=HoneyBeeHive.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=HoneyBeeHive.wsgi                     # WSGI module name

echo "Starting $NAME workers as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
export WORKON_HOME=/home/delos/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
workon hbh_django_17
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH


exec "$DJANGODIR"/manage.py celery -A $NAME worker -l warning

