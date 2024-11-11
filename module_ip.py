import socket

# Lokální IP adresa
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print("Local IP:", local_ip)
