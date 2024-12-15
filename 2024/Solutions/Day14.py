import copy

robots = open("2024/Inputs/D14.txt", "r")
positions = []
velocities = []
grid = []

# Boundaries/Dimensions (change for input)
hori = 101
verti = 103

# Functions
def creategrid(width, height):
    # Create a grid with the given dimensions
    #print(width, height)
    row = []
    template = []
    for _ in range(height):
        for _ in range(width):
            row.append('.')
        template.append(copy.deepcopy(row))
        row.clear()
    return template

def plotpos(positions: list):
    # Plot positions given the initial guard positions
    global grid
    for i in positions:
        x = i[0]
        y = i[1]
        if (grid[y][x] == '.'):
            grid[y][x] = 1
        else:
            grid[y][x] = grid[y][x] + 1
    return

def move():
    global locations, velocities, grid, hori, verti
    for i in range(0, len(velocities)):
        x = locations[i][0]
        y = locations[i][1]

        # For visualization purposes
        if (grid[y][x] == 1):
            grid[y][x] = '.'
        else:
            grid[y][x] = grid[y][x] - 1
        
        x += velocities[i][0]
        if (x > hori - 1):
            x = x - hori
        elif (x < 0):
            x = x + hori
        
        y += velocities[i][1]
        if (y > verti - 1):
            y = y - verti
        elif (y < 0):
            y = y + verti
        
        locations[i] = [x, y]
        
        if (grid[y][x] == '.'):
            grid[y][x] = 1
        else:
            grid[y][x] = grid[y][x] + 1
        
    return

def checkover(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (grid[y][x] == '.' or grid[y][x] == 1):
                continue
            else:
                return True
    return False
        
for _ in range(500): # Read and sort the list (change range for input)
    robot = robots.readline()
    robot = robot.replace("p=", "")
    robot = robot.replace("v=", "")
    robot = robot.strip()
    robot = robot.split()
    for x in range(0, len(robot)):
        robot[x] = robot[x].split(',')
        for y in range(0, len(robot[x])):
            robot[x][y] = int(robot[x][y])
    positions.append(robot[0])
    velocities.append(robot[1])

grid = creategrid(hori, verti)
plotpos(positions)
locations = copy.deepcopy(positions)


flag = True
march = 0
while (flag):
    march += 1
    move()
    flag = checkover(grid)

print(march)

# Test stuff
for x in grid:
    print(x)

robots.close()