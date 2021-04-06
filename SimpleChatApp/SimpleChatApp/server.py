import socket
import threading

# CODE NOT FINISHED...

HEADER = 64
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())         # using host name, retrives IP for local machine acting as server host
ADDR = (SERVER, 0)                                          # binding to port 0 allows OS to choose available port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # (address family, socket type) creates default socket  
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    # allows address to be reused

server.bind(ADDR)
#print(server.getsockname())

    
sockets = [server]  # list of sockets
clients = {}        # list of connected clients


def handle_client(client):                          # will handle single client connection
    client_name = client.gethostname()
    client_ip = client.gethostbyname(client_name)   # retrieves client IP through socket's ADDR
    print('New connection from ', client_ip)

    connected = True                                # beings looping to handle client connections
    while connected:
        msg_header = client.recv(HEADER)
        msg_length = int(msg_header.decode(FORMAT)) # receiving header, decoding, and converting to int type

        msg = client.recv(msg_length).decode(FORMAT)
        if msg == '.exit':                          # exit command 
            connected = False
        print(f"[{client_ip}] {msg}")
            
    client.close()
    #return {'header': msg_header, 'data': client.recv(msg_length)}

def server_start():     # will handle incoming client connections
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        client = server.accept() 
        thread = threading.Thread(target = handle_client, args = (client))  # setting up threading
        thread.server_start()
        print(f"Active Connections: {threading.activeCount() - 1}")  # retrives # of conneted users by counting threads - 1
                                                                    # substract 1 to not count server thread
print("Server Starting")
server_start()
