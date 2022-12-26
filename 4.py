from typing import overload


lines = open("4.txt").readlines()

contains = 0
overlap = 0

for line in lines:
    a, b = line.split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    print(a1, b2)

    if a1 >= b1 and a2 <= b2:
        contains += 1
    elif b1 >= a1 and b2 <= a2:
        contains += 1

    if a1 >= b1 and a1 <= b2:
        overlap += 1
    elif a2 >= b1 and a2 <= b2:
        overlap += 1
    elif b1 >= a1 and b1 <= a2:
        overlap += 1
    elif b2 >= a1 and b2 <= a2:
        overlap += 1

print(contains)
print(overlap)