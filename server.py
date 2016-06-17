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
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error : " + str(msg) + '\n' + "Retrying...")
        socket_bind()


# Establish connection with client
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()


# Sends commands to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(20480), "utf-8")
            print(client_response, end='')


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()

