import socket

# CODE NOT FINISHED...

HEADER = 64
FORMAT = 'utf-8'
SERVER = "192.168.1.13" # local IPv4
ADDR = (SERVER, 54850)  # figure out way to use same port as server automatically
                        # --or just use same static port for both

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Encoding username, and preparing and encoding header before sending to server
my_username = input("Username: ")
username = my_username.encode(FORMAT)
username_header = f"{len(username):<{HEADER}}".encode(FORMAT)   # encodes username_header as left-aligned f-string 
client.send(username_header + username)                         

# Begins looping send/receive messages
while True:
    # SENDING MESSAGE
    message = input()
    msg = message.encode(FORMAT)                            # encodes message
    msg_header = f"{len(msg):<{HEADER}}".encode(FORMAT)     # encodes message header
    client.send(msg_header + msg)                           # sends 

    while True:
        # RECEIVING MESSAGE
        username_header = client.recv(HEADER)
        username_length = int(username_header.decode(FORMAT))   # decodes username_header and converts to int type
        username = client.recv(username_length).decode(FORMAT)  # receives username from sender-client
    
client.send(msg_header + msg)

