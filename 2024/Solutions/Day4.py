lines = open("2024/Inputs/D4.txt", "r")
grid = []
verti = 0
hori = 0
xmas = 0

# Functions
def separate():
    # Create a multi-dimensional array and use it as a grid
    think = lines.readline()
    chars = []
    for x in range(0, len(think)):
        chars.append(think[x])
    if (chars[len(chars) - 1] == "\n"):
        chars.pop(len(chars) - 1)
    grid.append(chars)

def findx(x, y):
    # x is horizontal position, y is horizontal position, 'XMAS' is a four-letter word
    states = [1, 1, 1, 1, 1, 1, 1, 1]
    xmases = 0
    goahead = 0
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, 1], [-1, -1], [1, 1], [1, -1]]
    '''
    Determine what combinations are possible so we can just ignore other ones
    # Forwards horizontal (0)
    # backwards horizontal (1)
    # forwards vertical (2)
    # backwards vertical (3)
    # forwards diagonal left (4)
    # backwards diagonal left (5)
    # forwards diagonal right (6)
    # backwards diagonal right (7)
    '''
    if ((x + 3) > hori - 1):
        states[0] = 0
        states[6] = 0
        states[7] = 0
    if ((x - 3) < 0):
        states[1] = 0
        states[4] = 0
        states[5] = 0
    if ((y + 3) > verti - 1):
        states[2] = 0
        states[4] = 0
        states[6] = 0
    if ((y - 3) < 0):
        states[3] = 0
        states[5] = 0
        states[7] = 0
    # print(states)

    for i in range (0, 8):
        if (states[i]):
            xlook = direction[i][0]
            ylook = direction[i][1]
            goahead = (grid[y + ylook][x + xlook] == 'M') and (grid[y + (ylook * 2)][x + (xlook * 2)] == 'A') and (grid[y + (ylook * 3)][x + (xlook * 3)] == 'S')
            goahead = int(goahead)
            if (goahead):
                # print("Caught on instance " + str(i))
                xmases += 1
        else:
            continue
    
    print("Collected " + str(xmases))
    return xmases

# Run
for x in range(0, 140):
    # Take apart the input
    separate()

verti = len(grid)
hori = len(grid[0])

for y in range (0, len(grid)):
    for x in range (0, len(grid[0])):
        # print(grid[y][x])
        if (grid[y][x] != 'X'):
            continue
        else:
            # print("This is an X")
            xmas = xmas + findx(x, y)

print("We found " + str(xmas) + " instances")

# Endslate
lines.close()