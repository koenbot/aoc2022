lines = map(str.strip, open("9.txt").readlines())

commands = []
for line in lines:
    d, l = line.split(" ")
    l = int(l)
    commands.append([d, l])

wmax = 0
wmin = 0
hmax = 0
hmin = 0
x = 0
y = 0

rx = 0
ry = 0

tails = set()
tails.add((rx,ry))

for d, l in commands:
    # move the head
    if d == "U":
        y = y - l
        if y < hmin:
            hmin = y
    if d == "D":
        y = y + l
        if y > hmax:
            hmax = y
    if d == "L":
        x = x - l
        if x < wmin:
            xmin = x
    if d == "R":
        x = x + l
        if x > wmax:
            wmax = y

    # move the tail
    if abs(x-rx) <= 1 and abs(y-ry) <= 1: # still touching
        continue

    if x > rx + 1:
        for k in range(rx+1,x):
            tails.add((k,y))
        rx = x - 1
        ry = y
    elif x < rx - 1:
        for k in range(rx-1,x,-1):
            tails.add((k,y))
        rx = x + 1
        ry = y
    elif y > ry + 1:
        for k in range(ry+1,y):
            tails.add((x,k))
        rx = x
        ry = y - 1
    elif y < ry - 1:
        for k in range(ry-1,y,-1):
            tails.add((x,k))
        rx = x
        ry = y + 1

    # print(x,y)
    # print()

print(tails)
print(len(tails))

# w = wmax - wmin + 1
# h = hmax - hmin + 1
# print(w, h)
# print(commands)

