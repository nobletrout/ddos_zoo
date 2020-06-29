import scapy

# pick your dst to be a broadcast address, it'll route there since
# the middle network doesn't know what the local network is
sr1(IP(dst='198.168.0.255',src='1.2.3.4')/ICMP())
