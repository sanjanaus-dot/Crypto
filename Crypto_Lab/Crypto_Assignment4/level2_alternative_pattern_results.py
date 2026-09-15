# Extract patterns and store them in pattern_results.txt

import re

with open("security_data.txt", "r") as file:
    content = file.read()

ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", content)
emails = re.findall(r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,}", content)
sessions = re.findall(r"SEC-\d{4}-\d{4}", content)
hex_values = re.findall(r"\b[0-9a-fA-F]+\b", content)

with open("pattern_results.txt", "w") as file:
    file.write("IP addresses:\n")
    for item in ips:
        file.write(item + "\n")

    file.write("\nEmail addresses:\n")
    for item in emails:
        file.write(item + "\n")

    file.write("\nSession IDs:\n")
    for item in sessions:
        file.write(item + "\n")

    file.write("\nHexadecimal sequences:\n")
    for item in hex_values:
        file.write(item + "\n")

print("Results saved in pattern_results.txt")
