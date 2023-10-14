# Importing necessary modules
import socket

# Define some constants.
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(300)  # Set a timeout of 5 minutes

print("Welcome to the SIT202 Client Chat!")

def handshake_procedure():
    """Handles the handshake process with the server."""
    # Step 1: Send "Hello" to the server
    client_socket.sendto("Hello".encode(), (SERVER_IP, SERVER_PORT))

    try:
        # Wait for a response from the server
        response, server_address = client_socket.recvfrom(1024)
        print("Received from server:", response.decode())

        # Step 3: Client sends the name to the server
        name = input("Enter your name: ")
        client_socket.sendto(name.encode(), (SERVER_IP, SERVER_PORT))

        # Wait for final greeting response from the server
        greeting_response, server_address = client_socket.recvfrom(1024)
        print("Received from server:", greeting_response.decode())

    except socket.timeout:
        print("No response received from the server during handshake. Exiting...")
        client_socket.close()
        exit()  # Exit the program if handshake fails

# Start the handshake procedure
handshake_procedure()

# Main message loop
while True:   
    # Get the message to send to the server
    message = input("Enter a message to send to the server (type 'quit' to quit): ")

    # If the message is "quit", we'll break out of the loop
    if message.lower() == "quit":
        print("Exiting the client. Goodbye!")
        break

    # Send the message to the server
    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    try:
        # Wait for a response from the server
        response, server_address = client_socket.recvfrom(1024)  # 1024 is the buffer size, in bytes

        # Displaying the response
        print("Received from server:", response.decode())

    except socket.timeout:
        print("No response received from the server after 5 minutes. Please try again or type 'quit' to quit.")

# Good practice to close the socket when we're done
client_socket.close()
