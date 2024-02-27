
import re

s = input()
a = re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

print(a)
