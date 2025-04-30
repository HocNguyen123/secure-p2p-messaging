import tkinter as tk
from threading import Thread
from crypto_utils import encrypt_message, decrypt_message
from network_utils import send_message, recv_message
from key_manager import rotate_key
from config import SALT, KEY_ROTATE_INTERVAL

class ChatApp:
    def __init__(self, master, conn, key, password):
        self.master = master
        self.conn = conn
        self.base_key = key
        self.password = password
        self.counter = 0

        master.title("Secure P2P Chat")

        self.text_area = tk.Text(master, height=25, width=60)
        self.text_area.pack()

        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack()

        # Start a thread to receive messages in background
        self.receiver_thread = Thread(target=self.receive_messages, daemon=True)
        self.receiver_thread.start()

    def get_current_key(self):
        if self.counter > 0 and self.counter % KEY_ROTATE_INTERVAL == 0:
            return rotate_key(self.password, SALT, self.counter)
        return self.base_key

    def send_message(self):
        msg = self.entry.get()
        if msg:
            self.counter += 1
            key = self.get_current_key()
            encrypted = encrypt_message(key, msg)
            send_message(self.conn, encrypted)
            self.text_area.insert(tk.END, f"You → (hex): {encrypted.hex()}\n")
            self.entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                data = recv_message(self.conn)
                if data:
                    key = self.get_current_key()
                    plaintext = decrypt_message(key, data)
                    self.text_area.insert(tk.END, f"Friend → (hex): {data.hex()}\nFriend → (text): {plaintext}\n")
            except Exception as e:
                self.text_area.insert(tk.END, f"[Error receiving]: {e}\n")
                break
