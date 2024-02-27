
import re

s = input()
a = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), s)

print(a)
