# sctp\_reflection

1. verify that responder has open socket (responds with `INIT_ACK`)
2. flood with spoofed address of victim
3. profit?

an SCTP INIT packet is approximately 82 bytes (for IPv4)

observational evidence appears to demonstrate that an `INIT_ACK` is 298 bytes. This gets us an amplifiction factor of 2.6x.

an added benefit is, much like the great GRE flood of 2016 (Mirai) you will probably catch the ISPs with their
pants around their ankles because this isn't a TCP or UDP based protocol.
