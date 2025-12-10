import copy

waremap = open("2024/Inputs/D15.txt", "r")

grid = []
instructs = []
position = []
boxes = []
oldgrid = []

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
    elif (inpath == '[' or inpath == ']'):
        # Try to move a box
        boxx = x + directions[0]
        boxy = y + directions[1]
        boxes = []
        side = inpath

        while (inpath == '[' or inpath == ']'): # Find every box in the path
            boxes.append([boxx, boxy])
            if (instruct == '<' or instruct == '>'):
                boxx += directions[0] * 2
            else:
                if ((inpath == '[' and grid[boxy + directions[1]][boxx + 1] == '[') or (inpath == ']' and grid[boxy + directions[1]][boxx + 1] == ']')):
                    boxes.append([boxx + 1, boxy + directions[1]])
                    boxes.append([boxx + 1, boxy + directions[1] * 2])
                elif ((inpath == ']' and grid[boxy + directions[1]][boxx - 1] == ']') or (inpath == '[' and grid[boxy + directions[1]][boxx - 1] == '[')):
                    boxes.append([boxx - 1, boxy + directions[1]])
                    boxes.append([boxx - 1, boxy + directions[1] * 2])
                boxx += directions[0]
            boxy += directions[1]
            inpath = grid[boxy][boxx]
        
        if (inpath == '#'):
            return
        else:
            if ((instruct == '^') or (instruct == 'v')):
                for i in boxes:
                    if (grid[i[1]][i[0]] == '#' or grid[i[1] + directions[1]][i[0]] == '#'):
                        return
                    elif (grid[i[1]][i[0]] == '.'):
                        boxes.remove(i)
                    elif (grid[i[1]][i[0]] == '[' and grid[i[1] + directions[1]][i[0] + 1] == '#'):
                        return
                    elif (grid[i[1]][i[0]] == ']' and grid[i[1] + directions[1]][i[0] - 1] == '#'):
                        return
                    elif (grid[i[1]][i[0]] == '[' and grid[i[1] + directions[1]][i[0] + 1] == '[' and [i[0] + 1, i[1] + directions[1]] not in boxes):
                        boxes.append([i[0] + 1, i[1] + directions[1]])
                        boxes.append([i[0] + 1, i[1] + directions[1] * 2])
                    elif (grid[i[1]][i[0]] == ']' and grid[i[1] + directions[1]][i[0] - 1] == ']' and [i[0] - 1, i[1] + directions[1]] not in boxes):
                        boxes.append([i[0] - 1, i[1] + directions[1]])
                        boxes.append([i[0] - 1, i[1] + directions[1] * 2])
                    elif (((grid[i[1]][i[0]] == '[' and grid[i[1] + directions[1]][i[0]] == ']') or (grid[i[1]][i[0]] == ']' and grid[i[1] + directions[1]][i[0]] == '[')) and ([i[0], i[1] + directions[1]] not in boxes)):
                        boxes.append([i[0], i[1] + directions[1]])
                    else:
                        continue
                print(boxes)
                for i in reversed(boxes):
                    side = grid[i[1]][i[0]]
                    #print(side)
                    if (side == '['):
                        grid[i[1]][i[0]] = '.'
                        grid[i[1]][i[0] + 1] = '.'

                        grid[i[1] + directions[1]][i[0] + directions[0]] = '['
                        grid[i[1] + directions[1]][i[0] + directions[0] + 1] = ']'
                    elif (side == ']'):
                        grid[i[1]][i[0]] = '.'
                        grid[i[1]][i[0] - 1] = '.'

                        grid[i[1] + directions[1]][i[0] + directions[0] - 1] = '['
                        grid[i[1] + directions[1]][i[0] + directions[0]] = ']'
            elif ((instruct == '<') or (instruct == '>')):
                for i in reversed(boxes):
                    if (side == '['):
                        grid[i[1]][i[0]] = '.'
                        grid[i[1]][i[0] + 1] = '.'

                        grid[i[1] + directions[1]][i[0] + directions[0] + 1] = ']'
                        grid[i[1] + directions[1]][i[0] + directions[0]] = '['
                    elif (side == ']'):
                        grid[i[1]][i[0]] = '.'
                        grid[i[1]][i[0] - 1] = '.'

                        grid[i[1] + directions[1]][i[0] + directions[0] - 1] = '['
                        grid[i[1] + directions[1]][i[0] + directions[0]] = ']'
        
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

def doublegrid(original: list):
    newgrid = []
    line = []

    '''
    for x in original:
        print(x)
    '''
    
    for y in range(0, len(original)):
        for x in range(0, len(original[0])):
            point = original[y][x]
            match point:
                case '#':
                    line.append('#')
                    line.append('#')
                case 'O':
                    line.append('[')
                    line.append(']')
                case '.':
                    line.append('.')
                    line.append('.')
                case '@':
                    line.append('@')
                    line.append('.')
        newgrid.append(copy.deepcopy(line))
        line.clear()
    return newgrid

for _ in range(71): # Reading the file and categorizing it into where it needs to go
    line = waremap.readline()
    line = line.strip()
    if ('#' in line):
        oldgrid.append(list(line))
    elif ('^' in line) or ('<' in line) or ('>' in line) or ('v' in line):
        for i in line:
            instructs.append(i)
    else:
        continue

grid = doublegrid(oldgrid)

for y in range(0, len(grid)):
    if ('@' in grid[y]):
        position = [grid[y].index('@'), y]
    else:
        continue

#print(position)

# Moving through the grid
test = 0
for x in range(0, len(instructs)):
    helper = open("2024/help.txt", "w").close()
    helper = open("2024/help.txt", "a")
    print(x)
    move(instructs[x])
    print(instructs[x])
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            helper.write(grid[i][j])
        helper.write("\n")
    helper.close()
    if (x > 3420):
        test = input("")

# Getting box positions after it's all said and done
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        if (grid[y][x] == '['):
            boxes.append([x, y])
        else:
            continue

gps = 0
for x in boxes:
    gps += 100 * x[1] + x[0]

#for x in grid:
    #print(x)
#print(instructs)
#print(boxes)

print("The GPS sum is " + str(gps))

waremap.close()