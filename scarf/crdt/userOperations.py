from gset import GSet
from twoPSet import TwoPSet

# Here index denotes the index of the CRDT-based database where we are making the change

def addUser(index,data):
    data["type"]="AddUser"
    gset[index].add(data)

def addPost(index,data):
    data["type"]="AddPost"
    twoPSet[index].add(data)

def removePost(index,data):
    data["type"]="RemovePost"
    twoPSet[index].remove(data)