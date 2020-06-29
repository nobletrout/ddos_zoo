# openvpn_udp_reflection_reset
You can (basically) send any ol' crap you want on UDP to a listening OpenVPN
Server. By default it'll be setup to respond with 4 repeated attempts to
"reset" the connection. This leads to an amplifcation factor of 4x packets.

