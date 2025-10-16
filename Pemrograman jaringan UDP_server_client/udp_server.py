import socket
import datetime
import os

HOST = "127.0.0.1"
PORT = 5005
log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "server_log.txt")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Server berjalan di {HOST}:{PORT}")
print("Menunggu pesan dari client...\n")

while True:
    data, addr = server_socket.recvfrom(1024)
    pesan = data.decode('utf-8')
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{waktu}] Dari {addr}: {pesan}")

    with open(log_path, "a") as f:
        f.write(f"[{waktu}] Dari {addr}: {pesan}\n")

    balasan = f"Server menerima pesan '{pesan}' pada {waktu}"
    server_socket.sendto(balasan.encode('utf-8'), addr)
