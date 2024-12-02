# Solution for Day 2, Part A
with open("data.txt", 'r') as f:
    data = f.read().strip().splitlines()
    safe = 0
    for line in data:
        curr_report = list(map(int, line.split()))
        decreasing = all(curr_report[i] > curr_report[i+1] for i in range(len(curr_report)-1)) 
        increasing = all(curr_report[i] < curr_report[i+1] for i in range(len(curr_report)-1))
        within_values = all(1 <= abs(curr_report[i] - curr_report[i+1]) <= 3 for i in range(len(curr_report)-1))
        if (decreasing or increasing) and within_values:
            safe += 1
    print(safe)
            
        

