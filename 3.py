import re

s = input()

a = re.findall(r'[a-z_]+', s)

print(a)