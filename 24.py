import collections

lines = open("24.txt").readlines()

bliz = []  # list of (r, c, dir) - 0 = up, 1 = right, 2 = down, 3 = left

for r, line in enumerate(lines[1:-1]):
    for c, el in enumerate(line[1:-2]):
        if el == ".":
            continue
        dir = 0
        if el == ">":
            dir = 1
        if el == "v":
            dir = 2
        if el == "<":
            dir = 3
        bliz.append([r, c, dir])

h = len(lines) - 2
w = len(lines[0]) - 3

print(h, w)

# bfs so we don't need to remember state
# print(bliz)

print(sorted(bliz))

day = 0
check = set([(-1, 0)])
taken = set()

phase = 0

done = False
while not done:
    day += 1
    print("DAY", day)
    # if day == 10:
    #     break

    # first update bliz
    taken.clear()
    for i in range(len(bliz)):
        if bliz[i][2] == 0:
            bliz[i][0] = (bliz[i][0] - 1) % h
        if bliz[i][2] == 1:
            bliz[i][1] = (bliz[i][1] + 1) % w
        if bliz[i][2] == 2:
            bliz[i][0] = (bliz[i][0] + 1) % h
        if bliz[i][2] == 3:
            bliz[i][1] = (bliz[i][1] - 1) % w

        taken.add((bliz[i][0], bliz[i][1]))

    # find open spots to go to for each check
    # print(len(check), len(taken))
    # print(check)
    # print(sorted(bliz))
    # print(taken)

    newcheck = set()
    for r, c in check:
        if r == h - 1 and c == w - 1:
            if phase == 2:
                print("PHASE 2 DONE!")
                done = True
                break
            if phase == 0:
                print("PHASE 0 DONE!")
                phase = 1
                newcheck = set([(h, w - 1)])
                break

        if r == 0 and c == 0 and phase == 1:
            print("PHASE 1 DONE!")
            newcheck = set([(-1, 0)])
            phase = 2
            break

        if r == -1 and c == 0:  # wait at start
            newcheck.add((-1, 0))
            if (0, 0) not in taken:
                newcheck.add((0, 0))
            continue

        if r == h and c == w - 1:  # wait at end
            newcheck.add((h, w - 1))
            if (h - 1, w - 1) not in taken:
                newcheck.add((h - 1, w - 1))
            continue

        if (r, c) not in taken:
            newcheck.add((r, c))
        if r + 1 < h and (r + 1, c) not in taken:
            newcheck.add((r + 1, c))
        if r - 1 >= 0 and (r - 1, c) not in taken:
            newcheck.add((r - 1, c))
        if c + 1 < w and (r, c + 1) not in taken:
            newcheck.add((r, c + 1))
        if c - 1 >= 0 and (r, c - 1) not in taken:
            newcheck.add((r, c - 1))

    check = newcheck
    # print(check)
