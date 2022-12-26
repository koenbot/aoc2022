lines = open("5.txt").readlines()

stacks = []
for i in range(9):
    stacks.append([])
print(stacks)
moves = []

for line in lines:
    if "[" in line:
        for i in range(9):
            value = line[i*4 + 1]
            if value != " ":
                stacks[i].append(value)

    if "from" in line:
        a, b = line.split("from")
        amount = int(a[5:])
        frm = int(b[1]) - 1
        to = int(b[6]) - 1
        moves.append([amount, frm, to])

for i in range(9):
    stacks[i] = list(reversed(stacks[i]))

print(stacks)

for amount, frm, to in moves:
    print(amount, frm, to)
    print(stacks)
    boxes = stacks[frm][-amount:]
    # print(boxes)
    stacks[frm] = stacks[frm][:-amount]
    stacks[to] = [*stacks[to], *boxes]
    # stacks[to] = [*stacks[to], *list(reversed(boxes))]

    # print(stacks[to])
    # exit()

s = "".join(stack[-1] for stack in stacks)
print(s)