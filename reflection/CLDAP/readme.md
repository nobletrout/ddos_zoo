# cldap_ddos_reflection
CLDAP: Connectionless LDAP. Intended for lightweight access to certain
attributes available from the LDAP/Activedirectory server. This is used
for non-authentication level data for an endpoint.

The perl script is a modified hack that queries for `*` instead of
specific attributes. Typically a response will be about 3000 bytes, or two
fragmented packets.

https://www.ixiacom.com/company/blog/following-crumbs-deconstructing-cldap-ddos-reflection-attack
