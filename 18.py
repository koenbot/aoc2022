coords = []
for line in open("18.txt").readlines():
    x, y, z = map(int, line.split(","))
    coords.append([x, y, z])

sides = 0
for c1 in coords:
    open = 6

    for c2 in coords:
        if c1 == c2:
            continue
        if c1[0] == c2[0] and c1[1] == c2[1] and abs(c1[2] - c2[2]) == 1:
            open -= 1
        if c1[0] == c2[0] and c1[2] == c2[2] and abs(c1[1] - c2[1]) == 1:
            open -= 1
        if c1[1] == c2[1] and c1[2] == c2[2] and abs(c1[0] - c2[0]) == 1:
            open -= 1
    sides += open

print(sides)

minx = maxx = coords[0][0]
miny = maxy = coords[0][1]
minz = maxz = coords[0][2]

for x, y, z in coords:
    minx = min(x, minx)
    miny = min(y, miny)
    minz = min(z, minz)
    maxx = max(x, maxx)
    maxy = max(y, maxy)
    maxz = max(z, maxz)

print(minx, maxx)
print(miny, maxy)
print(minz, maxz)

# flood fill in cube

dirs = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
flood = [[minx, miny, minz]]

for x, y, z in flood:
    for d in dirs:
        xx = x + d[0]
        yy = y + d[1]
        zz = z + d[2]
        if (
            minx - 1 <= xx <= maxx + 1
            and miny - 1 <= yy <= maxy + 1
            and minz - 1 <= zz <= maxz + 1
        ):
            p = [xx, yy, zz]
            if p in flood or p in coords:
                continue
            flood.append(p)

print(len(flood))


sides = 0
for c1 in coords:

    for c2 in flood:
        if c1 == c2:
            print("HUUUH")
            continue
        if c1[0] == c2[0] and c1[1] == c2[1] and abs(c1[2] - c2[2]) == 1:
            sides += 1
        if c1[0] == c2[0] and c1[2] == c2[2] and abs(c1[1] - c2[1]) == 1:
            sides += 1
        if c1[1] == c2[1] and c1[2] == c2[2] and abs(c1[0] - c2[0]) == 1:
            sides += 1

print(sides)
