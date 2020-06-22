# send at a MS-SQL server. Get a response. 
target=192.168.1.1

echo -ne "\x03" | nc -u $target 1434
