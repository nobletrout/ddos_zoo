# ddos_zoo
A collection of pcaps and simple scripts to receate the packets you witness in ddos attacks.

# structure
The directory structure is organized thusly `/ddos_attack_type/protocol/`

within each directory will be a pcap, perhaps a matching PoC script, and a readme file describing each potential attack type.

# what it isn't
This isn't going to be another github full of fleshed out skiddie scripts. The intent is to provide an archive
of potential sources of DDoS activity. The PCAPs are intended for analyis. If there is a supporting script,
its intent is only to recreate the contents of the PCAP, not normally to create you a DDoS attack. For that
you'll need to grok, understand, and write some scapy code at least. But if you know anything about DDoS you'll
know that you should write it using raw interfaces in C.
