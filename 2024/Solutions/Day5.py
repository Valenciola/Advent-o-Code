import math

instructs = open("2024/Inputs/D5.txt", "r")
rules = []
manuals = []
grabs = instructs.readline()
passes = []
total = 0

def inspect(line):
    #print(line)
    for x in range(0, len(rules)):
        rule = rules[x]
        if ((rule[0] in line) and rule[1] in line):
            a = line.index(rule[0])
            b = line.index(rule[1])
            #print(rule, a, b)
            if (a > b):
                #print("bad")
                return
    passes.append(line)
    return

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
    inspect(manuals[x])

for x in range (0, len(passes)):
    middle = len(passes[x]) / 2
    middle = math.ceil(middle) - 1
    total = total + passes[x][middle]
    #print(middle)

#print(rules)
#print(manuals)
#print(passes)

print("The total is " + str(total))

instructs.close()