import sys
import os
import random
import datetime
import math
sys.path.append('../')


from faker import Faker

from discs.data.underlying.posts import Post
from discs.data.underlying.users import User
from discs.services.underlying import databaseWrite
from discs.services.underlying import  databaseRead
from discs.settings import connect_with_database
from discs.manageDatabases import listDatabases

MAX_USERS = 10
MIN_USERS = 2
MAX_POSTS_PER_USER = 5
MIN_POSTS_PER_USER = 1

FAKE_START_TIME = datetime.datetime(2019, 1, 1, 1, 1, 1)
FAKE_END_TIME = datetime.datetime(2020, 4, 25, 23,59,59)


NATIONALITIES = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans and Barbudan', 'Argentine', 'Armenian', 'Aruban', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Basque', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bermudian', 'Bhutanese', 'Bolivian', 'Bosniak', 'Bosnians and Herzegovinian', 'Botswana', 'Brazilian', 'Breton', 'British', 'British Virgin Islander', 'Bruneian', 'Bulgarian', 'Macedonian Bulgarian', 'Burkinabé', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Catalan', 'Cape Verdean', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comorian', 'Congolese (DRC)', 'Congolese (RotC)', 'Costa Rican', 'Croat', 'Cuban', 'Cypriot', 'Czech', 'Dane', 'Greenlander', 'Djiboutian', 'Dominicans (Commonwealth)', 'Dominicans (Republic)', 'Dutch', 'East Timorese', 'Ecuadorian', 'Egyptian', 'Emirati', 'English', 'Equatoguinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Falkland Islander', 'Faroese', 'Fijian', 'Finn', 'Finnish Swedish', 'Filipino', 'French citizen', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Baltic German', 'Ghanaian', 'Gibraltarian', 'Greek', 'Greek Macedonian', 'Grenadian', 'Guatemalan', 'Guianese (French)', 'Guinean', 'Guinea-Bissau national', 'Guyanese', 'Haitian', 'Honduran', 'Hong Konger', 'Hungarian', 'Icelander', 'I-Kiribati', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivoirian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakh', 'Kenyan', 'Korean', 'Kosovar', 'Kuwaiti', 'Kyrgyz', 'Lao', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macao', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivian', 'Malian', 'Maltese', 'Manx', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monégasque', 'Mongolian', 'Montenegrin', 'Moroccan', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'New Zealander', 'Nicaraguan', 'Nigerien', 'Nigerian', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Palestinian', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Pole', 'Portuguese', 'Puerto Rican', 'Qatari', 'Quebecer', 'Réunionnai', 'Romanian', 'Russian', 'Baltic Russian', 'Rwandan', 'Saint Kitts and Nevi', 'Saint Lucian', 'Salvadoran', 'Sammarinese', 'Samoan', 'São Tomé and Príncipe', 'Saudi', 'Scot', 'Senegalese', 'Serb', 'Seychelloi', 'Sierra Leonean', 'Singaporean', 'Slovak', 'Slovene', 'Solomon Islander', 'Somali', 'Somalilander', 'Sotho', 'South African', 'Spaniard', 'Sri Lankan', 'Sudanese', 'Surinamese', 'Swazi', 'Swede', 'Swis', 'Syriac', 'Syrian', 'Taiwanese', 'Tamil', 'Tajik', 'Tanzanian', 'Thai', 'Tibetan', 'Tobagonian', 'Togolese', 'Tongan', 'Trinidadian', 'Tunisian', 'Turk', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbek', 'Vanuatuan', 'Venezuelan', 'Vietnamese', 'Vincentian', 'Welsh', 'Yemeni', 'Zambian', 'Zimbabwean']


fake = Faker()


@connect_with_database
def add_fake_users(NUM_FAKE_USERS, **kwargs):
    for _ in range(NUM_FAKE_USERS):
        user = get_fake_user()
        databaseWrite.add_user(name=user.name,
            username=user.username,
            nationality=user.nationality,
            age=user.age)


@connect_with_database
def add_fake_posts(NUM_FAKE_POSTS, **kwargs):
    users = databaseRead.readUsers()
    # post_ids = []
    if len(users) >= 1:
        for _ in range(NUM_FAKE_POSTS):
            author_index = random.randint(0, len(users)-1)
            # print('author_index : ', author_index)
            author = users[author_index] 
            post = get_fake_post()
            post.author = author.username
            post_id =  databaseWrite.add_post(
                author=post.author,
                creation_time=post.creation_time,
                content=post.content
            )
            # print('\npost_id : ', post_id)


@connect_with_database
def add_random_followers(MAX_NUM_CONNECTIONS, **kwargs):
    NUM_CONNECTIONS = MAX_NUM_CONNECTIONS
    users = databaseRead.readUsers()
    num_users = len(users)

    if int(math.sqrt(NUM_CONNECTIONS)) >= num_users - 1:   # If NUM_CONNECTIONS is greater than max num of connections possible 
        NUM_CONNECTIONS = max(0, (num_users-2)**2)  

    for _ in range(NUM_CONNECTIONS):
        
        leader_index = 0
        follower_index = 0

        while(leader_index==follower_index):
            leader_index = random.randint(0,num_users-1)
            follower_index = random.randint(0,num_users-1)

        leader = users[leader_index]
        follower = users[follower_index]
        databaseWrite.add_follower(leader.username, follower.username)


@connect_with_database
def add_random_likes(MAX_NUM_LIKES, **kwargs):
    users = databaseRead.readUsers()
    posts = databaseRead.readPosts()
    max_likes = int(len(users)*len(posts))

    if MAX_NUM_LIKES>max_likes:
        MAX_NUM_LIKES = max_likes

    num_users = len(users)
    num_posts = len(posts)

    for _ in range(MAX_NUM_LIKES):
        user_index = random.randint(0, num_users-1)
        post_index = random.randint(0, num_posts-1)
        post = posts[post_index]
        user = users[user_index]
        databaseWrite.add_post_likes(post_id=post.id, username=user.username)    



def get_fake_user():
    name = fake.name()
    age = random.randint(4, 75)
    nationality = NATIONALITIES[random.randint(0, len(NATIONALITIES)-1)]
    username = fake.user_name()
    user = User(name=name, username=username, nationality=nationality, age=age)
    # return [name, username, age, nationality ]
    return user

def get_fake_post():
    """
    Returns: Post Object with fake data
    """
    time = fake.date_time_between_dates(datetime_start=FAKE_START_TIME, datetime_end=FAKE_END_TIME)
    content = fake.paragraph(nb_sentences=5)
    post = Post(content=content, creation_time=time)
    return post


if __name__ == "__main__":
    print(listDatabases())
    dbName = 'CRDT-DisCS'


