import sys
sys.path.append('../../../')

import mongoengine
import datetime
import pymongo
import json
from discs.data.middleware.users_update import Users_update
from discs.data.middleware.fullname_update import Fullname_update
from discs.data.middleware.nationality_update import Nationality_update
from discs.data.middleware.age_update import Age_update
from discs.data.middleware.followers_update import Followers_update
from discs.data.middleware.posts_updates import Posts_update
from discs.data.middleware.likedposts_updates import LikedPosts_update
from discs.data.middleware.post_content_updates import Post_content_update
from discs.crdt.CRDT.src.gset import GSet
from discs.crdt.CRDT.src.lww import LWWElementSet
from discs.crdt.CRDT.src.twopset import TwoPSet

# from discs.data.underlying.posts import Post
from discs.settings import connect_with_middleware_database

@connect_with_middleware_database
def check_users():
    user_updates = Users_update.objects().first()
    if user_updates is None:
        user_update = Users_update()
        user_updates_GSet = GSet()
        user_update.users = json.dumps(user_updates_GSet.__dict__)
        user_update.save()

@connect_with_middleware_database
def update_user(user, **kwargs):
    """
    Function to add user update (i.e. addition of user to middleware database) 
    """
    check_users_updates()   # checks whether any user exists in that collection
    user_updates=Users_update.objects().first()
    
    user_updates_GSet_dict = json.loads(user_updates.users)
    user_updates_GSet = GSet()
    user_updates_GSet.__dict__ = user_updates_GSet_dict

    user_updates_GSet.add(user)
    user_updates.users = json.dumps(user_updates_GSet.__dict__)
    user_updates.save()

@connect_with_middleware_database
def update_user_fullname(username, fullname, **kwargs):
    """
    Args:
    

    """
    user_fullname_updates = Fullname_update.objects(user_name=username).first()
    if user_fullname_updates is None:
        user_fullname_updates_lww = LWWElementSet()
        user_fullname_updates = Fullname_update()
        user_fullname_updates.user_name = username
        user_fullname_updates.update = json.dumps(user_fullname_updates_lww.__dict__)
        # user_fullname_updates.save()

    user_fullname_updates_lww_dict = json.loads(user_fullname_updates.update)
    user_fullname_updates_lww = LWWElementSet()
    user_fullname_updates_lww.__dict__ = user_fullname_updates_lww_dict

    user_fullname_updates_lww.add(fullname)
    user_fullname_updates.update = json.dumps(user_fullname_updates_lww.__dict__)
    user_fullname_updates.save()

@connect_with_middleware_database
def update_user_nationality(username, nationality, **kwargs):
    """
    Args:
    

    """
    user_nationality_updates = Nationality_update.objects(user_name=username).first()
    if user_nationality_updates is None:
        user_nationality_updates_lww = LWWElementSet()
        user_nationality_updates = Nationality_update()
        user_nationality_updates.user_name = username
        user_nationality_updates.update = json.dumps(user_nationality_updates_lww.__dict__)
        # user_nationality_updates.save()

    user_nationality_updates_lww_dict = json.loads(user_nationality_updates.update)
    user_nationality_updates_lww = LWWElementSet()
    user_nationality_updates_lww.__dict__ = user_nationality_updates_lww_dict

    user_nationality_updates_lww.add(nationality)
    user_nationality_updates.update = json.dumps(user_nationality_updates_lww.__dict__)
    user_nationality_updates.save()

@connect_with_middleware_database
def update_user_age(username, age, **kwargs):
    """
    Args:
    

    """
    user_age_updates = Age_update.objects(user_name=username).first()
    if user_age_updates is None:
        user_age_updates_lww = LWWElementSet()
        user_age_updates = Age_update()
        user_age_updates.user_name = username
        user_age_updates.update = json.dumps(user_age_updates_lww.__dict__)
        # user_age_updates.save()

    user_age_updates_lww_dict = json.loads(user_age_updates.update)
    user_age_updates_lww = LWWElementSet()
    user_age_updates_lww.__dict__ = user_age_updates_lww_dict

    user_age_updates_lww.add(age)
    user_age_updates.update = json.dumps(user_age_updates_lww.__dict__)
    user_age_updates.save()

@connect_with_middleware_database
def update_user_followers(username, follower_name, **kwargs):
    """
    user_name : this user who is being followed
    follower_name : username of the person who is clicking the follow button to follow the user with username in first argument
    """

    user_followers_updates = Followers_update.objects(user_name=username).first()
    if user_followers_updates is None:
        user_followers_updates_twopset = TwoPSet()
        user_followers_updates = Followers_update()
        user_followers_updates.user_name = username
        user_followers_updates.update = json.dumps(user_followers_updates_twopset.__dict__)
        # user_followers_updates.save()

    user_followers_updates_twopset_dict = json.loads(user_followers_updates.update)
    user_followers_updates_twopset = TwoPSet()
    user_followers_updates_twopset.__dict__ = user_followers_updates_twopset_dict

    user_followers_updates_twopset.add(follower_name)
    user_followers_updates.update = json.dumps(user_followers_updates_twopset.__dict__)
    user_followers_updates.save()


@connect_with_middleware_database
def remove_user_follower(username, follower_name, **kwargs):
    """
    user_name : this user is clicking the unfollow button to follow the user with username in second argument
    follower_name : username of the person to be unfollowed   
    """

    user_followers_updates = Followers_update.objects(user_name=username).first()
    if user_followers_updates is None:
        user_followers_updates_twopset = TwoPSet()
        user_followers_updates = Followers_update()
        user_followers_updates.user_name = username
        user_followers_updates.update = json.dumps(user_followers_updates_twopset.__dict__)
        # user_followers_updates.save()

    user_followers_updates_twopset_dict = json.loads(user_followers_updates.update)
    user_followers_updates_twopset = TwoPSet()
    user_followers_updates_twopset.__dict__ = user_followers_updates_twopset_dict

    user_followers_updates_twopset.remove(follower_name)
    user_followers_updates.update = json.dumps(user_followers_updates_twopset.__dict__)
    user_followers_updates.save()


@connect_with_middleware_database
def add_post(username, post, **kwargs):
    post_updates = Posts_update.objects(user_name=username).first()
    if post_updates is None:
        post_updates_twopset = TwoPSet()
        post_updates = Posts_update()
        post_updates.user_name = username
        post_updates.update = json.dumps(post_updates_twopset.__dict__)
        # post_updates.save()

    post_updates_twopset_dict = json.loads(post_updates.update)
    post_updates_twopset = TwoPSet()
    post_updates_twopset.__dict__ = post_updates_twopset_dict

    post_updates_twopset.add(post)
    post_updates.update = json.dumps(post_updates_twopset.__dict__)
    post_updates.save()

@connect_with_middleware_database
def remove_post(username, post, **kwargs):
    post_updates = Posts_update.objects(user_name=username).first()
    if post_updates is None:
        post_updates_twopset = TwoPSet()
        post_updates = Posts_update()
        post_updates.user_name = username
        post_updates.update = json.dumps(post_updates_twopset.__dict__)
        # post_updates.save()

    post_updates_twopset_dict = json.loads(post_updates.update)
    post_updates_twopset = TwoPSet()
    post_updates_twopset.__dict__ = post_updates_twopset_dict

    post_updates_twopset.remove(post)
    post_updates.update = json.dumps(post_updates_twopset.__dict__)
    post_updates.save()


@connect_with_middleware_database
def add_liked_post(username, liked_post, **kwargs):
    liked_post_updates = LikedPosts_update.objects(user_name=username).first()
    if liked_post_updates is None:
        liked_post_updates_twopset = TwoPSet()
        liked_post_updates = LikedPosts_update()
        liked_post_updates.user_name = username
        liked_post_updates.update = json.dumps(liked_post_updates_twopset.__dict__)
        # liked_post_updates.save()

    liked_post_updates_twopset_dict = json.loads(liked_post_updates.update)
    liked_post_updates_twopset = TwoPSet()
    liked_post_updates_twopset.__dict__ = liked_post_updates_twopset_dict

    liked_post_updates_twopset.add(liked_post)
    liked_post_updates.update = json.dumps(liked_post_updates_twopset.__dict__)
    liked_post_updates.save()

@connect_with_middleware_database
def remove_liked_post(username, liked_post, **kwargs):
    liked_post_updates = LikedPosts_update.objects(user_name=username).first()
    if liked_post_updates is None:
        liked_post_updates_twopset = TwoPSet()
        liked_post_updates = LikedPosts_update()
        liked_post_updates.user_name = username
        liked_post_updates.update = json.dumps(liked_post_updates_twopset.__dict__)
        # liked_post_updates.save()

    liked_post_updates_twopset_dict = json.loads(liked_post_updates.update)
    liked_post_updates_twopset = TwoPSet()
    liked_post_updates_twopset.__dict__ = liked_post_updates_twopset_dict

    liked_post_updates_twopset.remove(liked_post)
    liked_post_updates.update = json.dumps(liked_post_updates_twopset.__dict__)
    liked_post_updates.save()

@connect_with_middleware_database
def update_post_content(username, post_content, **kwargs):
    post_content_updates = Post_content_update.objects(user_name=username).first()
    if post_content_updates is None:
        post_content_updates_twopset = TwoPSet()
        post_content_updates = Post_content_update()
        post_content_updates.user_name = username
        post_content_updates.update = json.dumps(post_content_updates_twopset.__dict__)
        # post_content_updates.save()

    post_content_updates_twopset_dict = json.loads(post_content_updates.update)
    post_content_updates_twopset = TwoPSet()
    post_content_updates_twopset.__dict__ = post_content_updates_twopset_dict

    post_content_updates_twopset.add(post_content)
    post_content_updates.update = json.dumps(post_content_updates_twopset.__dict__)
    post_content_updates.save()