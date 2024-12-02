# Solution for Day 1, Part B

from collections import Counter

with open("data.txt", 'r') as f:
        data = f.read().strip()
        numbers = data.splitlines()
        list_one = []
        list_two = []
        for line in numbers:
                num1, num2 = map(int, line.split())
                list_one.append(num1)
                list_two.append(num2)
        
        # Initial Brute Force

        # list_one.sort()
        # list_two.sort()
        # similarity = 0
        # for num in list_one:
        #         occ = 0
        #         for num_two in list_two:
        #             if num == num_two:
        #                    occ += 1
        #             elif num_two > num:
        #                    break
        #         simularity += occ * num

        # Slightly Optimized
        list_one_counts = Counter(list_one)
        similarity = sum(num * list_one_counts[num] for num in list_two)                    
        print(similarity)

