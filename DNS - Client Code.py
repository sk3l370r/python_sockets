import socket

# Initialising the UDP client socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Defining the server's address and port number
server_address = ("127.0.0.1", 5354)

# Ensuring that A and CNAME are valid DNS record types that can be queried
valid_record_types = ["A", "CNAME"]

def get_record_type():
    # Prompt the user to enter the record type and validate the input.
    while True:
        record_type = input("Enter record type (A/CNAME): ").upper()
        if record_type in valid_record_types:
            return record_type
        print("Invalid record type. Please enter 'A' or 'CNAME'.")

def get_domain_name():
    # Prompt the user to enter the domain name and validate the input.
    while True:
        domain_name = input("Enter domain name: ")
        # Ensure the domain name is not empty
        if domain_name:  
            return domain_name
        print("Invalid domain name. Please enter a valid domain.")

def continue_query():
    # Ask the user if they wish to continue with another DNS query.
    while True:
        decision = input("Would you like to continue with another DNS query? (yes/no): ").lower()
        if decision in ["yes", "no"]:
            # Returns True if user chooses "yes", otherwise False
            return decision == "yes"  
        print("Invalid input. Please enter 'yes' or 'no'.")

# Implementing main loop to continuously prompt user for queries until they decide to exit
while True:
    record_type = get_record_type()
    domain = get_domain_name()

    # Sending the query to the DNS server
    client.sendto(f"{domain},{record_type}".encode('utf-8'), server_address)
    
    # Receive and then display the response from the server
    data, _ = client.recvfrom(1024)
    print("Response:", data.decode('utf-8'))
    
    # Enabing program exit if the user does not wish to continue.
    if not continue_query():
        print("Exiting the client. Goodbye!")
        break
