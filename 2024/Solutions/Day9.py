import copy

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

def findconti(space):
    global mem
    opening = 0
    for x in range(0, len(mem)):
        #print(x)
        if (str(mem[x]).isdigit()):
            opening = 0
        elif (mem[x] == '.'):
            opening += 1
            if (opening == space):
                return (x - opening + 1)
    return 0

for x in range(maxid, -1, -1):
    avail = findconti(mem.count(x))
    if (avail and not (avail > mem.index(x))):
        for z in range(0, mem.count(x)):
            #print(avail + z)
            mem[mem.index(x, (avail + z))] = '.'
            mem[avail + z] = x
#print(mem)
    
for x in range(0, len(mem)):
    #print(x, mem[x])
    if (mem[x] == '.'):
        continue
    total = total + (x * mem[x])

print(total)

grab.close()