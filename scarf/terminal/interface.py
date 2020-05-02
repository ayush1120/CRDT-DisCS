import sys
import os
import time
# import msvcrt
sys.path.append('../')

import mongoengine
import datetime
import pymongo
import json


from discs import manageDatabases
from discs import updateDatabases 
from discs import populate


from discs.services.underlying import databaseRead as underlyingDatabaseRead
from discs.services.underlying import databaseWrite as underlyingDatabaseWrite



screen = 'dashboard'

def make_connection(index):
    mongoengine.disconnect_all()
    dbName = 'CRDT-DisCS_Node_Core_' + str(index)
    middlewareDBName = 'CRDT-DisCS_Node_Middleware_' + str(index)
    mongoengine.register_connection(alias='core', name=dbName)
    mongoengine.register_connection(alias='middle', name=middlewareDBName)


def get_usernames():
    users = underlyingDatabaseRead.readUsers()
    usernames = []
    for user in users:
        usernames.append(user.username)
    
    return usernames

def print_connection():
    global serverNodeIndex
    dbName = 'CRDT-DisCS_Node_Core_' + str(serverNodeIndex)
    middlewareDBName = 'CRDT-DisCS_Node_Middleware_' + str(serverNodeIndex)
    print(f'Connected to {dbName}....')
    print(f'Connected to {middlewareDBName}....\n\n')



def dashboard():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_connection()
    print('0. Change Server Node')
    print('1. Hello')
    print('2. Login')
    print('3. Add User')
    print('4. Show all Users')
    print('5. Show all Posts')
    # print('6. Edit user')
    # print('7. Edit post')

    a = int(input('Press number to continue: '))
    screen = run_dashboard_choices(a)
    return screen


def run_dashboard_choices(a):

    screen = 'dashboard'
    if a == 0:
        b = int(input('\nEnter the server node index : '))
        if b>0 and b<=4:
            global serverNodeIndex
            serverNodeIndex = b
            if b!=a:
                make_connection(b)

    elif a == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Helloooo!!')
        time.sleep(1)
        screen = 'dashboard'
    elif a == 2:
        screen = 'login_dashboard'
        time.sleep(1)
        screen = login_dashboard()
    elif a == 3:
        screen = 'add_user_dashboard'
        time.sleep(1)
        screen = add_user_dashboard()
    elif a == 4:
        screen = 'show_all_user_dashboard'
        time.sleep(1)
        show_all_user_dashboard()
    elif a == 5:
        screen = 'show_all_post_dashboard'
        time.sleep(1)
        screen = show_all_post_dashboard()
    # elif a == 6:
    #     screen = 'edit_user'
    #     time.sleep(1)
    #     screen = edit_user()
    # elif a == 7:
    #     screen = 'show_all_post_dashboard'
    #     time.sleep(1)
    #     screen = show_all_post_dashboard()
    elif a >= 6:
        screen = 'exit'
    return screen


def pause():
    print('\n Press Enter to continue...\n')
    a = input()


def login_dashboard():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Showing All Users..... \n\n')
    print(get_usernames(), '\n\n')


    print("Enter 0 to go back to dashboard.")
    username = input("Enter Username to LogIn :")
    
    if underlyingDatabaseRead.check_user(username):
        user = underlyingDatabaseRead.get_user_by_username(username)
        screen = logged_in_dashboard(user)
    elif username=="0":
        return 'dashboard'

    else:
        print("Sadly, you entered a wrong username :( ")
        pause()
        screen = 'dashboard'

    return screen

def logged_in_dashboard(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{user.username}, Logged In\n\n')
    print('1. See my profile details')
    print('2. See my posts')
    print('3. Follow a user')
    print('4. See my followers')
    print('5. Like a post')
    print('6. Edit User Details')
    print('7. Edit User Post Details')

    
    print('8. logout')

    screen = login_choices_user(user)
    return screen



def login_choices_user(user):
    username = user.username
    a = int(input('Press number to continue: '))
    screen = 'login_dashboard'
    if a == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('My Profile details')
        user = underlyingDatabaseRead.get_user_by_username(username)
        underlyingDatabaseRead.print_user(user)
        time.sleep(5)
        
    elif a == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('My Posts')
        post_ids = underlyingDatabaseRead.get_posts_by_username(username)
        posts = [ underlyingDatabaseRead.get_post_by_id(post_id)  for post_id in post_ids ]
        if len(posts)>0:
            underlyingDatabaseRead.print_posts(posts=posts)
        else:
            print("Ohh no!! User has no post")
        pause()
    elif a == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Follow a User\n')
        # time.sleep(1)
        print(get_usernames(), '\n\n')
        follow_user = input('Type user to follow: ')
        if underlyingDatabaseRead.check_user(follow_user) and follow_user!=user.username:
            updateDatabases.add_follower(follow_user, username, serverNodeIndex=serverNodeIndex)
            print('Done! You have just followed ', follow_user)
            pause()
        else:
            print('Error')
            pause()
        
    elif a == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('These are my followers')
        # time.sleep(1)
        
        followers = underlyingDatabaseRead.get_followers_by_username(username)
        print(followers)
        pause()
        # Print followers

    elif a == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Like a post')
        # time.sleep(1)

        print('See all Posts :\n')
    
        posts = underlyingDatabaseRead.readPosts()
        if len(posts)>0:
            underlyingDatabaseRead.print_posts(posts)


        index = int(input("Enter Index of Post to like (Starting from 0) : "))
        post_id = posts[index].id

        # post_id = underlyingDatabaseRead.get_posts_by_username(username)
        # liked_post = input('Choose a post to like!! : ')
        updateDatabases.add_post_likes(post_id, username, serverNodeIndex=serverNodeIndex)

        # list of all post
        # choose a post
        # like a post function call

    elif a == 6:        #edit user
        os.system('cls' if os.name == 'nt' else 'clear')
        screen = edit_user(username)
        return screen



    elif a == 7:        #edit post
        os.system('cls' if os.name == 'nt' else 'clear')
        screen = edit_post(username)
    elif a > 7:
        screen = 'exit'
    return screen


def add_user_dashboard():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('Type "exit" and press enter to exit....\n')
    print('Add User Form')
    name = input('Full Name: ')
    if name == 'exit':
        return 'dashboard'
    
    username = input('Username: ')
    if username == 'exit':
        return 'dashboard'

    age = input('User Age: ')
    if age == 'exit':
        return 'dashboard'
    age = int(age)
    
    nationality = input('User Nationality: ')
    if nationality == 'exit':
        return 'dashboard'
    
    name = name
    age = age
    nationality = nationality

    if underlyingDatabaseRead.check_user(username):
        print('Username Alredy Exists :(')
        time.sleep(2)
        return 'dashboard'

    updateDatabases.add_user(name=name , username=username, nationality=nationality, age=age, dbIndex=None, serverNodeIndex=serverNodeIndex)
    screen = 'dashboard'
    return screen

def show_all_user_dashboard():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('See all Users')
    
    print(get_usernames(), '\n')
                                    
    a = input('Press key to continue :) ')
    time.sleep(1)
    screen = 'dashboard'
    return screen


def show_all_post_dashboard():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('See all Posts :\n')
    
    posts = underlyingDatabaseRead.readPosts()
    if len(posts)>0:
        underlyingDatabaseRead.print_post(posts)

    a = input('Press key to continue :) ')
    time.sleep(1)
    screen = 'dashboard'
    return screen


def edit_user(username):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('1. edit fullname')
    print('2. edit age')
    print('3. edit nationality')

    a = int(input('Select detail to edit: '))
    if a == 1:
        edit_name(username)
    elif a == 2:
        edit_age(username)
    elif a == 3:
        edit_nationality(username)
    elif a > 3:
        print('Oops! Check the typed number again please')
        pause()
    #show all user
    #what to edit -> class 3 age name nationality
                #   -> edit that thing
    #
    # print(get_usernames(), '\n')  #show all user
    # user = input('Select a User to Edit')
    
    screen = 'dashboard'
    return screen


def edit_name(username):
    # username = user.username
    name = input('Type new Name: ')
    updateDatabases.update_user_name(username, name, serverNodeIndex=serverNodeIndex)
    print('Fullname Updated.....')
    pause()
    

def edit_age(username):
    # username = user.username
    age = int(input('Type new Age: '))
    updateDatabases.update_user_age(username, age, serverNodeIndex=serverNodeIndex)
    print('Age Updated.....')
    pause()


def edit_nationality(username):
    # username = user.username
    nationality = input('Type new Nationality: ')
    updateDatabases.update_user_nationality(username, nationality, serverNodeIndex=serverNodeIndex)
    print('Nationality Updated.....')
    pause()


def edit_post(username):
    #author = username
    #get content
    #creation time khali
    author = username
    print('Editing post content')
    a = input('New content here: ')
    updateDatabases.add_post(author, creation_time=datetime.datetime.now, content=a, serverNodeIndex=serverNodeIndex)
    print("Post Updated ....")
    pause()
    return 'dashboard'


if __name__ == "__main__":
    
    # manageDatabases.deleteDatabase(dbName)
    # manageDatabases.deleteDatabase(middlewareDBName)


    global serverNodeIndex
    serverNodeIndex = 1
    make_connection(serverNodeIndex)


    populate.add_fake_users(3, serverNodeIndex=serverNodeIndex)
    populate.add_fake_posts(20, serverNodeIndex=serverNodeIndex)
    populate.add_random_followers(3, serverNodeIndex=serverNodeIndex)
    populate.add_random_likes(4, serverNodeIndex=serverNodeIndex)


    screen = 'dashboard'
    while (True):
        if screen == 'dashboard':
            screen = dashboard()
        elif screen == 'login_dashboard':
            screen = login_dashboard()
        elif screen == 'add_user_dashboard':
            screen = add_user_dashboard()
        elif screen == 'show_all_user_dashboard':
            screen = show_all_user_dashboard()
        elif screen == 'show_all_post_dashboard':
            screen = show_all_post_dashboard()
        elif screen == 'exit':
            break

    
    # users = underlyingDatabaseRead.readUsers()
    # underlyingDatabaseRead.print_users(users)

    
    # manageDatabases.deleteDatabase(dbName)
    # manageDatabases.deleteDatabase(middlewareDBName)