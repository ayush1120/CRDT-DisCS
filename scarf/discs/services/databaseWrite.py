from typing import List, Optional
import mongoengine
import pymongo
from data.users import User

def addUser(user_id, name, age, nationality):
    user = User()
    user.user_id = user_id
    user.name = name
    user.age = age
    user.nationality = nationality

    user.save()

    return user


def changeUserDetails(user_id, name, age, nationality):
    user = User.objects(user_id=user_id).first()

    user.name = name
    user.age = age
    user.nationality = nationality

    user.save()
    return user


def deleteUser(user_id):
    user = User.objects(user_id=user_id).first()
    user.delete()