import re


text = "Hello"

m = re.match(r"WONT MATCH", text)
m.group(0)
