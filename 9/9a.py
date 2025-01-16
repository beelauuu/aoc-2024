# Solution for Day 9, Part A

with open("data.txt", 'r') as f:
    equations = f.read()
    curr = 0
    index = 0
    spaceOrNot = False
    mappings = {}
    dot_positions = []
    normal_positions = []

    for part in equations:
        if not spaceOrNot:
            mappings[curr] = int(part)
            curr += 1
            for i in range(int(part)):
                normal_positions.append(index)
                index += 1

        else:
            for i in range(int(part)):
                dot_positions.append(index)
                index += 1
        spaceOrNot = not spaceOrNot

    unrolled = [key for key, count in mappings.items() for _ in range(count)]
    total = 0

    i = 0
    while unrolled:
        if i in dot_positions:
            value = unrolled.pop()
            pos = dot_positions.pop(0)
        else:
            value = unrolled.pop(0)
            pos = normal_positions.pop(0)
        total += value * pos
        i += 1

    print(total)
        

    
    
    