# Reflection Attacks
This directory contains a set of protocols that are vulnerable to reflection attacks. A lot has been been written about what a reflection attack is,
but it's easy to get lost in the details of a specific protocol. So here is a brief run down of what they are.

IPv4 and IPv6 do not have a connection oriented system. In other words, there is no way you can verify that I am who I say I am (source IP address) alone
based on the IP addresses in a packet. For that you need context or an upper layer protocol with some form of protection. TCP has it, so do some forms of IPSec,
UDP doesn't.

This allows for a sneaky form of sending a packet to a third party, called the reflector or responder, that will forward or respond to requests you send
towards to your intended victim. This lets you, the attacker, benefit in two discrete ways:

1. You can hide your identity. The attack will look like it comes from the third party.
2. If you are lucky, you can "amplify" your attack, making your reflector send more and/or more packets than you originally sent, increasing the size of your attack.

So, to recap Attacker sends requests to Responder, Responder sends bigger response to victim. Attacker does this by forging the original source address (typically IPv4 or IPv6).

<img width="774" alt="image" src="https://user-images.githubusercontent.com/16596040/115298245-39c7e780-a12b-11eb-9fa0-5b0439793c7c.png">
