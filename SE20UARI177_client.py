import socket
import threading

# Create a socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the server IP address and port to connect to
server_ip = "127.0.0.1"
server_port = 12345

# Connect to the server
client.connect((server_ip, server_port))

# Function to send messages to the server
def send_message():
    while True:
        message = input()
        client.send(message.encode('utf-8'))

# Function to receive messages from the server
def receive_message():
    while True:
        try:
            message = client.recv(1024)
            print(message.decode('utf-8'))
        except:
            print("Connection closed.")
            break

# Create threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

# Start the threads
send_thread.start()
receive_thread.start()
