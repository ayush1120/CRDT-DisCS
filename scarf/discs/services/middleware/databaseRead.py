import sys
sys.path.append('../../../')

from discs.data.middleware.users_update import Users_update
from discs.data.middleware.fullname_update import Fullname_update
from discs.data.middleware.nationality_update import Nationality_update
from discs.data.middleware.age_update import Age_update
from discs.data.middleware.followers_update import Followers_update
from discs.data.middleware.posts_updates import Posts_update
from discs.data.middleware.likedposts_updates import LikedPosts_update
from discs.data.middleware.post_content_updates import Post_content_update

from discs.settings import connect_with_middleware_database

@connect_with_middleware_database
def get_user_updates(**kwargs):
    users_updates =  Users_update.objects()
    if len(users_updates) == 0:
        return None
    else:
        return users_updates[0]

        
@connect_with_middleware_database
def get_age_updates(**kwargs):
    age_updates = Age_update.objects()
    if len(age_updates == 0):
        return None
    else:
        return age_updates


@connect_with_middleware_database
def get_age_updates_by_user(username, **kwargs):
    age_updates = Age_update.objects(user_name=username)
    if len(age_updates==0):
        return None
    else:
        return age_updates

@connect_with_middleware_database
def get_posts_updates(**kwargs):
    post_updates = Posts_update.objects()
    if len(post_updates == 0):
        return None
    else:
        return post_updates
        

@connect_with_middleware_database
def get_posts_updates_by_user(username, **kwargs):
    post_updates = Posts_update.objects(username=username)
    if len(post_updates == 0):
        return None
    else:
        return post_updates

@connect_with_middleware_database
def get_nationality_updates(**kwargs):
    nationality_updates = Nationality_update.objects()
    if len(nationality_updates == 0):
        return None
    else:
        return nationality_updates


@connect_with_middleware_database
def get_nationality_updates_by_User(username, **kwargs):
    nationality_updates = Nationality_update.objects(user_name=username)
    if len(nationality_updates == 0):
        return None
    else:
        return nationality_updates


@connect_with_middleware_database
def get_post_content_updates(**kwargs):
    post_content_updates = Post_content_update.objects()
    if len(post_content_updates == 0):
        return None
    else:
        return post_content_updates


@connect_with_middleware_database
def get_post_content_updates_by_post_id(post_id, **kwargs):
    post_content_updates = Post_content_update.objects(post_id=post_id)
    if len(post_content_updates == 0):
        return None
    else:
        return post_content_updates    


@connect_with_middleware_database
def get_fullname_updates(**kwargs):
    fullname_updates = Fullname_update.objects()
    if len(fullname_updates == 0):
        return None
    else:
        return fullname_updates


@connect_with_middleware_database
def get_fullname_updates_by_username(username, **kwargs):
    fullname_updates = Fullname_update.objects(user_name=username)
    if len(fullname_updates == 0):
        return None
    else:
        return fullname_updates


@connect_with_middleware_database
def get_follower_updates(**kwargs):
    followers_updates = Followers_update.objects()
    if len(followers_updates == 0):
        return None
    else:
        return followers_updates
        

@connect_with_middleware_database
def get_follower_updates_by_username(username, **kwargs):
    followers_updates = Followers_update.objects(username)
    if len(followers_updates == 0):
        return None
    else:
        return followers_updates


@connect_with_middleware_database
def get_liked_posts_updates(**kwargs):
    liked_post_updates = LikedPosts_update.objects()
    if len(liked_post_updates == 0):
        return None
    else:
        return liked_post_updates


@connect_with_middleware_database
def get_liked_posts_updates_by_username(username, **kwargs):
    liked_post_updates = LikedPosts_update.objects(username=username)
    if len(liked_post_updates == 0):
        return None
    else:
        return liked_post_updates
    






