# Solution for Day 5, Part B

from functools import cmp_to_key

with open("data.txt", 'r') as f:
    rules = f.read().splitlines()
    parsed_rules = []
    for rule in rules:
        before, after = map(int, rule.split("|"))
        parsed_rules.append((before,after))

def compare(a,b):
    if (a,b) in parsed_rules:
        return -1
    elif (b,a) in parsed_rules:
        return 1
    else:
        return 0
    
with open("data_two.txt", 'r') as f:
    pages = f.read().splitlines()
    total = 0
    for page in pages:
        number_list = list(map(int, page.split(',')))
        sorted_number_list = sorted(number_list, key=cmp_to_key(compare))
        if number_list != sorted_number_list:
            total += sorted_number_list[len(sorted_number_list) // 2] 

print(total)
        

        