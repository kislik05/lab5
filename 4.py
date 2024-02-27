import re

s = input()

a = re.findall(r'[A-Z][a-z]+', s)

print(a)