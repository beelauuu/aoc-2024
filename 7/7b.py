# Solution for Day 7, Part B

# Solution for Day 7, Part A

def checkIfPossible(expected, curr, index, parts):
    if index == len(parts) - 1:
        return curr == expected
    elif curr > expected:
        return False
    else:
        concat = int(str(curr) + str(parts[index+1]))
        return checkIfPossible(expected, curr * parts[index+1], index+1, parts) or checkIfPossible(expected, curr + parts[index+1], index+1, parts) or checkIfPossible(expected, concat, index+1, parts)


with open("data.txt", 'r') as f:
    equations = f.read().splitlines()
    final_total = 0
    for eq in equations:
        total, parts = eq.split(":")
        total = int(total)
        parts = parts.strip()
        parts = list(map(int, parts.split(' ')))

        
        if checkIfPossible(total, parts[0], 0, parts):
            final_total += total
    print(final_total)