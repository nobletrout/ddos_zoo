
# sip_invite
SIP is a protocol for making and receiving phone calls using the Internet.
An INVITE request looks a lot like a HTTP GET Request, however, it can
optionally (and typically) uses UDP instead of TCP as a transport layer.

Sending a SIP INVITE requests causes the receiving node, either another
SIP User Equipment (aka - phone) or registration service to return a message
indicating that the INVITE was received. Then it notifies that the phone
is ringing (creating a simulated ringing noise on your phone) and followed
by a 200 Ok message and a stream of RTP data which is the connected voice.

These three separate messages are sent without any ACK from the client,
causing a amplification of 3x the number of packets. Also a lot of phones
ringing.

This pcap is a trimmed version taken from the wireshark wiki.
https://wiki.wireshark.org/SampleCaptures#SIP_and_RTP

