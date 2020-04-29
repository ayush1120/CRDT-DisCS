import sys, requests



def hello(server_address):
        
    try:
        response = requests.get(server_address, timeout=1)
    except Exception as e:
        return e
    
    # if valid response
    if response.status_code == 200:
        pass
    else:
        return f'Sad, response.status_code : {response.status_code}'
        
    # if type == "get":
    return response.json()

if __name__ == "__main__":
    server_address = "http://127.0.0.1:6000"+"/"
    output = hello(server_address)
    print(output)
