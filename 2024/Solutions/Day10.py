topo = open("2024/Inputs/D10.txt", "r")
grid = []
heads = []
scores = 0
forks = []
checked = []

def lookahead(x, y):
    global hori,verti
    poss = [0, 0, 0, 0]
    #print(x, y)

    if (not (y - 1 < 0)):
        poss[0] = int(grid[y - 1][x])
    else:
        poss[0] = None
    
    if (not (x + 1 > hori - 1)):
        poss[1] = int(grid[y][x + 1])
    else:
        poss[1] = None
    
    if (not (y + 1 > verti - 1)):
        poss[2] = int(grid[y + 1][x])
    else:
        poss[2] = None
    
    if (not (x - 1 < 0)):
        poss[3] = int(grid[y][x - 1])
    else:
        poss[3] = None
    
    return poss

def seek(x, y):
    focus = int(grid[y][x])
    look = lookahead(x, y)
    search = focus + 1
    global scores, forks, checked
    temp = 0

    #print(x, y)
    #print(focus)
    #print(look)

    if (focus == 9):
        if (not ([x, y] in checked)):
            scores += 1
            checked.append([x, y])
        return

    if (search in look): # Basically, this is how I check for forks in the road
        if (look.count(search) > 1):
            for z in range(0, look.count(search) - 1):
                if (temp == 0):
                    temp = look.index(search, look.index(search) + (z + 1))
                else:
                    temp = look.index(search, temp + 1)
                #print(temp)
                match(temp):
                    case 0:
                        if (not ([x, y - 1] in forks)):
                            forks.append([x, y - 1])
                    case 1:
                        if (not ([x + 1, y] in forks)):
                            forks.append([x + 1, y])
                    case 2:
                        if (not ([x, y + 1] in forks)):
                            forks.append([x, y + 1])
                    case 3:
                        if (not ([x - 1, y] in forks)):
                            forks.append([x - 1, y])
        match(look.index(search)):
            case 0:
                y = y - 1
            case 1:
                x = x + 1
            case 2:
                y = y + 1
            case 3:
                x = x - 1

        #print(int(grid[y][x]))
        #print(forks)

        seek(x, y)
    else:
        return
    
    return

for x in range(0, 40):
    topline = topo.readline()
    topline = topline.strip()
    grid.append(topline)
for x in range(0, len(grid)):
    grid[x] = list(grid[x])
    for y in range(0, len(grid[x])):
        if (grid[x][y] == '0'):
            heads.append([y, x])

verti = len(grid)
hori = len(grid[0])

for x in range(0, len(grid)):
    print(grid[x])
#print(heads)

for x in range(0, len(heads)):
    seek(heads[x][0], heads[x][1])
    for i in forks:
        #print(i)
        seek(i[0], i[1])
    forks.clear()
    checked.clear()
print("The score? It's " + str(scores))

topo.close()