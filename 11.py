import json
import math

monkeys = json.load(open("11.txt"))
print(monkeys)
for monkey in monkeys:
    monkey.append(0) # inspection counter

divs = [monkeys[monkey][2] for monkey in range(len(monkeys))]
modulo = math.prod(divs)
print(modulo)

for round in range(10000):
    print(round)
    for monkey in range(len(monkeys)):
        for old in monkeys[monkey][0]:
            cmd = monkeys[monkey][1]
            new = 0
            # print(old)
            exec(cmd)
            # new = new // 3
            # print(new)
            new = new % modulo
            if new % monkeys[monkey][2] == 0:
                newmonkey = monkeys[monkey][3][0]
            else:
                newmonkey = monkeys[monkey][3][1]
            monkeys[newmonkey][0].append(new)
        monkeys[monkey][4] += len(monkeys[monkey][0])
        monkeys[monkey][0] = []

print(monkeys)
insp = list(reversed(sorted([monkeys[monkey][4] for monkey in range(len(monkeys))])))
print(insp[0] * insp[1])

