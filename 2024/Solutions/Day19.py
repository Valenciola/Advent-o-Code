import itertools
towelpats = open("2024/Inputs/D19.txt")

# Functions

def towelpower(design, patterns, focus = ""):
    #print(focus)
    if not design.startswith(focus): # Kinda constructing the line up
        return False

    if focus == design: # We got it
        return True
    
    return any(towelpower(design, patterns, focus + swatch) for swatch in patterns) # If we get a true then we're set

def puzzle(design, patterns): # A garbage approach that will keep me up at night
    good = 0
    forks = ['']
    while (forks):
        term = forks.pop(0)
        #print(term)
        if term == design:
            good += 1
            continue
        if design.startswith(term):
            for i in patterns:
                if (i[0] == design[len(term)]):
                    forks.append(term + i)
        else:
            continue
    return good



# Towls, patterns
towels = towelpats.read().splitlines()
patterns = towels[0].replace(" ", "").split(",")
towels.pop(0)
towels.pop(0)
patterns.sort(key=len)

#print(patterns)

# Necessary variables
possibles = []
possibilities = 0

for i in towels:
    #print(i)
    if towelpower(i, patterns):
        #print("Good!\n")
        possibles.append(i)
    else:
        #print("No good!\n")
        continue
        #test = input("")

for i in possibles:
    print(i)
    possibilities += puzzle(i, patterns)
print(possibilities)

towelpats.close()