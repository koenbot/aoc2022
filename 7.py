import collections

lines = map(str.strip, open("7.txt").readlines())

curdir = []

dirsizes = collections.defaultdict(dict)
dirsubs = {'': []}

for line in lines:
    if line[0] == '$':
        command = line[2:]
        # print(command)
        if command == "cd /":
            curdir = []
        elif command == "cd ..":
            curdir = curdir[:-1]
        elif command.startswith("cd"):
            dir = command[3:]
            curdir.append(dir)
        # print(curdir)
    else: # must be in ls mode
        dir = "/".join(curdir)
        if line.startswith("dir"):
            subname = line[4:]
            if dir != '':
                subdir = dir + "/" + subname
            else:
                subdir = subname
            if subdir not in dirsubs:
                dirsubs[subdir] = []
            dirsubs[dir].append(subname)
        else:
            size, name = line.split(" ")
            dirsizes[dir][name] = int(size)

for k, v in dirsizes.items():
    print(k,v)
for k, v in dirsubs.items():
    print(k,v)


def getsize(root):
    # print(root)
    tot = sum(dirsizes[root].values())
    for dir in dirsubs[root]:
        if root != "":
            dir = root + "/" + dir
        tot += getsize(dir)
    return tot

sub1k = 0

keys = list(dirsubs.keys())
print(keys)
for key in keys:
    size = getsize(key)
    print(key, size)
    if size <= 100000:
        print(key, size)
        sub1k += size 

print(sub1k)


tot = getsize("")
unused = 70000000 - tot
minreq = 30000000 - unused
print(minreq)

bestgood = 1e99

for key in keys:
    size = getsize(key)
    if size >= minreq and size < bestgood:
        # print(size)
        bestgood = size
print(bestgood)
