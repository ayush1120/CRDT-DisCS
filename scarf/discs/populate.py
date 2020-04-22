import sys
import os
import random
import datetime
sys.path.append('../')


from faker import Faker

from discs.data.underlying.posts import Post
from discs.data.underlying.users import User

MAX_USERS = 10
MIN_USERS = 2
MAX_POSTS_PER_USER = 5
MIN_POSTS_PER_USER = 1

FAKE_START_TIME = datetime.datetime(2019, 1, 1, 1, 1, 1)
FAKE_END_TIME = datetime.datetime(2020, 4, 20, 23,59,59)


NATIONALITIES = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans and Barbudan', 'Argentine', 'Armenian', 'Aruban', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Basque', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bermudian', 'Bhutanese', 'Bolivian', 'Bosniak', 'Bosnians and Herzegovinian', 'Botswana', 'Brazilian', 'Breton', 'British', 'British Virgin Islander', 'Bruneian', 'Bulgarian', 'Macedonian Bulgarian', 'Burkinabé', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Catalan', 'Cape Verdean', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comorian', 'Congolese (DRC)', 'Congolese (RotC)', 'Costa Rican', 'Croat', 'Cuban', 'Cypriot', 'Czech', 'Dane', 'Greenlander', 'Djiboutian', 'Dominicans (Commonwealth)', 'Dominicans (Republic)', 'Dutch', 'East Timorese', 'Ecuadorian', 'Egyptian', 'Emirati', 'English', 'Equatoguinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Falkland Islander', 'Faroese', 'Fijian', 'Finn', 'Finnish Swedish', 'Filipino', 'French citizen', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Baltic German', 'Ghanaian', 'Gibraltarian', 'Greek', 'Greek Macedonian', 'Grenadian', 'Guatemalan', 'Guianese (French)', 'Guinean', 'Guinea-Bissau national', 'Guyanese', 'Haitian', 'Honduran', 'Hong Konger', 'Hungarian', 'Icelander', 'I-Kiribati', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivoirian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakh', 'Kenyan', 'Korean', 'Kosovar', 'Kuwaiti', 'Kyrgyz', 'Lao', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macao', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivian', 'Malian', 'Maltese', 'Manx', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monégasque', 'Mongolian', 'Montenegrin', 'Moroccan', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'New Zealander', 'Nicaraguan', 'Nigerien', 'Nigerian', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Palestinian', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Pole', 'Portuguese', 'Puerto Rican', 'Qatari', 'Quebecer', 'Réunionnai', 'Romanian', 'Russian', 'Baltic Russian', 'Rwandan', 'Saint Kitts and Nevi', 'Saint Lucian', 'Salvadoran', 'Sammarinese', 'Samoan', 'São Tomé and Príncipe', 'Saudi', 'Scot', 'Senegalese', 'Serb', 'Seychelloi', 'Sierra Leonean', 'Singaporean', 'Slovak', 'Slovene', 'Solomon Islander', 'Somali', 'Somalilander', 'Sotho', 'South African', 'Spaniard', 'Sri Lankan', 'Sudanese', 'Surinamese', 'Swazi', 'Swede', 'Swis', 'Syriac', 'Syrian', 'Taiwanese', 'Tamil', 'Tajik', 'Tanzanian', 'Thai', 'Tibetan', 'Tobagonian', 'Togolese', 'Tongan', 'Trinidadian', 'Tunisian', 'Turk', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbek', 'Vanuatuan', 'Venezuelan', 'Vietnamese', 'Vincentian', 'Welsh', 'Yemeni', 'Zambian', 'Zimbabwean']


fake = Faker()


def get_fake_user():
    name = fake.name()
    age = random.randint(4, 75)
    nationality = NATIONALITIES[random.randint(0, len(NATIONALITIES))]
    return [name, age, nationality ]

def get_fake_post():
    """
    Returns: Post Object with fake data
    """
    time = fake.date_time_between_dates(datetime_start=FAKE_START_TIME, datetime_end=FAKE_END_TIME)
    content = fake.paragraph(nb_sentences=5)
    post = Post(content=content, creation_time=time)
    return post

if __name__ == "__main__":
    post = get_fake_post()
    print("Creation Time : ", post.creation_time)
    print("Content : ", post.content)


