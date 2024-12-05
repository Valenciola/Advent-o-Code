import math

instructs = open("2024/Inputs/D5.txt", "r")
rules = []
manuals = []
grabs = instructs.readline()
unpasses = []
total = 0
mode = 0

def inspect(line, mode):
    #print(line)
    for x in range(0, len(rules)):
        rule = rules[x]
        if ((rule[0] in line) and rule[1] in line):
            a = line.index(rule[0])
            b = line.index(rule[1])
            #print(rule, a, b)
            if (a > b and mode == 0):
                unpasses.append(line)
                return
            elif (a > b and mode == 1):
                return 1
    return 0

def swaps(line):
    for x in range(0, len(rules)):
        rule = rules[x]
        if (rule[0] in line and rule[1] in line):
            a = line.index(rule[0])
            b = line.index(rule[1])
            if (a > b):
                temp = line[a]
                line[a] = line[b]
                line[b] = temp
    #print(line)

for x in range (0, 1379):
    #print(grabs)
    # Separate the instructions from the updates
    grabs = grabs.strip()
    if ("|" in grabs):
        rules.append(grabs)
    elif ("," in grabs):
        manuals.append(grabs)
    grabs = instructs.readline()

# Split so we can use indices and make them ints
for x in range (0, len(rules)):
    rules[x] = rules[x].split("|")
    for y in range (0, len(rules[x])):
        rules[x][y] = int(rules[x][y])
for x in range (0, len(manuals)):
    manuals[x] = manuals[x].split(",")
    for y in range (0, len(manuals[x])):
        manuals[x][y] = int(manuals[x][y])

for x in range (0, len(manuals)):
    inspect(manuals[x], mode)

#print(unpasses)
mode = 1
for x in range (0, len(unpasses)):
    okay = 1
    while (okay):
        swaps(unpasses[x])
        okay = inspect(unpasses[x], mode)
#print(unpasses)

for x in range (0, len(unpasses)):
    middle = len(unpasses[x]) / 2
    middle = math.ceil(middle) - 1
    total = total + unpasses[x][middle]
    #print(middle)

#print(rules)
#print(manuals)

print("The total is " + str(total))

instructs.close()