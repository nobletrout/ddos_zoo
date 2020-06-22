import scapy
victim = '198.18.0.222'
sr1(IP(dst='198.18.0.1',src=victim)/TCP(sport=1234,dport=22,flags="S")
