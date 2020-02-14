char = "\xa1"  # '¡'

char.encode("utf-8")  # OK
char.encode("cp932")  # ERROR
