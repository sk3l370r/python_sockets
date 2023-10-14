# Importing the necessary modules
import socket

# Some constants
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

# Set up the UDP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.settimeout(300)  # Set a timeout of 5 minutes
server_socket.bind((SERVER_IP, SERVER_PORT))

def handshake(server_socket):
    # Always expect "Hello" first
    message, client_address = server_socket.recvfrom(1024)
    print("Hello received")  # Display acknowledgement after receiving 'Hello'
    response = "Hello, what’s your name?"
    server_socket.sendto(response.encode(), client_address)
    print("Name request sent")  # Display acknowledgement after sending the response

    # Always expect the name next
    name, _ = server_socket.recvfrom(1024)
    response = f"Hello {name.decode()}, welcome to SIT202"
    server_socket.sendto(response.encode(), client_address)
    print("Welcome message sent")  # Display acknowledgement after sending the greeting

# Start the handshake
handshake(server_socket)

print("SIT202 Server Chat is ready to receive messages!")
print("The server will timeout if no message is received within 5 minutes.")

try:
    # Regular messaging after the handshake
    while True:
        message, client_address = server_socket.recvfrom(1024)
        decoded_message = message.decode()

        char_count = len(decoded_message)
        print(f"Received a message with {char_count} characters from {client_address}")

        response_message = f"{char_count} characters: {decoded_message.upper()}"
        server_socket.sendto(response_message.encode(), client_address)

        if decoded_message.lower() == "exit":
            print("Exiting the server. Goodbye!")
            break

# Set Timeout
except socket.timeout:
    print("Server timed out after 5 minutes of inactivity. Goodbye!")

# Close the socket
finally:
    server_socket.close()