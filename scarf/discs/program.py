import mongoengine
from data.users import User
from services import databaseWrite

def global_init():
    mongoengine.register_connection(alias='core', name='test_db')


def readUsers(user_id):
    user =  User.objects(user_id=user_id).first()
    return user

def print_user(user):
    print('user_id: ', user.user_id)
    print('name: ', user.name)
    print('age: ', user.age)

def main():
    global_init()

    # user = databaseWrite.addUser('13', 'Ram', 34, 'Indian')
    curr_id =  '13'
    curr_user = readUsers(curr_id)
    # print_user(curr_user)
    if not curr_user:
        print("Already Deleted")
    else:
        print_user(curr_user)
        databaseWrite.deleteUser(curr_id)
        print("User Deleted")


if __name__ == "__main__":
    main()