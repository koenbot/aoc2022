lines = open("22.txt").readlines()

grid = []
cmds = []

# n = 16
n = 150


def getface(row, col):
    if row < 50:
        if col < 100:
            return "A"
        return "B"
    if row < 100:
        return "C"
    if row < 150:
        if col < 50:
            return "E"
        return "D"
    return "F"

for rr, line in enumerate(lines):
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
    for cc, c in enumerate(line):
        if c == " ":
            row.append(2)
        if c == ".":
            row.append(getface(rr, cc))
        if c == "#":
            # row.append(getface(rr, cc))
            row.append(1)
    if len(row) < n:
        row = row + [2] * (n - len(row))
    grid.append(row)


r = 0
c = 50

# 0 = right, 1 = down, 2 = left, 3 = up
dir = 0

# for line in grid:
#     print("".join(map(str, line)))

import copy


grid2 = copy.deepcopy(grid)

def draw():
    for line in grid2:
        vis = []
        for let in line:
            if let == 2:
                vis.append(" ")
            elif let == 1:
                vis.append("#")
            elif let != "X":
                vis.append(".")
            else:
                vis.append(let)
        print("".join(vis))

focus = 0

# r = 5
# c = 110
# dir = 1
# cmds = [("step", 1000)]
for k, (a, b) in enumerate(cmds):
    # if k == focus + 1:
    #     exit()
    if a == "turn":
        if b == "R":
            dir = (dir + 1) % 4
        if b == "L":
            dir = (dir - 1) % 4
    if a == "step":
        if k == focus:
            draw()
            print(a, b, dir)
        for i in range(b):
            grid2[r][c] = "X"
            # print(i,b,r,c, dir)
            if dir == 0:
                nextc = c + 1
                nextr = r
                nextdir = dir
                if nextc >= len(grid[r]) or grid[nextr][nextc] == 2:
                    if grid[r][c] == "B":
                        nextc = 99
                        nextr = 149 - r
                        nextdir = 2
                    if grid[r][c] == "D":
                        nextc = 149
                        nextr = 149 - r
                        nextdir = 2
                    if grid[r][c] == "C":
                        nextc = r + 50
                        nextr = 49
                        nextdir = 3
                    if grid[r][c] == "F":
                        nextc = r - 100
                        nextr = 149
                        nextdir = 3
            elif dir == 2:
                nextc = c - 1
                nextr = r
                nextdir = dir
                if nextc < 0 or grid[nextr][nextc] == 2:
                    if grid[r][c] == "A":
                        nextc = 0
                        nextr = 149 - r
                        nextdir = 0
                    if grid[r][c] == "E":
                        nextc = 50
                        nextr = 149 - r
                        nextdir = 0
                    if grid[r][c] == "C":
                        nextc = r - 50
                        nextr = 100
                        nextdir = 1
                    if grid[r][c] == "F":
                        nextc = r - 100
                        nextr = 0
                        nextdir = 1
            elif dir == 1:
                nextc = c
                nextr = r + 1
                nextdir = dir
                if nextr >= len(grid) or grid[nextr][nextc] == 2:
                    if grid[r][c] == "B":
                        nextc = 99
                        nextr = c - 50
                        nextdir = 2
                    if grid[r][c] == "D":
                        nextc = 49
                        nextr = c + 100
                        nextdir = 2
                    if grid[r][c] == "F":
                        nextc = c + 100
                        nextr = 0
                        nextdir = 1
            elif dir == 3:
                nextc = c
                nextr = r - 1
                nextdir = dir
                if nextr < 0 or grid[nextr][nextc] == 2:
                    if grid[r][c] == "E":
                        nextc = 50
                        nextr = c + 50
                        nextdir = 0
                    if grid[r][c] == "B":
                        nextc = c - 100
                        nextr = 199
                        nextdir = 3
                    if grid[r][c] == "A":
                        nextc = 0
                        nextr = c + 100
                        nextdir = 0

            if grid[nextr][nextc] != 1:
                c = nextc
                r = nextr
                dir = nextdir
            else:
                break
        
        if k == focus:
            draw()
    # print(r,c, dir)
    # if r < 0 or c < 0:
    #     exit()


print(dir)
score = (r+1) * 1000 + (c+1) * 4 + dir
print(score)
