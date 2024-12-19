import copy, collections
bytemap = open("2024/Inputs/D18.txt", "r")

#bytecount = 1024 # The number of falling bytes (change for applications)
falling = set()
square = 70 # The grid is a square; basically dimensions (change for applications)
grid = []
endgoal = (square, square)

def bestpath(walls: set, target: tuple):
    queue = collections.deque() # So now I'm learning how to use a queue... AoC's really making me learn a lot
    queue.append(((0, 0), 0, []))

    seen = set() # I've also never used a set before this is a good learning experience but I'm so inexperienced
    shortest = float("inf")
    helppath = [] # I really just need to visualize it

    while queue:
        position, score, path = queue.popleft()

        if position in seen:
            continue

        seen.add(position)
        path = path + [position]

        if score > shortest:
            continue

        if position == target:
            shortest = score
            helppath = path
            continue

        for directions in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            newpos = (position[0] + directions[0], position[1] + directions[1])

            if (newpos in seen) or (newpos in walls): # Have we been here already or are we hitting a wall?
                continue

            if (newpos[0] < 0) or (newpos[0] > target[0]) or (newpos[1] < 0) or (newpos[1] > target[1]): # Are we out of bounds?
                continue
        
            queue.append((newpos, score + 1, path))

    return shortest, path

finale = 0
# Add necessary bytes and whatnot
for i in range(0, 3450):
    helper = bytemap.readline().strip() # I always need a helper variable to just handle menial tasks
    helper = helper.split(',')
    for j in range(0, len(helper)):
        helper[j] = int(helper[j])
    helper = (helper[0], helper[1])
    falling.add(helper)

    finale, lepath = bestpath(falling, endgoal)
    print("i:", i, helper, finale)
    if (finale == float("inf")):
        break

    #test = input("")
    

'''
helper = []
for i in range(0, square + 1): # Create the empty grid
    for j in range(0, square + 1):
        helper.append('.')
    grid.append(copy.deepcopy(helper))
    helper.clear()

for i in falling: # Insert the falling bytes
    grid[i[1]][i[0]] = '#'

for i in lepath: # Visualization for path marker
    grid[i[1]][i[0]] = 'O'
'''

'''
for x in grid: # I just wanted to see it
    print(x)
'''

bytemap.close()