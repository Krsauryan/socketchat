import socket
import threading

# creating local host and port for chat 
host = 'localhost'
port = 8000

# create new socket object of the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific host and port defined on line 5 and 6
server.bind((host, port))

# Listen for incoming connections 
server.listen()

# List of clients connected to the server
clients = []

# Function to handle client connections
def handle_client(client_socket, client_address):
    # Add the client to the list of connected clients
    clients.append(client_socket)

    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()

        # Broadcast the data to all connected clients
        for client in clients:
            client.sendall(data.encode())

        # If the client disconnects, remove it from the list of connected clients
        if not data:
            clients.remove(client_socket)
            client_socket.close()
            break

# Function to start the server and handle incoming connections
def start_server():
    print(f'Server listening on {host}:{port}')

    while True:
        # Accept incoming connections
        client_socket, client_address = server.accept()

        # Create a new thread to handle the client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Start the server
start_server()