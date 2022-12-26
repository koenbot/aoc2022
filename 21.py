lines = map(str.strip, open("21.txt").readlines())

monkeys = {}

for line in lines:
    name = line[:4]
    op = line[6:]
    if len(op) <= 6:
        op = int(op)
    monkeys[name] = op


def get(key):
    op = monkeys[key]
    if type(op) == int:
        return op

    # print(op)
    x = op[:4]
    cmd = op[5]
    y = op[7:]


    if x == "humn" or y == "humn":
        return False

    xx = get(x)
    yy = get(y)

    if key == "root":
        print(xx, yy)

    if type(xx) == bool and xx == False:
        return False
    if type(yy) == bool and yy == False:
        return False

    if cmd == "+":
        val = xx + yy
    if cmd == "-":
        val = xx - yy
    if cmd == "*":
        val = xx * yy
    if cmd == "/":
        val = xx // yy

    monkeys[key] = val
    return val

for k in monkeys:
    get(k)

for k, v in monkeys.items():
    if type(v) != int:
        print(k, v)

monkeys["humn"] = "HUMN"

# reverse instructions

def chain(key, val):
    op = monkeys[key]

    if type(op) == int:
        return op

    x = op[:4]
    cmd = op[5]
    y = op[7:]


    if key == "root":
        cmd = "="

    xx = monkeys[x]
    yy = monkeys[y]

    
    if type(xx) == int:
        print(key, "=", x, cmd, y, "AKA", val, "=", xx, cmd, y)
    if type(yy) == int:
        print(key, "=", x, cmd, y, "AKA", val, "=", x, cmd, yy)

    if type(xx) != int and type(yy) != int:
        print("CRAPPPPP")

    if cmd == "=":
        if type(xx) == int:
            return y, xx
        if type(yy) == int:
            return x, yy
    if cmd == "+":
        if type(xx) == int:
            return y, val - xx
        if type(yy) == int:
            return x, val - yy
    if cmd == "-":
        if type(xx) == int:
            return y, xx - val
        if type(yy) == int:
            return x, val + yy
    if cmd == "*":
        if type(xx) == int:
            return y, val // xx
        if type(yy) == int:
            return x, val // yy
    if cmd == "/":
        if type(xx) == int:
            return y, val * xx
        if type(yy) == int:
            return x, val * yy


key = "root"
val = None
while True:
    key, val = chain(key, val)
    print(key, val)
