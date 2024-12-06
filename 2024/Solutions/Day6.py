mapgram = open("2024/Inputs/D6.txt", "r")
grid = []
position = [0,0] # Go (x,y)
direction = 0
stops = 0

def trace(position):
    x = position[0]
    y = position[1]
    grid[y][x] = 'X'
    scope = [x, y]
    global direction
    #print(scope)
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
        #print("Out of here")
        return 0
    elif (grid[scope[1]][scope[0]] == '#'):
        # print("Roadblock")
        # print(scope)
        direction += 1
        if (direction == 4):
            direction = 0
        return 1
    else:
        position[0] = scope[0]
        position[1] = scope[1]
        return 1

for x in range(0, 130):
    mapline = mapgram.readline().strip()
    grid.append(mapline)

for x in range(0, len(grid)):
    grid[x] = list(grid[x])
    if ('^' in grid[x]):
        position[1] = x
        position[0] = grid[x].index('^')
    #print(grid[x])

verti = len(grid)
hori = len(grid[0])

print(position)

active = 1
while(active):
    active = trace(position)

for x in range(0, len(grid)):
    stops = stops + grid[x].count('X')

print("The guard makes " + str(stops) + " stops.")

'''
for x in range(0, len(grid)):
    print(grid[x])
'''

mapgram.close()