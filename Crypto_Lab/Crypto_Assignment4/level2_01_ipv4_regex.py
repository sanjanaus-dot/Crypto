# Find IPv4-address-like patterns using regex

import re

with open("security_data.txt", "r") as file:
    content = file.read()

ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", content)

for ip in ips:
    print(ip)
