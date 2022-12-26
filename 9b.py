lines = map(str.strip, open("9.txt").readlines())

commands = []
for line in lines:
    d, l = line.split(" ")
    commands += [d] * int(l)

print(commands)

pos = [[0,0] for i in range(10)]
print(pos)
tails = set()

def move(a, b):
    # move pos2 towards pos1 so that they touch
    if abs(a[0]-b[0]) <= 1 and abs(a[1]-b[1]) <= 1: # still touching
        return b

    if abs(a[0]-b[0]) >= 3 or abs(a[1]-b[1]) >= 3:
        print(a[0]-b[0],a[1]-b[1])

    if a[0] > b[0] + 1 and a[1] > b[1] + 1:
        b[0] = a[0] - 1
        b[1] = a[1] - 1
    elif a[0] < b[0] - 1 and a[1] > b[1] + 1:
        b[0] = a[0] + 1
        b[1] = a[1] - 1
    elif a[0] > b[0] + 1 and a[1] < b[1] - 1:
        b[0] = a[0] - 1
        b[1] = a[1] + 1
    elif a[0] < b[0] - 1 and a[1] < b[1] - 1:
        b[0] = a[0] + 1
        b[1] = a[1] + 1
    elif a[0] > b[0] + 1:
        b[0] = a[0] - 1
        b[1] = a[1]
    elif a[0] < b[0] - 1:
        b[0] = a[0] + 1
        b[1] = a[1]
    elif a[1] > b[1] + 1:
        b[0] = a[0]
        b[1] = a[1] - 1
    elif a[1] < b[1] - 1:
        b[0] = a[0]
        b[1] = a[1] + 1
    return b

for c in commands:
    if c == "U":
        pos[0][1] -= 1
    if c == "D":
        pos[0][1] += 1
    if c == "L":
        pos[0][0] -= 1
    if c == "R":
        pos[0][0] += 1


    for i in range(9):
        pos[i+1] = move(pos[i], pos[i+1])

    # print(pos[9])
    tails.add(tuple(pos[-1]))

# print(tails)
print(len(tails))
print((0,0) in tails)

# x = 0
# y = 0

# rx = 0
# ry = 0

# tails = set()
# tails.add((rx,ry))

# for d, l in commands:
#     # move the head
#     if d == "U":
#         y = y - l
#         if y < hmin:
#             hmin = y
#     if d == "D":
#         y = y + l
#         if y > hmax:
#             hmax = y
#     if d == "L":
#         x = x - l
#         if x < wmin:
#             xmin = x
#     if d == "R":
#         x = x + l
#         if x > wmax:
#             wmax = y

#     # move the tail
#     if abs(x-rx) <= 1 and abs(y-ry) <= 1: # still touching
#         continue

#     if x > rx + 1:
#         for k in range(rx+1,x):
#             tails.add((k,y))
#         rx = x - 1
#         ry = y
#     elif x < rx - 1:
#         for k in range(rx-1,x,-1):
#             tails.add((k,y))
#         rx = x + 1
#         ry = y
#     elif y > ry + 1:
#         for k in range(ry+1,y):
#             tails.add((x,k))
#         rx = x
#         ry = y - 1
#     elif y < ry - 1:
#         for k in range(ry-1,y,-1):
#             tails.add((x,k))
#         rx = x
#         ry = y + 1

#     # print(x,y)
#     # print()

# print(tails)
# print(len(tails))

# # w = wmax - wmin + 1
# # h = hmax - hmin + 1
# # print(w, h)
# # print(commands)

