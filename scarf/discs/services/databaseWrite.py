import mongoengine
import pymongo
from discs.data.users import User
from discs.settings import  connect_with_database


@connect_with_database
def addUser(user_id, name, age, nationality, **kwargs):
    user = User()
    user.user_id = user_id
    user.name = name
    user.age = age
    user.nationality = nationality

    user.save()

    return user


@connect_with_database
def changeUserDetails(user_id, name, age, nationality, **kwargs):
    user = User.objects(user_id=user_id).first()
    user.name = name
    user.age = age
    user.nationality = nationality
    user.save()
    return user




@connect_with_database
def deleteUser(user_id, **kwargs):
    user = User.objects(user_id=user_id).first()
    user.delete()