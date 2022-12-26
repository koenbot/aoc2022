lines = map(str.strip, open("10.txt").readlines())

reg0 = 1
clock =  0
signal = 0
checks = [20,60,100,140,180,220]

crt = []

for line in lines:
    if line == "noop":
        clock += 1
        if clock in checks:
            print(clock, reg0)
            signal += clock * reg0
        if abs(clock - reg0) <= 1:
            crt.append("#")
        else:
            crt.append(".")
    else:
        val = int(line.split(" ")[1])
        # print(val)
        clock += 1
        if clock in checks:
            print(clock, reg0)
            signal += clock * reg0
        if abs(clock - reg0) <= 1:
            crt.append("#")
        else:
            crt.append(".")
        clock += 1
        if clock in checks:
            print(clock, reg0)
            signal += clock * reg0
        reg0 += val
        if abs(clock - reg0) <= 1:
            crt.append("#")
        else:
            crt.append(".")
    clock = clock % 40

print(signal)
for i in range(0, len(crt), 40):
    print(crt[i:i+40])