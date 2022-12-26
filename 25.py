def to_num(s):
    l = len(s) - 1
    t = 0
    for e in s:
        k = -3
        if e == "=":
            k = -2
        elif e == "-":
            k = -1
        else:
            k = int(e)
        t += (5**l) * k
        l = l - 1
    return t


def from_num_binary_search(n):
    c = ["2", "1", "0", "-", "="]

    l = 1
    while to_num(c[0] * l) < n:
        l += 1

    s = ""
    if to_num("1" + c[4] * (l - 1)) <= n <= to_num("1" + c[0] * (l - 1)):
        s = "1"
    else:
        s = "2"

    e = l - 1
    # n = n - int(s) * 5**e

    while e > 0:
        e = e - 1
        for i in range(len(c)):
            lo_s = s + c[i] + c[4] * e
            hi_s = s + c[i] + c[0] * e
            lo = to_num(lo_s)
            hi = to_num(hi_s)
            print(e, i, lo_s, hi_s, lo, hi, n)
            if lo <= n <= hi:
                s = s + c[i]
                # n = n - (i - 2) * (5 ** e)
                break
    print(s)
    return s




    print(n)

    e = l - 2
    while n != 0 and e >= 0:
        k = 5 **e
        print(e, k, n, s)
        if n <= -2 * k:
            s += "="
            n = n + 2 * k
        elif n <= k:
            s += "-"
            n = n + 1 * k
        elif n <= 1 * k:
            s += "0"
        elif n <= 2 * k:
            s += "1"
            n = n - 1 * k
        elif n <= 3 * k:
            s += "2"
            n = n - 2 * k
        e = e - 1

    print(s, to_num(s))
    return s


def from_num(n):
    s = ""
    l = 0
    while 5**l < n:
        l += 1
    l = l - 1
    print(l, 5**l)

    # first is 1 or 2
    r = n // (5**l)
    s += str(r)
    print(r)
    n = n - 5**l * r
    print(n)

    return 0


lines = map(str.strip, open("25.txt").readlines())

k = to_num("1=-0-2")
s = from_num_binary_search(k)
print(k, s)

tot = 0
for line in lines:
    k = to_num(line)
    print(line, k)
    tot += k
print(tot)


s = from_num_binary_search(tot)
print(tot, s)
