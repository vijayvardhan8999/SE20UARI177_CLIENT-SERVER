import socket
import threading

# Create a socket for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the IP address and port for the server
server_ip = "127.0.0.1"
server_port = 12345

# Bind the socket to the server address
server.bind((server_ip, server_port))

# Listen for incoming connections
server.listen()

print(f"Server is listening on {server_ip}:{server_port}")

# List to hold connected clients
clients = []

# Function to broadcast messages to all connected clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if unable to send message
                remove(client)

# Function to remove a client from the list
def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(message.decode('utf-8'))
                broadcast(message, client_socket)
            else:
                # Remove the client if no data is received
                remove(client_socket)
        except:
            continue

# Accept and handle incoming client connections
while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    print(f"Client {client_address} connected")

    # Create a thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
