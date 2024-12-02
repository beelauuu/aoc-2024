# Solution for Day 2, Part B

def is_safe(curr_report):
    decreasing = all(curr_report[i] > curr_report[i+1] for i in range(len(curr_report)-1)) 
    increasing = all(curr_report[i] < curr_report[i+1] for i in range(len(curr_report)-1))
    within_values = all(1 <= abs(curr_report[i] - curr_report[i+1]) <= 3 for i in range(len(curr_report)-1))
    return (decreasing or increasing) and within_values

with open("data.txt", 'r') as f:
    data = f.read().strip().splitlines()
    safe = 0
    for line in data:
        curr_report = list(map(int, line.split()))
        if is_safe(curr_report):
            safe += 1
        else:
            for i in range(len(curr_report)):
                modified_report = curr_report[:i] + curr_report[i+1:]
                if is_safe(modified_report):
                    safe += 1
                    break
    print(safe)
            
        

