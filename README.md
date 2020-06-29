# ddos_zoo
A collection of pcaps and simple scripts to receate the packets seen in DDoS attacks.

# structure
The directory structure is organized thusly `/ddos_attack_type/protocol/`

within each directory will be a pcap, perhaps a matching PoC script, and a readme file describing each potential attack type.
You can use the scripts and PCAPs to validate that your services are not at risk of the same kind of abuse.

# what it isn't
This isn't going to be another github full of fleshed out skiddie scripts. The intent is to provide an archive
of potential sources of DDoS activity. The PCAPs are intended for analysis. If there is a supporting script,
its intent is only to recreate the contents of the PCAP, not to create a full fledged DDoS attack. For that
you'll need to grok, understand, and write some scapy code at the very least.
