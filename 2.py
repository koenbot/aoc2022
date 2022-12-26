lines = open("2.txt").readlines()
score = 0
for line in lines:
    elf, me = line.split()
    me = chr(ord(me) - ord('X') + ord('A'))
    s = elf + me
    if elf == me:
        score += 3
    elif s in ["AB", "BC", "CA"]:
        score += 6
    if me == 'A':
        score += 1
    if me == 'B':
        score += 2
    if me == 'C':
        score += 3
    # print(elf, me)
print(score)

score = 0
for line in lines:
    elf, me = line.split()
    if me == "Y":
        me = elf
        score += 3
    elif me == "X":
        if elf == "A":
            me = "C"
        if elf == "B":
            me = "A"
        if elf == "C":
            me = "B"
    elif me == "Z":
        score += 6
        if elf == "A":
            me = "B"
        if elf == "B":
            me = "C"
        if elf == "C":
            me = "A"

    
    if me == 'A':
        score += 1
    if me == 'B':
        score += 2
    if me == 'C':
        score += 3
print(score)
