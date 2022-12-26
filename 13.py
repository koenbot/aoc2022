import json
import functools

def compare(x, y):
    # print(x, y)
    if type(x) == int and type(y) == int:
        if x < y:
            return -1
        if x == y:
            return 0
        return 1
    if type(x) == int:
        return compare([x], y)
    if type(y) == int:
        return compare(x, [y])

    l = max(len(x), len(y))
    for k in range(l):
        if k >= len(x):
            # print("X RAN OUT, -1")
            return -1
        if k >= len(y):
            # print("Y RAN OUT, 1")
            return 1
        c = compare(x[k], y[k])
        # print(k, c)
        if c == 0:
            continue
        return c
    return 0
    # print("HUUUH")
    # exit()

lines = list(map(str.strip, open("13.txt").readlines()))

# sum = 0

# for i in range(0, len(lines), 3):
#     a = json.loads(lines[i])
#     b = json.loads(lines[i+1])
#     ok = compare(a,b)
#     print("GLOBAL", ok)
#     print()

#     if ok == -1:
#         print((i // 3) + 1)
#         sum += (i // 3) + 1

# print(sum)


els = [json.loads(line) for line in lines if line]
print(els)
els.append([[2]])
els.append([[6]])
els.sort(key=functools.cmp_to_key(compare))
k1 = 0
k2 = 0
for i, x in enumerate(els):
    print(x)
    if x == [[2]]:
        k1 = i + 1
    if x == [[6]]:
        k2 = i + 1
print(k1 * k2)