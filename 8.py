lines = map(str.strip, open("8.txt").readlines())
grid = []
visible = []
for line in lines:
    grid.append([int(a) for a in line])
    visible.append([0] * len(line))
print(grid)

h = len(grid)
w = len(grid[0])
print(h, w)

for i in range(h):
    top = -1
    for j in range(w):
        if grid[i][j] > top:
            top = grid[i][j]
            visible[i][j] = 1

for i in range(h):
    top = -1
    for j in range(w-1, -1, -1):
        if grid[i][j] > top:
            top = grid[i][j]
            visible[i][j] = 1

for j in range(w):
    top = -1
    for i in range(h):
        if grid[i][j] > top:
            top = grid[i][j]
            visible[i][j] = 1


for j in range(w):
    top = -1
    for i in range(h-1, -1, -1):
        if grid[i][j] > top:
            top = grid[i][j]
            visible[i][j] = 1

# for i in range()
print(visible)
print(sum(map(sum, visible)))

maxscore = 0
for i in range(h):
    for j in range(w):
        me = grid[i][j]
        up = 0
        for k in range(i-1, -1, -1):
            up += 1
            if grid[k][j] >= me:
                break
        down = 0
        for k in range(i+1, h):
            down += 1
            if grid[k][j] >= me:
                break
            
        left = 0
        for k in range(j-1, -1, -1):
            left += 1
            if grid[i][k] >= me:
                break

        right = 0
        for k in range(j+1, w):
            right += 1
            if grid[i][k] >= me:
                break

        
        score = up * down * left * right
        print(i,j,up,down,left,right, score)
        if score > maxscore:
            maxscore = score
print(maxscore)
