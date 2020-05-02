import sys, requests
sys.path.append('../../')


from crdt.server.config import NUM_SERVERS


def hello(server_address, message):      
    try:
        response = requests.get(server_address, json=message ,timeout=1)
    except Exception as e:
        return e
    
    # if valid response
    if response.status_code == 200:
        pass
    else:
        return f'Sad, response.status_code : {response.status_code}'
        
    # if type == "get":
    return response.json()

def shutdown_server(server_address):
    try:
        response = requests.get(server_address, timeout=1)
    except Exception as e:
        return e
    return 'Server Closed'

def try_internal_comm(server_address, message):
    try:
        response = requests.get(server_address, json=message ,timeout=5)
    except Exception as e:
        return e
    return response.json



if __name__ == "__main__":
    server_index = 1
    print('Selected Server Index : ', server_index)
    message = {
        'type': 'request_data',
        'data_type' : 'Users_update'
    }
    flag=1

    

    while (True):
        server_address = "http://0.0.0.0:600" + str(server_index) +"/"
        
        print('\nSelected Server Index : ', server_index)
        print('\ne to change Server Index')
        print('r to run hello')
        print('p to test async requests')
        print('q to shutdown selected server')
        print('z to shutdown all the servers\n')
        a = input('Enter Operation: ')
        if a == 'q':
            output = shutdown_server(server_address+'stopServer')
            print(output)

        elif a=='r':
            output = hello(server_address+'sendRequest', message)
            print(output)

        elif a=='e':
            server_index = int(input('Enter Server Index : '))
            if (server_index<0 or server_index>NUM_SERVERS):
                print('Wrong Serber Index Provided. Please Check config.')
                server_index = 1

        elif a=='p':
            server_address = server_address + 'testSending'
            output = try_internal_comm(server_address, 'hello')
            print(output)
        
        elif a=='z':
            for i in range(1,NUM_SERVERS+1):
                server_index = i
                print(f'Quitting Server {i}')
                server_address = "http://0.0.0.0:600" + str(server_index) +"/"
                output = shutdown_server(server_address+'stopServer')
                print(output)
            
            print('All servers have been shut down.')
            break
            



