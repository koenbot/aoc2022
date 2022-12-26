lines = list(map(str.strip, open("14.txt").readlines()))

rocks = set()

maxr = 0
minc = 0
maxc = 0

for line in lines:
    prev = False
    for pt in map(str.strip, line.split("->")):
        c, r = map(int, pt.split(","))
        print(c,r)
        if r > maxr:
            maxr = r
        if c < minc:
            minc = c
        if c > maxc:
            maxc = c

        if prev:
            c0, r0 = prev
            if c0 == c and r0 <= r:
                for k in range(r0, r + 1):
                    rocks.add((k,c))
            if c0 == c and r0 > r:
                for k in range(r, r0 + 1):
                    rocks.add((k,c))
            if r0 == r and c0 <= c:
                for k in range(c0, c + 1):
                    rocks.add((r,k))
            if r0 == r and c0 > c:
                for k in range(c, c0 + 1):
                    rocks.add((r,k))

        prev = (c,r)

# for i in range(minc - 100, maxc + 100):
#     rocks.add((maxr + 2, i))

print(sorted(rocks))
print(maxr)
adds = 0
done = False

while not done:
    print(adds)
    c, r = 500, 0
    while True:
        # print(r,c)
        # if r > maxr:
        #     done = True
        #     break
        if r == maxr + 2:
            rocks.add((r, c))
            break
        if (0, 500) in rocks:
            done = True
            break
        if (r + 1, c) not in rocks:
            r = r + 1
            continue
        if (r + 1, c-1) not in rocks:
            c = c - 1
            r = r + 1
            continue
        if (r + 1, c+1) not in rocks:
            c = c + 1
            r = r + 1
            continue
        # print("Adding",c,r)
        rocks.add((r, c))
        adds += 1
        break

print(adds)
