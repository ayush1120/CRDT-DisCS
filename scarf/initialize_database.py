import os
import shutil
import random
import django
from django.db import models
import json
from faker import Faker 
import uuid

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scarf.settings")
django.setup()


from django.contrib.auth.models import User
from scarf import settings


from discs.settings import DATABASES_NAMES
from discs.services import databaseWrite
from discs.manageDatabases import  listDatabases, deleteDatabase

def add_fake_user(dbName=None):
    fake = Faker()    
    name = fake.name()
    age = random.randint(4, 72)
    user_id = uuid.uuid4().hex[:6].upper()
    examples = ['Indian', 'American', 'Bósnia', 'Turca', 'Italiana', 'Argelina', 'Moldava']
    nationality = examples[random.randint(0,6)]

    databaseWrite.addUser(user_id=user_id, name=name, age=age, nationality=nationality, dbName=dbName)


def add_data():
    User.objects.create_superuser('ayush', 'ayush@iitbhilai.ac.in', 'ayush')
    Faker.seed(69)
    for database in DATABASES_NAMES:
        for i in range(1, random.randint(2,6)):
            add_fake_user(dbName=database)




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

    databases = listDatabases()
    for database in databases:
        if 'CRDT-DisCS__DB' in database:
            deleteDatabase(database)

    os.system("python manage.py makemigrations")
    os.system("python manage.py migrate --run-syncdb")
    add_data()
