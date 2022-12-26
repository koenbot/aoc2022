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
    if flow[k]> 0:
        print(k, len(v))

valves = [k for k in flow if flow[k] > 0]
print(valves)

print(flow)
floworder = sorted([(k, v) for k,v in flow.items() if v > 0], key=lambda x: -x[1])

# exit()
# bfs or so

states = collections.deque()
states.append([("AA", "AA", 0, 0), 0, [], 0]) # pos1, pos2, time1, time2, flow tot, visits, score
# states.append([("AA", "AA", 0, 0), 0, [], 0, ["AA"]]) # pos1, pos2, time1, time2, flow tot, visits, score, path

# topscores = collections.defaultdict(int)
# topscores[("AA", "AA", 0, 0)] = 0

end = 26

# best = 2654
best = 0
i = 0


while len(states):
    i += 1
    if i % 10000 == 0:
        print(i, len(states), best)
    (pos1, pos2, tim1, tim2), flowrate, visits, score = states.pop() # right, not left, dfs not bfs

    # try to prune: if top achievable score is less than best, makes no sense to continue
    
    maxbest = score
    for v in valves:
        if v in visits:
            continue
        maxbest += (end - (min(tim1, tim2) + 1)) * flow[v]

    if maxbest < best:
        # print("PRUNING")
        continue


    if tim1 <= tim2:
        # for k, v in dist2[pos1].items():
        for k, stream in floworder:
            if k in visits or k == pos1:
                continue
            v = dist2[pos1][k]
            if tim1 + v + 1 > end:
                continue

            newscore = score + (end - (tim1 + v + 1)) * flow[k]
            idx = (k, pos2, tim1 + v + 1, tim2)
            if newscore > best:
                best = newscore
                print(best)
            visited = [*visits, k]
            states.append([idx, flowrate + flow[k], visited, newscore])
    else:
        # for k, v in dist2[pos2].items():
        for k, stream in floworder:
            if k in visits or k == pos2:
                continue
            v = dist2[pos2][k]
            if tim2 + v + 1 > end:
                continue

            newscore = score + (end - (tim2 + v + 1)) * flow[k]
            idx = (pos1, k, tim1, tim2 + v + 1)
            if newscore > best:
                best = newscore
                print(best)
            visited = [*visits, k]
            states.append([idx, flowrate + flow[k], visited, newscore])


print(best)
