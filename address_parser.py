import re
import os


pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')

with open('data.txt','r') as f:
    content = f.read()
matches = pattern.findall(content)

for i in matches:
    print(i)
