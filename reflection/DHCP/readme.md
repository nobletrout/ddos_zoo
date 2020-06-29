# DHCP Inform Reflection

Appears to get about 1.18x byte increase. Possibilities for more. Finding a DHCP
server with lots of options would help. Also probably possible to trim down the
request.

## Notes


- the ability to issue unicast queries against DHCP servers is not RFC
        compliant. However, it doesn't seem to stop most DHCP servers from
        responding. Would be a neat showcase to scan the internet for all
        accessible DHCP servers.

- BOOTP is sort of a sister protocol to DHCP. Probably some additinoal
        areas to explore there. If you find a misconfigured DHCP that's on the
        internet, it might lead to TFTP configuration discoveries and paths
        to files you might not otherwise discover.
