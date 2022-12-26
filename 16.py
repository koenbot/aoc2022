import re
import collections

lines = list(map(str.strip, open("16.txt").readlines()))

flow = {}
dist = collections.defaultdict(dict)

for line in lines:
    m = re.match(r"Valve (.*) has flow rate=(\d*); tunnel[s]? lead[s]? to valve[s]? (.*)", line)
    name, rate, nexts = m.groups()
    nexts = list(map(str.strip, nexts.split(",")))

    flow[name] = int(rate)

    for target in nexts:
        dist[name][target] = 1

# determine dist
for s in flow:
    for t in flow:
        if t not in dist[s] and t != s:
            dist[s][t] = 99

for i in range(len(flow)):
    for s in flow:
        for t in flow:
            if s == t:
                continue
            for u in flow:
                if u == s or u == t:
                    continue
                dist[s][t] = min(dist[s][t], dist[s][u] + dist[u][t])

# remove valves with zero flow
dist2 = {}
for s in flow:
    # if flow[s] == 0:
    #     continue
    dist2[s] = {k: v for k,v in dist[s].items() if flow[k] > 0}

for k, v in dist2.items():
    print(k, v)

# bfs or so

states = collections.deque()
states.append(["AA", 30, 0, 0, []]) # position, time left, flow rate, flow accumulated, visits

best = 0
i = 0

while len(states):
    # print(i, states)
    i += 1
    if i % 10000 == 0:
        print(i, len(states))
    pos, tim, rate, acc, visits = states.popleft()
    # print(i, pos, tim, rate, acc, visits)
    # if i == 10:
    #     exit()

    if len(dist2[pos]) + 1 == len(visits): # nothing more to visit, so just wait here
        bestacc = acc + rate * (tim - 1)
        if bestacc > best:
            best = bestacc
            print(i, len(states), pos, tim, rate, acc, best)
        continue

    for k, v in dist2[pos].items():
        # if pos == "AA" and k != "DD":
        #     continue
        # if pos == "DD" and k != "BB":
        #     continue
        # if pos == "BB" and k != "JJ":
        #     continue
        # if pos == "JJ" and k != "HH":
        #     continue
        # if pos == "HH" and k != "EE":
        #     continue
        # if pos == "EE" and k != "CC":
        #     continue
        
        # print(k, visits)
        # print(acc)
        if k in visits:
            continue
        if tim - v - 1 < 0:
            bestacc = acc + rate * (tim - 1)
            if bestacc > best:
                best = bestacc
                print(i, len(states), pos, tim, rate, acc, best)
            continue
        visit = visits.copy()
        visit.append(k)
        states.append([k, tim - v - 1, rate + flow[k], acc + rate * (v + 1) + flow[k], visit])
    # print(pos, tim, flow, acc)

print(best)

# for k in dist["AA"]:
# list(.keys())



# print(flow)
# print(dist)
# print(dist2)


