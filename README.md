# c03u5

Overview
--------
This is a reverse shell writen in Python 3.x
It works with multiple clients and employs multiple threads.

The shell should only be used for accessing remote systems where you have proper authorisation. Make sure you aren't tresspassing.

Usage
-----

You need to run the client and server scripts on different machines. Once both are running you can access the client machine through the server script. 

Make sure that the server script is already running when the client script is executed. 

You will have to change the ip address in the client.py file to that of the server machine. 

### Server

To set up server script, simply run **server.py** using Python 3.4

`python3 server.py`

You will then enter an interactive prompt where you are able to view connected clients, select a specific client, and send commands to that client remotely.

To list all current connections:

`turtle> list`

To select a target from the list of clients:

`turtle> select 3`


### Client

In **client.py**, first change the IP address to that of the server and then run on target machine.

***

_Currently working on making the client.py an executable file for supporting target machines without python set up. Feel free to contribute._
