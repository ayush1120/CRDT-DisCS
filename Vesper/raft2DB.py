import json
import sys
import random
import time
import mongoengine


sys.path.append("../scarf/")

from discs.manageDatabases import listDatabases, deleteDatabase
from discs.services.underlying.databaseRead import readUsers, print_users
from discs.services.underlying.databaseWrite import add_post, add_user, update_user_name


msg = None

with open("test_msgs/test.json", 'r') as json_file:
        msg = json.load(json_file)

dbName = "test_lola"

# name "Leslie Lampart"

# name msg

# msg = {
#         "type": "add_user",
#         "args": {
#                 "name": "Sukhiya",
#                 "username": "soku",
#                 "nationality": "Indian",
#                 "age": 20
#         }
#     }
#     {
#         "type": "update_user_name",
#         "args": {"name": "Sukhi",
#                  "username": "soku"}
#     },
#     {
#         "type": "update_user_nationality",
#         "args": {
#                 "username": "soku",
#                 "nationality": "Belgian"
#         }
#     },
#     {
#         "type": "update_user_age",
#         "args": {
#                 "username": "soku",
#                 "age": 30
#         }
#     },
    # {
#         "type": "add_follower",
#         "args": {
#                 "username": "soku",
#                 "follower": "lmao"
#         }
#     },
    # {
#         "type": "remove_follower",
#         "args": {
#                 "username": "soku",
#                 "follower": "lmao"
#         }
#     },
    # {
#         "type": "add_post",
#         "args": {
#                 "author": "hoihoi",
#                 "content": "ye lo content",
                # "likes": 1
#         }
#     },
    # {
#         "type": "change_post_content",
#         "args": {
#                 "postid": 123,
#                 "content": "ye lo new content",
#         }
#     },
    # {
#         "type": "add_post_likes",
#         "args": {
#                 "postid": 123,
#                 "username": "soku",
#         }Messege
#     },
    # {
#         "type": "reduce_post_likes",
#         "args": {
#                 "postid": 123,
#                 "username": "soku",
#         }
#     },
    # {
#         "type": "deletePost",
#         "args": {
#                 "postid": 123
#         }
#     }
# ]



def parseMessage(msg, dbName='CRDT-DisCS_Test'):
    if msg["type"] == "add_user":
        args = msg["args"]
        add_user(name=args["name"],
                username=args["username"],
                nationality=args["nationality"],
                age=args["age"],
                dbName=dbName)
    if msg["type"] == "update_user_name":
        print("Hello name")
        args = msg["args"]
        update_user_name(username=args["username"],
                        name=args["name"],
                        dbName=dbName)
    if msg["type"] == "update_user_nationality":
        print("Hello nationality")
        args = msg["args"]
        update_user_nationality(username=args["username"],
                                nationality=args["nationality"],
                                dbName=dbName)
    if msg["type"] == "update_user_age":
        print("Hello age")
        args = msg["args"]
        update_user_age(username=args["username"],
                        age=args["age"],
                        dbName=dbName)
    if msg["type"] == "add_follower":
        args = msg["args"]
        add_follower(username=args["username"],
                    follower=args["follower"],
                    dbName=dbName)
    if msg["type"] == "remove_follower":
        args = msg["args"]
        remove_follower(username=args["username"],
                        follower=args["follower"],
                        dbName=dbName)
    if msg["type"] == "add_post":
        args = msg["args"]
        add_post(author=args["author"],
                content=args["content"],
                likes=args["likes"],
                dbName=dbName)
    if msg["type"] == "change_post_content":
        args = msg["args"]
        change_post_content(postid=args["postid"],
                            content=args["content"],
                            dbName=dbName)
    if msg["type"] == "add_post_likes":
        args = msg["args"]
        add_post_likes(postid=args["postid"],
                        username=args["username"],
                        dbName=dbName)
    if msg["type"] == "reduce_post_likes":
        args = msg["args"]
        reduce_post_likes(postid=args["postid"],
                        username=args["username"],
                        dbName=dbName)
    if msg["type"] == "deletePost":
        args = msg["args"]
        deletePost(postid=args["postid"],
                    dbName=dbName)


if __name__ == "__main__":
    
    deleteDatabase(dbName=dbName)
    deleteDatabase(dbName='CRDT-DisCS_Test')
    # print(listDatabases())

    # parsemessage(msg, dbName=dbName)
    
    # users = readUsers(dbName=dbName)
    
    # print_users(users)

    # print(listDatabases())

    
    # print(listDatabases())

    from client import put, get
    
    # mongoengine.register_connection(alias='core', name=dbName)
    start = time.perf_counter()
    
    addr = "http://127.0.0.1:500" + str(random.randint(0, 2))
    print("Current Address : ", addr)
    key = 'my_msg'
    value = msg
    put(addr, key, value)
    addr = "http://127.0.0.1:500" + str(random.randint(0, 2))
    print("Recieving Address : ", addr)
    recv_msg = get(addr, key)
    # print('Recieved message : ',recv_msg)

    print("Num of Users : ", len(readUsers()))

    parsable_message = recv_msg['payload']['value']
    parseMessage(parsable_message, dbName=None)
    users = readUsers()
    print("Num of Users : ", len(users))
    print("----------------Users----------------- ")
    print_users(users)
    
    finish = time.perf_counter()
    print(f'\n\n\nFinished in {round(finish-start, 3)} seconds')

    mongoengine.disconnect(alias='core')

    deleteDatabase(dbName=dbName)
    # https://www.pluralsight.com/guides/web-scraping-with-request-python