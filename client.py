#CLIENT SIDE

import socket

HOST = input('Ip address: ')
PORT = 7000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print('Write \"exit\" to get out.\n')
msg = input('Tap an message: ')

while msg != 'exit':
    client_socket.send(msg.encode())
    msg = client_socket.recv(1024)
    print('\nAnswer: {}\n'.format(msg.decode()))
    msg = input('Tap an message: ')
client_socket.close()
