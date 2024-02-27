import re
s = input()

a = re.findall("ab{2,3}", s)

print(a)