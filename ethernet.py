from scapy.all import Ether, sendp, get_if_hwaddr

target_mac = "ce:00:51:2a:a5:75"
interface = "eth0"
my_mac = get_if_hwaddr(interface)

packet = Ether(src=my_mac, dst=target_mac, type=0xFFFF)
#packet = packet / "Challenge Data"

sendp(packet, iface=interface)
