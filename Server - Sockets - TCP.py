# Importing the necessary modules
import socket

# Some constants to keep things tidy
SERVER_IP = "127.0.0.1"  # This means the server is on my local machine
SERVER_PORT = 12345      # This should match the client's port number

#  Set up the TCP server socket. AF_INET for IPv4 and SOCK_STREAM for TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

# The server starts listening for incoming TCP requests.
server_socket.listen(5)  # 5 is the maximum number of queued connections

print("SIT202 Server Chat is ready to receive messages!")
print("The server will timeout if no message is received within 5 minutes.")

while True:  # To keep the server running
    client_socket, client_address = server_socket.accept()  # Server waits and accepts a client connection
    client_socket.settimeout(300)  # Set a timeout on the accepted connection

    try:
        # Loop to handle multiple messages from the same client
        while True:
            message = client_socket.recv(1024)  # Receive the message from the client
            if not message:
                # If message is empty, client has likely closed the connection
                break

            decoded_message = message.decode()

            # Calculate the number of characters in the received message and print it
            char_count = len(decoded_message)
            print(f"Received a message with {char_count} characters from {client_address}")

            # Send back the count and the message in uppercase
            response_message = f"{char_count} characters: {decoded_message.upper()}"
            client_socket.send(response_message.encode())

            # Exit if "exit" is received
            if decoded_message.lower() == "exit":
                print("Exiting the server. Goodbye!")
                client_socket.close()  # Close the connection to the client
                break

    except socket.timeout:
        print("Connection with client timed out after 5 minutes of inactivity.")
        client_socket.close()  # Close the connection to the client

    except Exception as e:
        print(f"An error occurred: {e}")
        client_socket.close()  # Close the connection to the client

server_socket.close()  # Close the server socket when exiting
