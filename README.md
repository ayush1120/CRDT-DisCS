# CRDT-Discs
### A CRDT Based Distributed Consensus System
To Learn more visit [this link](https://docs.google.com/document/d/1VCTHx3wVX6Us8y8xRrRbpZXsHLyIKg_P1zGGLV11iZw).

## Installation Instruction

### Cloning Repository 
Clone the Github Repository.

### Installing Requirements
Install Virtualenv
```sh
$ pip3 install virtualenv
```
Find your Python3 Path 
```python
import sys
print(sys.executable)
```
Example Output
> /usr/bin/python3

Run setup.sh with first argument **as path to repository** and second argument as **python3 path**
Example Command:
```sh
$ ./setup.sh  /home/user/CRDT-DisCS  /usr/bin/python3 
```
The setup.sh script will create envCRDT-DisCS environment inside Project Directory and install all the requirements. ( For UNIX based systems only )

### Running Project
Activate the virtual environment by command
```sh
$ source <path to repo>/envCRDT-DisCS/bin/activate
```
Change Directory to <repository>/scarf
```sh
$ cd <path to repo>/scarf
```

Start the django server in development mode vi command
```sh
$ python manage.py runserver
```
Visit http://localhost:8000/ in your browser to see the web interface. 
