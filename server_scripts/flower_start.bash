#!/bin/bash
 
NAME="HoneyBeeHive"                                  # Name of the application
DJANGODIR=/var/projects/hbh/HoneyBeeHive             # Django project directory
USER=delos                                        # the user to run as
GROUP=delos                                     # the group to run as
AUTH_USER=admin
AUTH_PASS=honey2014
HOST=vps63619.ovh.net
PORT=5555
PERSISTENT=True
BROKER=redis://localhost:6379/0
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


exec flower --address=$HOST --port=$PORT --basic_auth="$AUTH_USER":"$AUTH_PASS" --persistent=$PERSISTENT --broker=$BROKER
 
