# Solution for Day 4, Part A


def search(x, y, dx, dy, word, grid):
    for k in range(len(word)):
        nx, ny = x + (dx * k), y + (dy * k)
        if nx >= len(grid) or ny >= len(grid[0]) or nx < 0 or ny < 0 or grid[nx][ny] != word[k]:
            return False
    return True
        

with open("data.txt", 'r') as f:
    data = [list(list(line)) for line in f.read().splitlines()]
    rows, cols = len(data), len(data[0])
    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(-1,-1),(1,-1)]
    result = 0

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search(x,y,dx,dy,"XMAS",data):
                    result += 1

    print(result)
