import argparse
import socket
from key_manager import derive_key
from network_utils import start_server, start_client
from gui import ChatApp
from config import PORT, SALT
import tkinter as tk

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['server', 'client'], required=True)
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--password', required=True)
    args = parser.parse_args()

    key = derive_key(args.password, SALT)

    if args.mode == 'server':
        print("Waiting for connection...")
        conn = start_server(PORT)
    else:
        conn = start_client(args.host, PORT)

    root = tk.Tk()
    app = ChatApp(root, conn, key, args.password)
    root.mainloop()

if __name__ == '__main__':
    main()
