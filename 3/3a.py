# Solution for Day 3, Part A

import re

with open("data.txt", 'r') as f:
    data = f.read()
    matches = re.findall(r"mul\(\d+,\d+\)", data)
    total = 0
    for match in matches:
        num1, num2 = re.findall(r"\d+", match)
        total += (int(num1) * int(num2))
    print(total)
        
