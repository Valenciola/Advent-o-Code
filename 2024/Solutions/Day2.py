levels = open("2024/Inputs/D2.txt", "r")
safes = 0

def assess():
    determine = seps[1] - seps[0]
    if (determine > 0):
        determine = 1
    elif (determine < 0):
        determine = 0
    else:
        return 0
    
    for x in range (0, len(seps) - 1):
        chart = seps[x + 1] - seps[x]
        if (chart == 0):
            return 0
        elif ((abs(chart) < 1) or (abs(chart)) > 3):
            return 0
        elif ((chart > 0 and determine == 0) or (chart < 0 and determine == 1)):
            return 0
    return 1

for x in range (0, 1000):
    level = levels.readline()
    seps = level.split()

    for x in range (0, len(seps)):
        seps[x] = int(seps[x])
    
    if (assess()):
        safes = safes + 1

print("The amount of safe levels is " + str(safes))