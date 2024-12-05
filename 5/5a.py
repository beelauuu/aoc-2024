# Solution for Day 5, Part A

with open("data.txt", 'r') as f:
    mapped_rules_after = {}
    mapped_rules_before = {}
    rules = f.read().splitlines()
    for rule in rules:
        before, after = rule.split("|")
        if int(before) not in mapped_rules_after:
            mapped_rules_after[int(before)] = []
        if int(after) not in mapped_rules_before:
            mapped_rules_before[int(after)] = []
        mapped_rules_after[int(before)].append(int(after))
        mapped_rules_before[int(after)].append(int(before))
    
with open("data_two.txt", 'r') as f:
    pages = f.read().splitlines()
    total = 0
    for page in pages:
        number_list = list(map(int, page.split(',')))
        successful = True
        for i in range(len(number_list)):
            for j in range(0, i):
                if (number_list[i] in mapped_rules_before and number_list[j] not in mapped_rules_before[number_list[i]]):
                    successful = False
                    break
            for j in range(i+1, len(number_list)):
                if (number_list[i] in mapped_rules_after and number_list[j] not in mapped_rules_after[number_list[i]]):
                    successful = False
                    break
        if successful:
            total += number_list[len(number_list) // 2]

print(total)
             
            