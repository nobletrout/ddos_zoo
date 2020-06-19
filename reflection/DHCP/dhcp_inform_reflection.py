from scapy.all import *



discover=IP(src='198.18.3.100', dst='198.18.2.100')/UDP(dport=67,sport=68)/BOOTP(op=1,ciaddr='10.10.10.10')/DHCP(options=[('message-type', 'inform'), ('end')])

send(discover)
