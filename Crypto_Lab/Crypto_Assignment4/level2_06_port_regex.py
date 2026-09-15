# Extract the port number

import re

with open("security_data.txt", "r") as file:
    content = file.read()

port = re.search(r"Port (\d+) connection established", content)

if port:
    print("Port number:", port.group(1))
else:
    print("Port not found")
