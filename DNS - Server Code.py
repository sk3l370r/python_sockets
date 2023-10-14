import socket

# Setting up my "fake" DNS data as a dictionary.
dns_records = {
    "example.com": {
        "A": "192.0.2.1",
        "MX": "mail.example.com",
        "NS": "ns1.example.com"
    },
    "www.example.com": {
        "CNAME": "example.com"
    },
    "test.com": {
        "A": "192.0.2.2",
        "MX": "mail.test.com",
        "NS": "ns1.test.com"
    },
    "www.test.com": {
        "CNAME": "test.com"
    },
    "www.test2.com": {
        "CNAME": "test.com"
    },
    "www.test3.com": {
        "CNAME": "test.com"
    },
    "mail.example.com": {
        "A": "192.0.2.3"
    },
    "ns1.example.com": {
        "A": "192.0.2.4"
    },
    "mail.test.com": {
        "A": "192.0.2.5"
    },
    "ns1.test.com": {
        "A": "192.0.2.6"
    }
}

# Creating the UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 5354))

# Setting a timeout for receiving data. 
# If no data is received for 5 minutes (300 seconds), 
# the recvfrom method will raise a socket.timeout exception.
# For testing purposes only.
server.settimeout(300)

print("DNS server is running. Ready to decode some DNS!")

# Implementing the loop that enables the client response with multiple queries.
try:
    while True:
        # Receiving the query from the client
        data, addr = server.recvfrom(1024)
        query = data.decode('utf-8').split(",")  # Assuming input as domain,record_type

        # Check the dictionary to retrieve the appropriate DNS record
        domain = query[0]
        record_type = query[1]
        response = dns_records.get(domain, {}).get(record_type, "Not found")
        
        # Format the response
        formatted_response = f"{record_type}: {response}"
        
        # Sending the response back to the client
        server.sendto(formatted_response.encode('utf-8'), addr)

# Handling the timeout exception
except socket.timeout:
    print("No activity for 5 minutes. Shutting down the server for testing purposes.")
    server.close()