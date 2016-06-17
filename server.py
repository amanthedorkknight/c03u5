import socket
import sys

# Create socket
def socket_create():
    try:
        global host
        global port
        global s

        host = '' # Leave blank for own machine
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error : " + str(msg))

# Bind socket to port and wait for client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port : " + str(port))
        s.bind(host, port)
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error : " + str(msg))
        time.sleep()
        socket_bind()


