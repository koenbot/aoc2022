text = open("6.txt").read()

markers = 0
n = 14

for i in range(len(text) - n):
    packet = set(text[i:i+n])
    if len(packet) == n:
        print(i + n)
        markers += 1
        break

print(markers)
