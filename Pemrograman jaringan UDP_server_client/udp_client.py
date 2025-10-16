import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Ketik 'exit' untuk keluar.\n")

while True:
    pesan = input("Masukkan pesan ke server: ")
    if pesan.lower() == "exit":
        print("Client ditutup.")
        break

    print(f"Mengirim pesan ke {SERVER_IP}:{SERVER_PORT}")
    client_socket.sendto(pesan.encode('utf-8'), (SERVER_IP, SERVER_PORT))

    data, _ = client_socket.recvfrom(1024)
    print("Balasan dari server:", data.decode('utf-8'))
