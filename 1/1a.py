# Solution for Day 1, Part A


with open("data.txt", 'r') as f:
        data = f.read().strip()
        numbers = data.splitlines()
        list_one = []
        list_two = []
        for line in numbers:
                num1, num2 = map(int, line.split())
                list_one.append(num1)
                list_two.append(num2)
        list_one.sort()
        list_two.sort()
        differences = [abs(a-b) for a,b in zip(list_one, list_two)]
        print(sum(differences))

