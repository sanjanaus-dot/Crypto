# Find email-address-like patterns using regex

import re

with open("security_data.txt", "r") as file:
    content = file.read()

emails = re.findall(r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,}", content)

for email in emails:
    print(email)
