
import re

s = input()
a = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

print(a)
