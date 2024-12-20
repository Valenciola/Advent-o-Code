towelpats = open("2024/example.txt")

# Functions

def towelpower(design):
    global patterns
    if (len(design) == 0):
        return 1
    
    top = -1
        
    for i in reversed(patterns):
        if i in design:
            #print(i)
            if (patterns.index(i) > top and design[0] == i[0]):
                top = patterns.index(i)
        else:
            continue
    
    if top > -1:
        if (design[0] in patterns) and not (len(patterns[top]) > 1):
            top = patterns.index(design[0])

        print(patterns[top])    
        design = design.replace(patterns[top], "", 1)
        return towelpower(design)
    else:
        return 0

# Towls, patterns
towels = towelpats.read().splitlines()
patterns = towels[0].replace(" ", "").split(",")
towels.pop(0)
towels.pop(0)
patterns.sort(key=len)

print(patterns)

# Necessary variables
possibles = []

for i in towels:
    print(i, towelpower(i))
    if towelpower(i):
        possibles.append(i)

print(len(possibles))

towelpats.close()