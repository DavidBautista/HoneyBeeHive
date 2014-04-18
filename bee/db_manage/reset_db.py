import os
import sys
from django.db import connection
import threading

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HoneyBeeHive.settings")

from django.core.management.commands import syncdb

def sync():
    syncdb.Command().execute(noinput=True, verbosity=1, database='default')


def deletetables():
    cursor = connection.cursor()
    print "DROP"
    try:
        cursor.execute("DROP DATABASE honeybeehive")
    except:
        pass
    print "CREATE"
    cursor.execute("CREATE DATABASE honeybeehive CHARACTER SET utf8 COLLATE utf8_general_ci;")
    cursor.close()

if __name__ == "__main__":
    t1 = threading.Thread(target=deletetables)
    t1.start()
    t1.join()
    sync()


