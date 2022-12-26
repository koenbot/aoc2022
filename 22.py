lines = open("22.txt").readlines()

grid = []
cmds = []

# n = 16
n = 150

for line in lines:
    if line == "":
        continue
    if line[0] not in [" ", ".", "#"]:
        s = line.strip()
        while len(s) > 0:
            rpos = s.find("R")
            lpos = s.find("L")
            if rpos == -1:
                rpos = 1e9
            if lpos == -1:
                lpos = 1e9
            pos = min(rpos, lpos)
            if pos == 1e9:
                steps = int(s)
                cmds.append(["step", steps])
                break
            steps = int(s[:pos])
            turn = s[pos]
            cmds.append(["step", steps])
            cmds.append(["turn", turn])
            s = s[pos+1:]

    row = []
    for c in line:
        if c == " ":
            row.append(2)
        if c == ".":
            row.append(0)
        if c == "#":
            row.append(1)
    if len(row) < n:
        row = row + [2] * (n - len(row))
    grid.append(row)


r = 0
c = 8

# 0 = right, 1 = down, 2 = left, 3 = up
dir = 0


print(grid[r][c])

for a, b in cmds:
    if a == "turn":
        if b == "R":
            dir = (dir + 1) % 4
        if b == "L":
            dir = (dir - 1) % 4
    if a == "step":
        for i in range(b):
            print(i,b,r,c, dir)
            if dir == 0:
                nextc = c + 1
                if nextc >= len(grid[r]) or grid[r][nextc] == 2: # look for first non-blank grid
                    nextc = 0
                    while grid[r][nextc] == 2:
                        nextc += 1
                if grid[r][nextc] == 0:
                    c = nextc
                else:
                    break
            if dir == 2:
                nextc = c - 1
                if nextc < 0 or grid[r][nextc] == 2: # look for first non-blank grid
                    nextc =  len(grid[r]) - 1
                    while grid[r][nextc] == 2:
                        nextc -= 1
                if grid[r][nextc] == 0:
                    c = nextc
                else:
                    break
            if dir == 1:
                nextr = r + 1
                if nextr >= len(grid) or grid[nextr][c] == 2: # look for first non-blank grid
                    nextr = 0
                    while grid[nextr][c] == 2:
                        nextr += 1
                if grid[nextr][c] == 0:
                    r = nextr
                else:
                    break
            if dir == 3:
                nextr = r - 1
                if nextr < 0 or grid[nextr][c] == 2: # look for first non-blank grid
                    nextr = len(grid) - 1
                    while grid[nextr][c] == 2:
                        nextr -= 1
                if grid[nextr][c] == 0:
                    r = nextr
                else:
                    break
    print(r,c, dir)

score = (r+1) * 1000 + (c+1) * 4 + dir
print(score)
# for r in grid:
#     print(r)

# print(cmds)