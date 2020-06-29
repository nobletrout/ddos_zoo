# icmp_broadcast_ping
"Surely no one can be that stupid?"

But yes, sadly, it appears Cisco networking equipment (switches/routers) will
respond to a broadcast ping that comes from a non-local network.

So you effectively send a ICMP ping request to a broadcast netblock, and get
multiple responses sent back to your victim. 
