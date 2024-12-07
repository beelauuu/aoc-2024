# Solution for Day 6, Part A

def find_start(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "^":
                return (i,j)
    

with open("data.txt", 'r') as f:
    data = [list(list(line)) for line in f.read().splitlines()]
    steps = set()
    x, y = find_start(data)
    curr = "^"
    
    steps.add((x, y))
    while x+1 < len(data) and x-1 >= 0 and y+1 < len(data[x]) and y-1 >= 0:
        if curr == "^":
            if data[x-1][y] == "#":
                curr = ">"
                y += 1
            else:
                x -= 1
        elif curr == ">":
            if data[x][y+1] == "#":
                curr = "v"
                x += 1
            else:
                y += 1
        elif curr == "v":
            if data[x+1][y] == "#":
                curr = "<"
                y -= 1
            else:
                x += 1
        elif curr == "<":
            if data[x][y-1] == "#":
                curr = "^"
                x -= 1
            else:
                y -= 1
        steps.add((x, y))

    print(len(steps))         