import socket
import threading


host = '127.0.0.1'
port = 8080

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client.connect((host, port))


def echo():
    while True:
        message = input('Enter a message: ')
        client.send(message.encode('ascii'))


def read():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(f'message from other clients: {message}')
        except:
            client.close()
            break


echo_thread = threading.Thread(target=echo)
echo_thread.start()

read_thread = threading.Thread(target=read)
read_thread.start()

