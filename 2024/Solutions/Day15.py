waremap = open("2024/Inputs/D15.txt", "r")

grid = []
instructs = []
position = []
boxes = []

# Functions
def move(instruct: str):
    # Move the robot through the grid again I guess
    global position, grid
    inpath = ''
    x = position[0]
    y = position[1]
    directions = []

    match instruct:
        case '<':
            inpath = grid[y][x - 1]
            directions = [-1, 0]
        case '^':
            inpath = grid[y - 1][x]
            directions = [0, -1]
        case '>':
            inpath = grid[y][x + 1]
            directions = [1, 0]
        case 'v':
            inpath = grid[y + 1][x]
            directions = [0, 1]

    if (inpath == '#'):
        # It's a wall, don't do anything
        #print("Wall")
        return
    elif (inpath == 'O'):
        # Try to move a box
        boxx = x + directions[0]
        boxy = y + directions[1]
        boxes = []

        while (inpath == 'O'): # Find every box in the path
            boxes.append([boxx, boxy])
            boxx += directions[0]
            boxy += directions[1]
            inpath = grid[boxy][boxx]
        
        #print(boxes)
        if (inpath == '#'):
            return
        else:
            for i in reversed(boxes):
                grid[i[1]][i[0]] = '.'
                grid[i[1] + directions[1]][i[0] + directions[0]] = 'O'
        
        # Update the position after
        grid[y][x] = '.'
        match instruct:
            case '<':
                position = [x - 1, y]
            case '^':
                position = [x, y - 1]
            case '>':
                position = [x + 1, y]
            case 'v':
                position = [x, y + 1]
        grid[position[1]][position[0]] = '@'
        return

    else:
        # Move as normal
        #print("Move")
        grid[y][x] = '.'
        match instruct:
            case '<':
                position = [x - 1, y]
            case '^':
                position = [x, y - 1]
            case '>':
                position = [x + 1, y]
            case 'v':
                position = [x, y + 1]
        grid[position[1]][position[0]] = '@'
        return

for _ in range(71): # Reading the file and categorizing it into where it needs to go
    line = waremap.readline()
    line = line.strip()
    if ('#' in line):
        grid.append(list(line))
    elif ('^' in line) or ('<' in line) or ('>' in line) or ('v' in line):
        for i in line:
            instructs.append(i)
    else:
        continue

for y in range(0, len(grid)):
    if ('@' in grid[y]):
        position = [grid[y].index('@'), y]
    else:
        continue

# Moving through the grid
for x in range(0, len(instructs)):
    move(instructs[x])

# Getting box positions after it's all said and done
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        if (grid[y][x] == 'O'):
            boxes.append([x, y])
        else:
            continue

gps = 0
for x in boxes:
    gps += 100 * x[1] + x[0]

for x in grid:
    print(x)
#print(instructs)
print(boxes)

print("The GPS sum is " + str(gps))

waremap.close()