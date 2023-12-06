almanac = open("Inputs/Chal5.txt", "r")
sight = almanac.readline()
seeds = [] # Initial seeds
locations = []
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
soil, fertilizer, water, light, temperature, humidity, location = [], [], [], [], [], [], []
lowest = 0

# Setup Functions
def scan(array, line):
    while line != "\n" and line != "":
        line = almanac.readline()
        line.strip('\n')
        array.append(line)

def clean(array):
    for x in range(0, len(array)):
        array[x] = array[x].strip()
    array.pop(len(array) - 1)

def readseeds():
    # Read the seeds
    seed = ""
    for x in range (0, len(sight)):
        # print("x is " + str(x), sight[x])
        if (x < 7):
            pass
        elif(sight[x].isdigit()):
            # print("That's a digit.")
            seed = seed + sight[x]
        else:
            # print("That's a space.")
            seeds.append(int(seed))
            seed = ""

def readtostart():
    # Read entire rest of file
    for x in range (1, 3):
        sight = almanac.readline()
    scan(soil, sight)
    clean(soil)

    for x in range (1, 2):
        sight = almanac.readline()
    scan(fertilizer, sight)
    clean(fertilizer)

    for x in range (1, 2):
        sight = almanac.readline()
    scan(water, sight)
    clean(water)

    for x in range (1, 2):
        sight = almanac.readline()
    scan(light, sight)
    clean(light)

    for x in range (1, 2):
        sight = almanac.readline()
    scan(temperature, sight)
    clean(temperature)

    for x in range (1, 2):
        sight = almanac.readline()
    scan(humidity, sight)
    clean(humidity)

    for x in range (1, 2):
        sight = almanac.readline()
    scan(location, sight)
    clean(location)

def transform(seed, list):
    destination = 0
    source = 0
    ran = 0
    indice = 0
    final = seed
    sourcerun = []
    destirun = []
    found = 0
    # print(final)
    # print(seed)
    for x in range (0, len(list)):
        phase = 1
        construct = ""
        for y in list[x]:
            if (y.isdigit()):
                # print(construct)
                construct = construct + y
            else:
                if (phase == 1):
                    destination = int(construct)
                    construct = ""
                    phase = 2
                elif (phase == 2):
                    source = int(construct)
                    construct = ""
        ran = int(construct) # take whatever is left
        # print(destination, source, ran)

        # Check for range
        if not (source > seed):
            # print("Not greater!")
            if ((seed - source) < ran and (seed - source) >= 0):
                # print("Within range!")
                found = 1
                break
            else:
                pass
        else:
            # print("Greater!")
            pass
    
    # print(destination, source, ran)

    if (found == 1):
        for x in range (0, ran):
            sourcerun.append(source + x)
            destirun.append(destination + x)
        
        while (sourcerun[indice] != seed):
            indice = indice + 1
        final = destirun[indice]
    else:
        pass
    
    return (final)

# Actual running
# Starting
readseeds()
readtostart()

# Running seeds
for x in range(0, len(seeds)):
    sow = seeds[x]

    sow = transform(sow, soil)
    sow = transform(sow, fertilizer)
    sow = transform(sow, water)
    sow = transform(sow, light)
    sow = transform(sow, temperature)
    sow = transform(sow, humidity)
    sow = transform(sow, location)
    
    locations.append(sow)

# Calculating the lowest
lowest = locations[x]
for x in range(0, len(locations)):
    if (lowest > locations[x]):
        lowest = locations[x]

# print(seeds)
# print(soil, fertilizer, water, light, temperature, humidity, location)
print(locations)
print(lowest)

almanac.close()