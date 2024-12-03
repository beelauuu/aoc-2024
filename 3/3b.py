# Solution for Day 3, Part B

import re

with open("data.txt", 'r') as f:
    data = f.read()
    matches = re.findall(r"do\(\)|mul\(\d+,\d+\)|don't\(\)", data)
    total = 0
    enabled = True
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        else:
            if enabled:
                num1, num2 = re.findall(r"\d+", match)
                total += (int(num1) * int(num2))
    print(total)