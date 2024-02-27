import re

s = input()

a = re.findall(r'a.*b\b', s)

print(a)