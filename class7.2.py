import re
a = input()
name = re.match(r"^[A-Z]{1}[a-z]+$", a)
print(name)