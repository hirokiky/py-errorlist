import os


HERE = os.path.dirname(__file__)
p = os.path.join(HERE, "utf8.txt")

with open(p, encoding="cp932") as f:
    f.read()
