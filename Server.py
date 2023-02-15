import socket
import threading

host = '127.0.0.1'
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print("Server is listening.")

clients = []


def handle(client: socket.socket):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(f'client {address[1]} says {message}')
            for reciever_client in clients:
                if reciever_client != client:
                    reciever_client.send(message.encode('ascii'))
        except:
            print('Error in handling.')
            clients.remove(client)
            client.close()
            break


while True:
    client, address = server.accept()
    print(f'connected with {address}.')
    clients.append(client)
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()
