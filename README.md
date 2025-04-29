# 🔐 Secure P2P Messaging App

This project is a secure instant messaging tool between two peers (Alice and Bob) with encrypted communication, a user-friendly GUI, and key management.

## 📦 Features
- AES-128 encryption with PBKDF2 key derivation
- Random IV for every message
- GUI with message display and input (Tkinter)
- Periodic key rotation
- Socket-based client/server messaging over TCP

## 🛠️ Project Structure

secure_p2p_messaging/
│
├── main.py                  # 🔌 Entry point: launch client or server with GUI
│
├── crypto_utils.py          # 🔐 Encryption/decryption functions (AES + padding + IV)
├── key_manager.py           # 🔁 Key derivation and periodic re-key logic
├── network_utils.py         # 🌐 Socket communication (send/recv, server/client)
├── gui.py                   # 🖼️ GUI interface (Tkinter-based chat window)
│
├── config.py                # ⚙️ Shared constants (e.g., port, buffer size, message limit)
│
├── tests/                   # 🧪 Unit tests
│   ├── test_crypto.py
│   ├── test_network.py
│   ├── test_key_manager.py
│
├── assets/                  # 📸 Optional: icons, logos, screenshots for report
│
├── report/                  # 📄 Screenshots + design report (PDF or markdown)
│   ├── design_diagram.png
│   ├── screenshots/
│   └── final_report.md
│
└── README.md                # 📘 How to run, install, test


## 📚 How to Run

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/secure-p2p-messaging.git
cd secure-p2p-messaging

# Run the app (server or client)
python main.py


---

## 🚦 6. Commit & Push Initial Setup

```bash
git add .
git commit -m "Initial project setup with file structure"
git push origin main
