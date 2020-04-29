import sys, requests


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

if __name__ == "__main__":
    server_address = "http://0.0.0.0:6000"+"/"
    message = {
        'type': 'request_data',
        'data_type' : 'Users_update'
    }
    flag=1
    while (True):
        a = input()
        if a == 'q':
            output = shutdown_server(server_address+'stopServer')

        elif a=='r':
            output = hello(server_address+'sendRequest', message)
            print(output)

        elif a=='s':
            if flag==1:
                from server import app
                app.run()
                flag=2

