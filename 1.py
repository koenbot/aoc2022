f = open("1.txt")
lines = f.readlines()

sums = []
sum = 0
for line in lines:
    if line == "\n":
        sums.append(sum)
        sum = 0
        continue
    sum += int(line)
sums.append(sum)

sums = sorted(sums, reverse=True)
print(sums)

print(sums[0] + sums[1] + sums[2])
