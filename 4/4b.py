# Solution for Day 4, Part B

def search(x, y, grid):
    if x-1 >= 0 and x+1 < len(grid) and y-1 >= 0 and y+1 < len(grid[0]):
        top_left_corner = grid[x-1][y-1] 
        top_right_corner = grid[x-1][y+1] 
        bottom_left_corner = grid[x+1][y-1] 
        bottom_right_corner = grid[x+1][y+1]
        caseOne = top_left_corner == 'M' and bottom_right_corner == 'S' and top_right_corner == 'S' and bottom_left_corner == 'M'
        caseTwo = top_left_corner == 'M' and bottom_right_corner == 'S' and top_right_corner == 'M' and bottom_left_corner == 'S'
        caseThree = top_left_corner == 'S' and bottom_right_corner == 'M' and top_right_corner == 'S' and bottom_left_corner == 'M'
        caseFour = top_left_corner == 'S' and bottom_right_corner == 'M' and top_right_corner == 'M' and bottom_left_corner == 'S'

        return caseOne or caseTwo or caseThree or caseFour

with open("data.txt", 'r') as f:
    data = [list(list(line)) for line in f.read().splitlines()]
    rows, cols = len(data), len(data[0])
    result = 0
    for x in range(rows):
        for y in range(cols):
            if data[x][y] == 'A' and search(x,y,data):
                result += 1
                

    print(result)
