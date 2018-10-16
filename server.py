#SERVER

import socket
import random

#APPLICATION

def request(obj):
    msg = str(obj).lower()
    greetings = ['Hi!', 'Hi', 'Hello!', 'Hello', 'Hey!', 'Hey']
    formalities = ['How are you?', 'What\'s up?', 'What\'s new?', 'How\'s it going?', 'What\'s going on?', 'What is up?', 'What is new?', 'How is it going?', 'What is going on?']
    answers = ['I\'m ok', 'I am ok', 'I\'m fine', 'I am fine', 'I\'m not bad', 'I am not bad', 'Not bad', 'I\'m great', 'Great', 'I\'m well', 'I am well']
    other = ['Good morning', 'Good afternoon', 'Good evening']
    farewell = ['Good night', 'See you later', 'See you', 'Bye bye', 'Goodbye']


    if msg in [expression.lower() for expression in greetings]:
        return random.choice(greetings)
    elif msg in [expression.lower() for expression in formalities]:
        return random.choice(answers) + '\n' + random.choice(formalities)
    elif msg == other[0].lower():
        return other[0]
    elif msg == other[1].lower():
        return other[1]
    elif msg == other[2].lower():
        return other[2]
    elif msg in [expression.lower() for expression in answers]:
        return '...'
    elif msg in [expression.lower() for expression in farewell]:
        return random.choice(farewell)
    else:
        return 'I did not understand what you said'

#SOCKET
HOST = ''
PORT = 7000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

while True:
    con, client = server_socket.accept()
    print('Conected with ',format(client))
    while True:
        msg = con.recv(1024)
        if not msg: break
        con.send(request(msg.decode()).encode())
    print('Finishing client conection ', client)
    con.close()
