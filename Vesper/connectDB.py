import sys
sys.path.append('../scarf/')
import json

from discs.data.underlying.posts import Post
from discs.populate import get_fake_post
from discs.services.underlying.databaseWrite import add_post, add_user
from discs.services.underlying.databaseRead import readUsers
from discs.manageDatabases import listDatabases, deleteDatabase


dbName = "test_lola"

# name "Leslie Lampart"

# name msg

msg= {
    'type' : 'add_user',
    'args' : {
        'name':'Sukhiya', 
        'username':'soku',
        'nationality':'Indian',
        'age':20
    }
}



if __name__ == "__main__":
    print(listDatabases())
    if msg['type'] == 'add_user':
        args = msg['args']
        add_user(name=args['name'],
        username=args['username'], 
        nationality=args['nationality'], 
        age=args['age'],
        dbName=dbName)
    print(listDatabases())
    users = readUsers(dbName=dbName)
    for user in users:
        print(user.name)
        print(user.age)
        print(user.username)
        print(user.nationality)

    deleteDatabase(dbName=dbName)
    print(listDatabases())

    # a = json.dumps(msg) # dumps -> python object to json string 
    # print("type of a : ", type(a))
    # print(f'a : {a}')
    # print('\n-----------------------------\n')
    # b = json.loads(a) # loads -> json string to python object
    # print(f'type of b : {type(b)}')
    # print(f'b : \n{b}')
