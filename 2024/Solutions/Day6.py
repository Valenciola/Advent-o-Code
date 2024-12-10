import copy

mapgram = open("2024/Inputs/D6.txt", "r")
grid = []
position = [0,0] # Go (x,y)
direction = 0
marks = []
returns = 0
blocks = 0
transcript = []
weirdos = []

def trace(position):
    #Working through the map
    x = position[0]
    y = position[1]
    grid[y][x] = 'X'
    scope = [x, y]
    global direction
    #print(scope)
    global returns # The amount of times we hit the O
    global blocks
    global transcript, lim

    global weirdos

    match direction: # Look ahead in the grid
        case 0: # Facing forward
            scope = [x, y - 1]
        case 1: # Facing right
            scope = [x + 1, y]
        case 2: # Facing down
            scope = [x, y + 1]
        case 3: # Facing left
            scope = [x - 1, y]
    if ((scope[0] > hori - 1) or (scope[1] > verti - 1) or (scope[0] < 0) or (scope[1]) < 0):
        print("Out of here")
        returns = 0
        return 0
    elif (grid[scope[1]][scope[0]] == '#' or grid[scope[1]][scope[0]] == 'O'):
        #print("Roadblock", scope)
        if (grid[scope[1]][scope[0]] == 'O'):
            returns += 1
            if (returns > 5):
                print("Good boundary")
                print(returns)
                returns = 0
                blocks += 1
                return 0
        
        direction += 1
        if (direction == 4):
            direction = 0
        return 1
    else:
        position[0] = scope[0]
        position[1] = scope[1]
        transcript.append(scope)
        if (len(transcript) > lim):
            transcript.clear()
            weirdos.append(returns)
            blocks += 1
            returns = 0
            return 0
        return 1

# Grid generation
for x in range(0, 130):
    mapline = mapgram.readline().strip()
    grid.append(mapline)

for x in range(0, len(grid)):
    grid[x] = list(grid[x])
    if ('^' in grid[x]):
        position[1] = x
        position[0] = grid[x].index('^')
    #print(grid[x])

# Establishing boundaries and saving the start point
verti = len(grid)
hori = len(grid[0])
init = copy.deepcopy(position)
lim = verti * hori * 100

print(position)

active = 1
while(active):
    active = trace(position)

for y in range(0, verti):
    for x in range(0, hori):
        if (grid[y][x] == 'X'):
            marks.append([x,y])
            grid[y][x] = '.'

marks.remove(init)
grid[init[1]][init[0]] = '^'
#print(marks)

print("Reviewing with blocks")
for x in range(0, len(marks)):
    chx = marks[x][0]
    chy = marks[x][1]
    print(chx, chy)
    grid[chy][chx] = 'O'
    position = copy.deepcopy(init)
    active = 1
    direction = 0
    while(active):
        active = trace(position)
    grid[chy][chx] = '.'

# print(init)
# print(position)

'''
for x in range(0, len(grid)):
    print(grid[x])
'''

print("We can do " + str(blocks) + " obstructions")
print(weirdos)

mapgram.close()