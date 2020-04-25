import mongoengine

DEBUG = True

NUM_DATABASES = 5

DATABASES_NAMES = ["CRDT-DisCS__DB"+str(i) for i in range(1, NUM_DATABASES+1)]

MIDDLEWARE_DATABASES = ["CRDT-DisCS_Middleware__DB"+str(i) for i in range(1, NUM_DATABASES+1)]

def connect_with_database(orig_func):
    global DEBUG
    def wrapper(*args, **kwargs):
        if (DEBUG==True) and 'dbName' in kwargs:
            dbName = kwargs.get('dbName')
            if dbName is not None:
                print('Connecting with database')
                mongoengine.register_connection(alias='core', name=dbName)
                results = orig_func(*args, **kwargs)
                mongoengine.disconnect(alias='core')
                return results
        
        return orig_func(*args, **kwargs)
    
    return wrapper

def connect_with_middleware_database(orig_func):
    
    def wrapper(*args, **kwargs):
        if 'dbName' in kwargs:
            dbName = kwargs.get('dbName')
            mongoengine.register_connection(alias='middle', name=dbName)
            results = orig_func(*args, **kwargs)
            mongoengine.disconnect(alias='middle')
            return results
        else:
            return orig_func(*args, **kwargs)
    
    return wrapper

