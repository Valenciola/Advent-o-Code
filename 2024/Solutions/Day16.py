import collections, copy
reinmaze = open("2024/example.txt", "r")

def bestpath(walls: set, start: tuple, target: tuple):
    queue = collections.deque() # Taking from Day 18
    queue.append((start, (1, 0), 0, [])) # Starting position, direction (1, 0 is facing east), score, path makeup

    seen = set() # I've also never used a set before this is a good learning experience but I'm so inexperienced
    shortest = float("inf")
    helppath = [] # I really just need to visualize it
    bonsai = {}

    while queue:

        position, direction, score, path = queue.popleft()

        seen.add(position)
        path = path + [position]

        if position == target: # We reached the end?
            shortest = min(score, shortest) # Which path has a lower score...
            seen.remove(position)
            helppath = path
            continue
            
        if score > shortest: # We've gone too far already
            seen.remove(position)
            continue

        if bonsai.get(position, float("inf")) < score:
            seen.remove(position)
            continue
        else:
            bonsai[position] = score

        for directions in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if directions == (-direction[0], -direction[1]): # Don't go backwards
                continue

            newpos = (position[0] + directions[0], position[1] + directions[1])

            if (newpos in seen) or (newpos in walls): # Have we been here already or are we hitting a wall?
                continue
            
            queue.append((newpos, directions, score + 1 + (directions != direction) * 1000, path))

        seen.remove(position) # I think this seeks new paths

    return shortest, helppath

# Create a grid off the bat
grid = reinmaze.read().splitlines()
for i in range(0, len(grid)):
    grid[i] = list(grid[i])

# Starting lineup for variables
walls = set()
start = (0, 0)
end = (0, 0)
finale = 0

# Get walls, start point, end point
for i in range(0, len(grid)):
    for j in range(0, len(grid[0])): # (x, y) = (j, i)
        if grid[i][j] == '#':
            walls.add((j, i))
        elif grid[i][j] == 'S':
            start = (j, i)
        elif grid[i][j] == 'E':
            end = (j, i)
        else:
            continue

finale, path = bestpath(walls, start, end)
print(finale)
path = set(path)

# Attempt to block every cell in the best paths to see how it recalculates

reinmaze.close()