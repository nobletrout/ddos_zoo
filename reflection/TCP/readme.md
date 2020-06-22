# tcp_reflection_ddos
1. Verify that host (victim) does not respond with an RST to a port which it
receives an out of sequence SYN/ACK packet.
2. Send a SYN packet to reflector with source IP of victim
3. Reflector will send repeated SYN/ACK's in attempt to connect to victim.
