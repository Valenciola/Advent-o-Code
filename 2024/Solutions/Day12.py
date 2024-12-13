garden = open("2024/Inputs/D12.txt", "r")

# Create the garden
grid = garden.read().splitlines()
for x in range(0, len(grid)):
    grid[x] = list(grid[x])

viewed = []
verti = len(grid)
hori = len(grid[0])
regions = []
cost = 0

# The functions
def scan(x, y):
    # In other words, we look around
    view = [0, 0, 0, 0]
    #print(x, y)

    if (y - 1 < 0):
        view[0] = None
    else:
        view[0] = grid[y - 1][x]

    if (x + 1 > hori - 1):
        view[1] = None
    else:
        view[1] = grid[y][x + 1]
    
    if (y + 1 > verti - 1):
        view[2] = None
    else:
        view[2] = grid[y + 1][x]
    
    if (x - 1 < 0):
        view[3] = None
    else:
        view[3] = grid[y][x  - 1]
    
    return view

def check(x, y):
    # In other words, we get regions here
    if ([x, y] in viewed):
        return
    else:
        idea = []
        checks = [[x, y]]
        letter = grid[y][x]

        while checks:
            cx, cy = checks.pop(0)
            if ([cx, cy] not in viewed):
                idea.append([cx, cy])
                viewed.append([cx, cy])
                around = scan(cx, cy)

                if (letter in around):
                    for a in range(0, len(around)):
                        if (around[a] == letter):
                            match a:
                                case 0:
                                    checks.append([cx, cy - 1])
                                case 1:
                                    checks.append([cx + 1, cy])
                                case 2:
                                    checks.append([cx, cy + 1])
                                case 3:
                                    checks.append([cx - 1, cy])
        return idea

def getarea(region):
    # Get the area of a region but it's kinda just the number of points
    return len(region)

def getperi(region, letter):
    # Get the perimeter with the help of a hint from George
    peri = 0
    for re in region:
        focus = scan(re[0], re[1])
        for n in focus:
            if (n != letter):
                peri += 1
            else:
                continue
    return peri

# Find the regions
for y in range(0, verti):
    for x in range(0, hori):
        if ([x, y] in viewed):
            continue
        else:
            regions.append(check(x, y))

# Get calculations
for x in range(0, len(regions)):
    letter = grid[regions[x][0][1]][regions[x][0][0]]
    print(letter + ":", getarea(regions[x]), "*", getperi(regions[x], letter), "=", getarea(regions[x]) * getperi(regions[x], letter))
    cost += getarea(regions[x]) * getperi(regions[x], letter)

print("The total cost will be", str(cost))

'''
# Random stuff I print to check
print("The grid")
for x in range(0, len(grid)):
    print(grid[x])
print("Dimensions:", hori, "x", verti)
for x in range(0, len(regions)):
    print(grid[regions[x][0][1]][regions[x][0][0]] + ":", regions[x])
'''

garden.close()