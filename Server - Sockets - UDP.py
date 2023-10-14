# Importing the necessary modules
import socket

# Some constants to keep things tidy
SERVER_IP = "127.0.0.1"  # This means the server is on my local machine
SERVER_PORT = 12345      # This should match the client's port number

#  Set up the UDP server socket. AF_INET for IPv4 and SOCK_DGRAM for UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout of 300 seconds (5 minutes)
server_socket.settimeout(300)

# Bind the server to a specific IP and port so it knows where to listen
server_socket.bind((SERVER_IP, SERVER_PORT))

# A friendly message so I know the server has started!
print("SIT202 Server Chat is ready to receive messages!")
print("The server will timeout if no message is received within 5 minutes.")

try:
    # Get into a loop to continuously listen for messages
    while True:
        # Waiting to receive a message from a client
        message, client_address = server_socket.recvfrom(1024)  # Use a 1024-byte buffer size

       # Decode the message
        decoded_message = message.decode()

        # Calculate the number of characters in the received message and print it
        char_count = len(decoded_message)
        print(f"Received a message with {char_count} characters from {client_address}")

        # Send back a response!
        # First, calculate the number of characters in the received message
        char_count = len(decoded_message)

        # Send back the count and the message in uppercase
        response_message = f"{char_count} characters: {decoded_message.upper()}"
        
        # Now send the response back to the client
        server_socket.sendto(response_message.encode(), client_address)

        # Set a way to stop the server. If it receives "exit", it will stop.
        if decoded_message.lower() == "exit":
            print("Exiting the server. Goodbye!")
            break
except socket.timeout:
    print("Server timed out after 5 minutes of inactivity. Goodbye!")

# It's a good idea to close the socket when done
server_socket.close()
