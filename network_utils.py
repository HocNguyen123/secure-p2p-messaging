import socket
from config import BUFFER_SIZE

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', port))
    server.listen(1)
    conn, addr = server.accept()
    print(f"Connected by {addr}")
    return conn

def start_client(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"Connected to {host}:{port}")
    return client

def send_message(conn, data):
    conn.sendall(data)

def recv_message(conn):
    return conn.recv(BUFFER_SIZE)
