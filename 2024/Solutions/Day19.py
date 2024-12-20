towelpats = open("2024/Inputs/D19.txt")

# Functions

def towelpower(design, patterns, focus = ""):
    #print(focus)
    if not design.startswith(focus): # Kinda constructing the line up
        return False

    if focus == design: # We got it
        return True
    
    return any(towelpower(design, patterns, focus + swatch) for swatch in patterns) # If we get a true then we're set

# Towls, patterns
towels = towelpats.read().splitlines()
patterns = towels[0].replace(" ", "").split(",")
towels.pop(0)
towels.pop(0)
patterns.sort(key=len)

#print(patterns)

# Necessary variables
possibles = []

for i in towels:
    print(i)
    if towelpower(i, patterns):
        print("Good!\n")
        possibles.append(i)
    else:
        print("No good!\n")
        #test = input("")

print(len(possibles)) # why is this wrong (Initial 364, then 309, both are too low but why???)

towelpats.close()