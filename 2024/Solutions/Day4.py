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
    # x is horizontal position, y is horizontal position, 'MAS' has four X possibilities?
    goahead = 0
    tops = []

    # We can't an X if there's not enough space in the top to bottom or left to right
    if ((x + 1 > hori - 1) or (x - 1 < 0) or (y + 1 > verti - 1) or (y - 1 < 0)):
        # print("Won't fit")
        return 0
    else:
        if (grid[y - 1][x - 1] == 'M' or grid[y - 1][x - 1] == 'S'):
            tops.append(grid[y - 1][x - 1])
        else:
            #print ("1 is bad")
            return 0
        
        if (grid[y - 1][x + 1] == 'M' or grid[y - 1][x + 1] == 'S'):
            tops.append(grid[y - 1][x + 1])
        else:
            #print ("2 is bad")
            return 0

        if (grid[y + 1][x + 1] != tops[0] and grid[y + 1][x + 1] != 'X' and grid[y + 1][x + 1] != 'A'):
            goahead = 1
        else:
            #print ("3 is bad")
            return 0
        if (grid[y + 1][x - 1] != tops[1] and grid[y + 1][x - 1] != 'X' and grid[y + 1][x - 1] != 'A'):
            goahead = 1
        else:
            #print ("4 is bad")
            return 0
        #print(grid[y - 1][x - 1], grid[y + 1][x + 1], grid[y][x], grid[y - 1][x + 1], grid[y + 1][x - 1])
        return 1

# Run
for x in range(0, 140):
    # Take apart the input
    separate()

verti = len(grid)
hori = len(grid[0])

for y in range (0, len(grid)):
    for x in range (0, len(grid[0])):
        if (grid[y][x] != 'A'):
            continue
        else:
            xmas = xmas + findx(x, y)

print("We found " + str(xmas) + " instances")

# Endslate
lines.close()