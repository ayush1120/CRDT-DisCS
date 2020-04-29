import sys
sys.path.append('../')

from discs.data.middleware.users_update import Users_update
from discs.data.middleware.posts_updates import Posts_update
from discs.data.middleware.age_update import Age_update
from discs.data.middleware.post_content_updates import Post_content_update
from discs.data.middleware.likedposts_updates import LikedPosts_update
from discs.data.middleware.fullname_update import Fullname_update
from discs.data.middleware.nationality_update import Nationality_update
from discs.data.middleware.followers_update import Followers_update


from discs.services.underlying import databaseWrite as underlyingDatabaseWrite
from discs.services.underlying import databaseRead as underlyingDatabaseRead
from discs.services.middleware import databaseWrite as middlewareDatabaseWrite
from discs.services.middleware import databaseRead as middlewareDatabaseRead

def update_underlying_from_middleware(dbIndex, **kwargs):
    underlyingDatabase = underlyingDatabaseName(dbIndex)
    middlewareDatabase = middlewareDatabaseName(dbIndex)
    new_users = middlewareDatabaseRead.update_user()
    if new_users is not None:
        users = new_users.users

        underlyingDatabaseWrite.add_user_by_object(new_user, **kwargs)

# def update