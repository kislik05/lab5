import re
s = input()

a = re.findall("ab*", s)

print(a)