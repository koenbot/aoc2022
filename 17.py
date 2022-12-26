data = open("17.txt").read()

s1 = [[0, 2], [0, 3], [0, 4], [0, 5]]
s2 = [[0, 3], [1, 2], [1, 3], [1, 4], [2, 3]]
s3 = [[0, 2], [0, 3], [0, 4], [1, 4], [2, 4]]
s4 = [[0, 2], [1, 2], [2, 2], [3, 2]]
s5 = [[0, 2], [0, 3], [1, 2], [1, 3]]
shapes = [s1, s2, s3, s4, s5]

grid = [[1, 1, 1, 1, 1, 1, 1]]
maxh = 0

jet = 0

i = -1

prevmaxh = 0
previ = 0
first = True
stop = False

# for i in range(2022):
while True:
    i = i + 1
    rock = shapes[i % 5]

    # if i == 2022:
    if i == 1000000000000:
        print(maxh)
        exit()

    # appear
    r = maxh + 4
    c = 0

    # move and fall in steps
    while True:

        # print(r, c)
        # print(data[jet])
        # push - collision check
        if data[jet] == ">":
            allow = True
            for rr, cc in rock:
                if cc + c + 1 >= 7:
                    allow = False
                    break
                if r + rr < len(grid) and grid[r + rr][cc + c + 1] == 1:
                    allow = False
                    break
            if allow:
                c = c + 1
        else:
            allow = True
            for rr, cc in rock:
                if cc + c - 1 < 0:
                    allow = False
                    break
                if r + rr < len(grid) and grid[r + rr][cc + c - 1] == 1:
                    allow = False
                    break
            if allow:
                c = c - 1

        jet = (jet + 1) % len(data)
        if jet == 0:
            print(i, i % 5, jet, len(data), maxh, prevmaxh - maxh, previ - i)
            if not first and not stop:
                i = i + (1000000000000 // 1700 - 2) * 1700
                offset = (1000000000000 // 1700 - 2) * 2654
                print("OFFSET", offset)
                # maxh = maxh + (1000000000000 // 1700 - 2) * 2654
                stop = True
                # print(i, maxh)
                # exit()
            prevmaxh = maxh
            previ = i
            first = False

        # print(r, c)

        # fall - collision check
        allow = True
        for rr, cc in rock:
            if 0 <= rr + r - 1 < len(grid) and grid[rr + r - 1][cc + c] == 1:
                # print(rr, cc, "caused collision")
                allow = False
                break

        if allow:
            r = r - 1
            # print(r, c)

        else:
            # add rock to grid where it is
            # print("Adding at ", r, c)
            while r + 3 >= len(grid):
                grid.append([0, 0, 0, 0, 0, 0, 0])

            for rr, cc in rock:
                if rr + r > maxh:
                    maxh = rr + r
                grid[rr + r][cc + c] = 1

            # print("Done")
            # for row in reversed(grid):
            #     s = ""
            #     for col in row:
            #         if col == 0:
            #             s += "."
            #         else:
            #             s += "#"
            #     print(s)
            break

print(maxh)
