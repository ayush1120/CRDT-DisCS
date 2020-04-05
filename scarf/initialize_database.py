import os
import shutil
import random
import django
from django.db import models
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scarf.settings")
django.setup()


from django.contrib.auth.models import User
from scarf import settings



def add_data():
    User.objects.create_superuser('ayush', 'ayush@iitbhilai.ac.in', 'ayush')



if __name__ == "__main__":
    BASE_DIR = settings.BASE_DIR
    if os.path.exists(os.path.join(settings.BASE_DIR, "db.sqlite3")):
        os.remove(os.path.join(settings.BASE_DIR, "db.sqlite3"))
    else:
        print("The file does not exist")
    
    if os.path.exists(os.path.join(BASE_DIR, "sage", "migrations")):
        shutil.rmtree(os.path.join(BASE_DIR, "sage", "migrations"))

    if os.path.exists(os.path.join(BASE_DIR, "scarf", "__pycache__")):
        shutil.rmtree(os.path.join(BASE_DIR, "scarf", "__pycache__"))
    
    if os.path.exists(os.path.join(BASE_DIR, "sage", "__pycache__")):
        shutil.rmtree(os.path.join(BASE_DIR, "sage", "__pycache__"))

    os.system("python manage.py makemigrations")
    os.system("python manage.py migrate --run-syncdb")
    add_data()
