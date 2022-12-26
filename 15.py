import re

lines = list(map(str.strip, open("15.txt").readlines()))

circs = []

for line in lines:
    m = re.search(r"x=([-\d]*), y=([-\d]*).*x=([-\d]*), y=([-\d]*)", line)
    x0, y0, x1, y1 = map(int, m.groups())
    r = abs(x1 - x0) + abs(y1 - y0)
    circs.append([x0, y0, r])

# 3355220 [[-158295, 3299358], [3299360, 4399268]]

print(3355220 + 3299359 * 4000000)
exit()
# r = 10
# r = 2000000
for r in range(0, 4000000):
    if r % 10000 == 0:
        print(r)

    intvs = []

    for c0, r0, rad in circs:
        # print(r0, c0, rad)
        w = abs(r - r0)
        lr = rad - w
        if lr <= 0:
            continue
        lo = c0 - lr
        hi = c0 + lr
        # print(lo, hi)
        intvs.append([lo, hi])

    # print(intvs)
        # print(lo, hi)


    # merge intervals
    # intvs.sort()
    # print(intvs)

    out = []
    for i in sorted(intvs):
        if out and i[0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], i[1])
        else:
            out += i,

    if len(out) > 1:
        print(r, out)
# l = 0
# for i in out:
#     l += i[1] - i[0]
# print(l)