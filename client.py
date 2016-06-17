import os
import socket
import subprocess


# Create socket
def socket_create():
    try:
        global host
        global port
        global s
        host = '192.168.43.153' # Server ip
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error : " + str(msg))


# Connect to a remote socket
def socket_connect():
    try:
        global host
        global port
        global s
        s.connect((host, port))
    except socket.error as msg:
        print("Socket connection error: " + str(msg))
