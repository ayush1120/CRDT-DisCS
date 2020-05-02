# [CRDT-DisCS](https://github.com/ayush1120/CRDT-DisCS)
### A CRDT Based Distributed Consensus System
To Learn more visit [this link](https://docs.google.com/document/d/1VCTHx3wVX6Us8y8xRrRbpZXsHLyIKg_P1zGGLV11iZw).

## Installation Instruction
**Please Make Sure mongoDB is installed and working correctly.**
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

Initialize Database & Update Migrations
```sh
$ python initialize_database.py
```
**This Initilizes databases with random data, all databases have different data, can be viewed using website interface**

#### To Run CRDT Server Nodes
```sh
$ cd python <path to repo>/scarf/crdt/server/run_crdt_servers.py
```
*This step clears the databases and after the flasks servers are started now the consensus will be achieved for the updates, called with functions from <ProjectDIR>/scarf/discs/updateDatabases.py*

**Note: Currently CRDT_UPDATE is marked as true, make it false to stop using CRDTs for consensus. RAFT_UPDATE variable will we used in future to achive consensus using RAFT, paxos based protocol**

#### To Run the terminal interface to interact with a single node:
**Note: CRDT Server Nodes should be started & running in a separate terminal beforehand.**
```sh
$ cd python <path to repo>/scarf/terminal/interface.py
```

## To test the raft based consensus
Currently under development, you can see proof of work by running the following files as :
```sh
$ run the servers 
```

#### To Run the Web Interface

Start the django server in development mode via command
```sh
$ python manage.py runserver
```
Visit http://localhost:8000/ in your browser to see the web interface. 

Deactivate the virtual environment by command
```sh
$ deactivate
```