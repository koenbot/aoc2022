import re
import collections
import math

# o = ore
# c = clay
# b = obsidian
# g = geo


# IT DIDN'T WORK BECAUSE I DIDN'T ****** READ PROPERLY
# I CAN ONLY MAKE 1 BOT AT A TIME. NOT HOWEVER MANY BOTS AT ONCE.
# THIS ~vastly~ SIMPLIFIES THINGS

def run(coo, cco, cbo, cbc, cgo, cgb):

    # day ,ore, clay, obsidian, geode, orebot, claybot, obsidianbot, geodebot
    start = [1, 0, 0, 0, 0, 1, 0, 0, 0]
    check = collections.deque([start])

    maxgeo = 0

    counter = 0


    maxo = max(coo, cco, cbo, cgo)

    memo = set()

    while len(check) > 0:
        # print(len(check))
        cur = check.pop()
        day, o, c, b, g, ob, cb, bb, gb = cur
        # print(day, o, c, b, g, ob, cb, bb, gb)


        if tuple(cur) in memo:
            # print("SEEN")
            continue

        memo.add(tuple(cur))

        counter += 1
        if counter % 100000 == 0:
            print(counter, len(check), maxgeo)


        remain = 32 - day + 1
        attain = g + remain * gb + remain * (remain + 1) / 2
        if attain <= maxgeo: # purge, never reachable
            continue

        if day == 32:
            g += gb
            if g > maxgeo:
                print(o, c, b, g, ob, cb, bb, gb)
                maxgeo = g
            continue

        # next state is actually building a bot, waiting as long as it takes
        
        # ore
        # if ob < maxo:
        #     wait = max(1, math.ceil((coo - o) / ob))
        #     if day + wait <= 24:
        #         check.append([day + wait, o + ob * wait - coo, c + cb * wait, b + bb * wait, g + gb * wait, ob + 1, cb, bb, gb])


        # # clay
        # if cb < cbc:
        #     wait = max(1, math.ceil((cco - o) / ob))
        #     if day + wait <= 24:
        #         check.append([day + wait, o + ob * wait - cco, c + cb * wait, b + bb * wait, g + gb * wait, ob, cb + 1, bb, gb])
        #         print(cur)
        #         print(check[-1])
        #         print()
        # # # obs
        # if cb > 0 and bb < cgb:
        #     wait = max(1, math.ceil((cbc - c) / cb), math.ceil((cbo - o) / ob))
        #     if day + wait <= 24:
        #         check.append([day + wait, o + ob * wait - cbo, c + cb * wait - cbc, b + bb * wait, g + gb * wait, ob, cb, bb + 1, gb])

        # # # geo
        # if bb > 0:
        #     wait = max(1, math.ceil((cgb - b) / bb), math.ceil((cgo - o) / ob))
        #     if day + wait <= 24:
        #         check.append([day + wait, o + ob * wait - cgo, c + cb * wait, b + bb * wait - cgb, g + gb * wait, ob, cb, bb, gb + 1])

        d = day + 1

        check.append([d, o + ob, c + cb, b + bb, g + gb, ob, cb, bb, gb])

        if b >= cgb and o >= cgo:
            check.append([d, o + ob - cgo, c + cb, b + bb - cgb, g + gb, ob, cb, bb, gb + 1])
        if c >= cbc and o >= cbo and bb < cgb:
            check.append([d, o + ob - cbo, c + cb - cbc, b + bb, g + gb, ob, cb, bb + 1, gb])
        if o >= cco and cb < cbc:
            check.append([d, o + ob - cco, c + cb, b + bb, g + gb, ob, cb + 1, bb, gb])
        if o >= coo and ob < maxo:
            check.append([d, o + ob - coo, c + cb, b + bb, g + gb, ob + 1, cb, bb, gb])
        # no-op

    return maxgeo


lines = list(map(str.strip, open("19.txt").readlines()))

sum = 0
prod = 1
for line in lines[:3]:
    m = re.match(
        r"Blueprint (\d*): Each ore robot costs (\d*) ore. Each clay robot costs (\d*) ore. Each obsidian robot costs (\d*) ore and (\d*) clay. Each geode robot costs (\d*) ore and (\d*) obsidian.",
        line,
    )
    id, coo, cco, cbo, cbc, cgo, cgb = map(int, m.groups())
    # print(id, coo, cco, cbo, cbc, cgo, cgb)
    # best = run(4,2,3,14,2,7)
    # best = run(2, 3, 3, 8, 3, 12)
    best = run(coo, cco, cbo, cbc, cgo, cgb)
    print(id, best)
    # exit()
    sum += id * best
    prod = prod * best
print(sum)
print(prod)