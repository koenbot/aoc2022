import collections

heights = list(map(str.strip, open("12.txt").readlines()))
heights = [list(map(lambda x: ord(x) - ord('a'), line)) for line in heights]
print(heights)

w = len(heights[0])
h = len(heights)

# find start and end
startr = -1
startc = -1
for r in range(h):
    for c in range(w):
        if heights[r][c] == ord('E') - ord('a'):
            startr = r
            startc = c
            heights[r][c] = 25


# dijkstra
dists = []
for r in range(h):
    dists.append([9999] * w)
print(dists)

t = (startr, startc, 0)
checks = collections.deque([t])
visited = set()

while True:
    # print(checks)
    if len(checks) == 0:
        break
    r, c, dist = checks.popleft()
    val = heights[r][c]

    if dist >= dists[r][c]:
        continue
    
    dists[r][c] = dist

    if val == 0:
        print(dist)
        break

    # add options to checks
    if r > 0 and heights[r-1][c] >= val - 1:
        checks.append((r-1,c,dist+1))
    if r < h-1 and heights[r+1][c] >= val - 1:
        checks.append((r+1,c,dist+1))
    if c > 0 and heights[r][c-1] >= val - 1:
        checks.append((r,c-1,dist+1))
    if c < w-1 and heights[r][c+1] >= val - 1:
        checks.append((r,c+1,dist+1))

    # print("HI")
    # print(checks)

