import collections

lines = open("23.txt").readlines()

pos = []  # list of tuples

for r, line in enumerate(lines):
    for c, let in enumerate(line):
        if let == "#":
            pos.append((r, c))
print(pos)
print(len(pos))
# exit()

# order = ["N", "S", "W", "E"]
order = ["N", "E", "S", "W"]

posset = set(pos)

k = 0
while True:
    k = k + 1
    
    newpos = {}
    counts = collections.defaultdict(int)

    for i, (r, c) in enumerate(pos):
        if (
            (r - 1, c - 1) not in posset
            and (r - 1, c) not in posset
            and (r - 1, c + 1) not in posset
            and (r, c - 1) not in posset
            and (r, c + 1) not in posset
            and (r + 1, c - 1) not in posset
            and (r + 1, c) not in posset
            and (r + 1, c + 1) not in posset
        ):
            continue

        for o in order:
            if o == "N":
                if (r - 1, c - 1) not in posset and (r - 1, c) not in posset and (r - 1, c + 1) not in posset:
                    newpos[i] = (r - 1, c)
                    counts[(r - 1, c)] += 1
                    break
            if o == "S":
                if (r + 1, c - 1) not in posset and (r + 1, c) not in posset and (r + 1, c + 1) not in posset:
                    newpos[i] = (r + 1, c)
                    counts[(r + 1, c)] += 1
                    break
            if o == "E":
                if (r - 1, c + 1) not in posset and (r, c + 1) not in posset and (r + 1, c + 1) not in posset:
                    newpos[i] = (r, c + 1)
                    counts[(r, c + 1)] += 1
                    break
            if o == "W":
                if (r - 1, c - 1) not in posset and (r, c - 1) not in posset and (r + 1, c - 1) not in posset:
                    newpos[i] = (r, c - 1)
                    counts[(r, c - 1)] += 1
                    break

        # print(newpos)
        # print(counts)

    if len(newpos) == 0:
        break

    # update pos when count is 1
    for elf, p in newpos.items():
        if counts[p] == 1:
            pos[elf] = p

    posset = set(pos)   

    # cycle order
    order = order[1:] + [order[0]]
    print(k, order, len(newpos))

print(k)
exit()

minr = maxr = pos[0][0]
minc = maxc = pos[0][1]

for r, c in pos:
    minr = min(r,minr)
    minc = min(c,minc)
    maxr = max(r,maxr)
    maxc = max(c,maxc)

print(minr,minc,maxr,maxc)

print(pos)

tiles = (maxr - minr + 1) * (maxc - minc + 1) - len(pos)
print(tiles)
