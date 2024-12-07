# Solution for Day 6, Part B


def find_start(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "^":
                return (i,j)
    
def simulate(x, y, data, ox, oy):
    steps = set()
    data[ox][oy] = "#"
    curr = "^"
    
    while True:
        if x+1 >= len(data) or x-1 < 0 or y+1 >= len(data[x]) or y-1 < 0:
            data[ox][oy] = "."
            return False
        if ((x,y), curr) in steps:
            data[ox][oy] = "."
            return True
        steps.add(((x,y), curr))

        if curr == "^":
            if data[x-1][y] == "#":
                curr = ">"
            else:
                x -= 1
        if curr == ">":
            if data[x][y+1] == "#":
                curr = "v"
            else:
                y += 1
        if curr == "v":
            if data[x+1][y] == "#":
                curr = "<"
            else:
                x += 1
        if curr == "<":
            if data[x][y-1] == "#":
                curr = "^"
            else:
                y -= 1


with open("data.txt", 'r') as f:
    data = [list(list(line)) for line in f.read().splitlines()]
    x, y = find_start(data)
    count = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != "#" and (i,j) != (x,y) and simulate(x, y, data, i, j) == True:
                count += 1
    
    print(count)

    

            