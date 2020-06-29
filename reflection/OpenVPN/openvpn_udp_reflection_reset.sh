#!/bin/bash
echo -e "\x38\x01\x00\x00\x00\x00\x00\x00\x00" | timeout 10 nc -u 182.76.113.54 1194
