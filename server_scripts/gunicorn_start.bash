#!/bin/bash
 
NAME="HoneyBeeHive"                                  # Name of the application
DJANGODIR=/var/projects/hbh/HoneyBeeHive             # Django project directory
SOCKFILE=/var/projects/hbh/run/gunicorn.sock  # we will communicte using this unix socket
USER=delos                                        # the user to run as
GROUP=delos                                     # the group to run as
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=HoneyBeeHive.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=HoneyBeeHive.wsgi                     # WSGI module name
 
echo "Starting $NAME as `whoami`"
 
# Activate the virtual environment
cd $DJANGODIR
export WORKON_HOME=/home/delos/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
workon hbh_django_17
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --bind=unix:$SOCKFILE
