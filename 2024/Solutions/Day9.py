grab = open("2024/Inputs/D9.txt", "r")
line = grab.readline()
#print(line)
total = 0

blocks = []
spaces = []
for x in range (0, len(line)):
    focus = int(line[x])
    if (x % 2 == 0):
        blocks.append(focus)
    else:
        spaces.append(focus)
spaces.append(0)

#print(blocks)
#print(spaces)

mem = []
for x in range(0, len(blocks)):
    for y in range(0, blocks[x]):
        mem.append(x)
    for y in range(0, spaces[x]):
        mem.append('.')
maxid = x

#print(mem)

for x in mem:
    #print(x)
    if (str(x).isdigit()):
        continue
    else:
        while (mem[len(mem) - 1] == '.'):
            mem.pop(len(mem) - 1)
        mem[mem.index(x)] = mem[len(mem) - 1]
        mem.pop(len(mem) - 1)
    #print(mem)

for x in range(0, len(mem)):
    #print(x, mem[x])
    if (mem[x] == '.'):
        continue
    total = total + (x * mem[x])

print(total)

grab.close()