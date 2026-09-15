# Find session IDs in the format SEC-YYYY-NNNN

import re

with open("security_data.txt", "r") as file:
    content = file.read()

session_ids = re.findall(r"SEC-\d{4}-\d{4}", content)

for session_id in session_ids:
    print(session_id)
