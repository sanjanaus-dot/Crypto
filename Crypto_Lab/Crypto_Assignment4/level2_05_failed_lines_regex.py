# Display lines containing "failed", ignoring case

import re

with open("security_data.txt", "r") as file:
    for line in file:
        if re.search(r"failed", line, re.IGNORECASE):
            print(line.strip())
