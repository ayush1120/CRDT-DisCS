#  Get update (content & type) & save it in middleware database.

import sys
sys.path.append('..')

import json
import os

from crdt.gset import GSet


def validate_middleware(middlewareName):
    middlewarePath = middlewareName + '.json'
    # Initialize middleware if doesn't exist
    if not os.path.exists(middlewarePath):
        with open(middlewarePath, 'w+') as mp:
            json.dump({'Users': GSet().toDict()} , mp)

def print_middleware(middlewareName):
    validate_middleware(middlewareName)
    middlewarePath = middlewareName + '.json'
    with open(middlewarePath) as mp:
        middlewareData = json.load(mp)
    print('middlewareData : ', middlewareData)
        

def load_middleware(middlewareName):
    middlewarePath = middlewareName + '.json'
    validate_middleware(middlewareName)

    with open(middlewarePath) as mp:
        middlewareData = json.load(mp)
        
    return middlewareData 


def save_middleware(data, middlewareName):
    validate_middleware(middlewareName)
    middlewarePath = middlewareName + '.json'
    
    with open(middlewarePath,'w+') as mp:
        json.dump(data, mp)
    


def addUsers(user, dbName, middlewareName):  
    middlewareData = load_middleware(middlewareName)
    data = GSet.loadFromDict(middlewareData['Users'])  # type(middlewareData['Users']) : GSet
    data.add(user)
    middlewareData['Users'] = data.toDict()
    save_middleware(middlewareData, middlewareName)

def mergeUsers(middlewareName1, middlewareName2):
    middlewareData1 = load_middleware(middlewareName1)
    middlewareData2 = load_middleware(middlewareName2)
    data1 = GSet.loadFromDict(middlewareData1['Users'])
    data2 = GSet.loadFromDict(middlewareData2['Users'])
    data1.merge(data2)
    mergedList = data1.toDict()
    middlewareData1['Users'] = mergedList
    save_middleware(middlewareData1, middlewareName1)
    save_middleware(middlewareData1, middlewareName2)

if __name__ == "__main__":
    User1 = {
        'Name' : 'Ayush',
        'Nationality' : "Belgian",
        'Age' : 72
    }

    User2 = {
        'Name' : 'Saptarshi',
        'Nationality' : "Greek",
        'Age' : 48
    }

    User3 = {
        'Name' : 'Robert',
        'Nationality' : "English",
        'Age' : 25
    }

    User4 = {
        'Name' : 'Stafford',
        'Nationality' : "American",
        'Age' : 41
    }

    
    print_middleware('test')
    addUsers(User1, 'lol', 'test')
    print_middleware('test')
    addUsers(User2, 'lol', 'test')
    print_middleware('test')

    print_middleware('test1')
    addUsers(User3, 'lol1', 'test1')
    print_middleware('test1')
    addUsers(User4, 'lol1', 'test1')    
    print_middleware('test1')             

    mergeUsers('test', 'test1')
    
"""
class Users():
    users = GSet()

    def merge():


class User():
    age = LWW()
    Nationality = LWW()
    friends = TwoPSet()

    def merge(self, User2):
        if self.age!=User2.age:
            self.age = self.age.merge(User2.age)
        self.Nationality = self.Nationality.merge(User2.Nationality)
        self.friends = self.friends.merge(User2.friends)

{
    f'Users__{ayush}__nationality' : LWW(),
    f'Users__{ayush}__age' : LWW(),
    'ayush_id' : ayush


}
"""