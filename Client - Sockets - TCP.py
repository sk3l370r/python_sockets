# Importing necessary modules
import socket

# Define some constants. Better than using magic numbers!
SERVER_IP = "127.0.0.1"  # I'm running the server on the same machine, so localhost!
SERVER_PORT = 12345      # Random port number, this can be changed.

# Create a TCP socket. AF_INET is for IPv4 and SOCK_STREAM means it's TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout of 300 seconds (5 minutes) for receiving response from the server
client_socket.settimeout(300)

# Connect to the server
client_socket.connect((SERVER_IP, SERVER_PORT))

# A quick greeting!
print("Welcome to the SIT202 TCP Client Chat!")

while True:   # Start an infinite loop
    # Get the message to send to the server
    message = input("Enter a message to send to the server (type 'quit' to quit): ")

    # If the message is "quit", we'll break out of the loop
    if message.lower() == "quit":
        print("Exiting the client. Goodbye!")
        break

    # Time to send the message! Off it goes!
    client_socket.send(message.encode())

    try:
        # Wait for a response from the server
        response = client_socket.recv(1024)  # 1024 is the buffer size, in bytes

        # Displaying the response
        print("Received from server:", response.decode())

    except socket.timeout:
        print("No response received from the server after 5 minutes. Please try again or type 'quit' to quit.")

# Good practice to close the socket when we're done
client_socket.close()
