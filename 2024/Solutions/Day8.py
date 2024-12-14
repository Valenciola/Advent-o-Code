import itertools

lemap = open("2024/Inputs/D8.txt", "r")
grid = lemap.read().splitlines()

for x in range(0, len(grid)):
    grid[x] = list(grid[x])

hori = len(grid[0])
verti = len(grid)
antinodes = []

print(hori, "x", verti)

def findantennas(antenna):
    # Find the location of every single antenna of a certain type
    found = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if (grid[y][x] == antenna):
                found.append([x, y])
            else:
                continue
    print(antenna + ":", found)
    return found

def findantinodes(locations):
    global antinodes
    pairs = list(itertools.combinations(locations, 2)) # Trying an itertool for the first time; this will form the pairs
    for pair in pairs:
        slope = [pair[1][0] - pair[0][0], + pair[1][1] - pair[0][1]]
        rate = 1

        x = pair[1][0] + slope[0]
        y = pair[1][1] + slope[1]
        antinode = [x, y]
        while (not(x < 0) and not(x > hori - 1) and not(y < 0) and not(y > verti - 1)):
            if (not([x, y] in antinodes)):
                antinodes.append([x, y])
            rate += 1
            x = pair[1][0] + (slope[0] * rate)
            y = pair[1][1] + (slope[1] * rate)
        
        rate = 1
        x = pair[0][0] - slope[0]
        y = pair[0][1] - slope[1]
        antinode = [x, y]
        while (not(x < 0) and not(x > hori - 1) and not(y < 0) and not(y > verti - 1)):
            if (not([x, y] in antinodes)):
                antinodes.append([x, y])
            rate += 1
            x = pair[0][0] - (slope[0] * rate)
            y = pair[0][1] - (slope[1] * rate)

        #antinode1 = [pair[1][0] + slope[0], pair[1][1] + slope[1]]
        #antinode2 = [pair[0][0] - slope[0], pair[0][1] - slope[1]]

        #print(pair[0], pair[1], slope)
    return

# Get every kind of antenna so we can search through easily and then find their locations
antennatypes = []
locations = []
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        if ((grid[y][x] in antennatypes) or (grid[y][x] == '.')):
            continue
        else:
            antennatypes.append(grid[y][x])
for x in range(0, len(antennatypes)):
    locations.append(findantennas(antennatypes[x]))

for x in range(0, len(locations)):
    findantinodes(locations[x])

for x in range(0, len(locations)):
    for i in locations[x]:
        if (not (i in antinodes)):
            antinodes.append(i)


#print(antinodes)
print("In the end, we got", (len(antinodes)), "antinodes")

''' # Test stuff that might break my console if I try to print it with puzzle input haha
for x in antinodes:
    grid[x[1]][x[0]] = '#'

for x in grid:
    print(x)
'''

lemap.close()