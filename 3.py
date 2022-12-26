
lines = open("3.txt").readlines()

lines = list(map(str.strip, lines))
sum = 0
for line in lines:
    n = len(line) // 2
    a = set(line[:n])
    b = set(line[n:])
    c = a.intersection(b)
    cc = list(c)[0]
    v = ord(cc)
    if cc > 'a':
        v = v - ord('a') + 1
    else:
        v = v - ord("A") + 27
    print(c, v)
    sum += v
print(sum)

sum = 0
for i in range(0, len(lines), 3):
    a = set(lines[i])
    b = set(lines[i+1])
    c = set(lines[i+2])
    d = a.intersection(b).intersection(c)
    print(d)
    cc = list(d)[0]
    v = ord(cc)
    if cc > 'a':
        v = v - ord('a') + 1
    else:
        v = v - ord("A") + 27
    print(cc, v)
    sum += v
print(sum)