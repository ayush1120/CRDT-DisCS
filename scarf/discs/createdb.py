# from pymongo import MongoClient

# #Creating a pymongo client
# client = MongoClient('localhost', 27017)

# #Getting the database instance
# db = client['mydb']
# print("Database created........")

# #Verification
# print("List of databases after creating new one")
# print(client.list_database_names())

import pymongo
from pymongo import MongoClient
# client = MongoClient('localhost', 54321)
mongo_client = MongoClient('mongodb://localhost:27017')
# database_list = mongo_client.database_names()
# print ("database_list:", database_list)
print (mongo_client)
db = mongo_client["lol_database"]
# db.clients.count()
# clients = db.clients
# clients.find()

def main():

    while(1):
    # chossing option to do CRUD operations
        selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')
    
        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        else:
            print ('\n INVALID SELECTION \n')

# Function to insert data into mongo db
def insert():
    try:
        UserId = input('Enter User id :')
        Name = input('Enter Name :')
        Age = input('Enter age :')
        Nationality =input('Enter Nationality :')
        
        db.User.insert_one(
            {
                "id": UserId,
                "name":Name,
                "age":Age,
                "nationality":Nationality
        })
        print ('\nInserted data successfully\n')
    
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
