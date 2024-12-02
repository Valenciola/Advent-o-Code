levels = open("2024/Inputs/D2.txt", "r")
safes = 0
reconsiders = []
flag = 0

def assess(nums):
    determine = nums[1] - nums[0]
    if (determine > 0):
        determine = 1
    elif (determine < 0):
        determine = 0
    else:
        return 0
    
    for x in range (0, len(nums) - 1):
        chart = nums[x + 1] - nums[x]
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
    
    if (assess(seps)):
        safes = safes + 1
    else:
        reconsiders.append(seps)

for x in range (0, len(reconsiders)):
    focus = reconsiders[x]
    for y in range (0, len(focus)):
        test = focus.copy()
        test.pop(y)
        if (assess(test)):
            safes = safes + 1
            break
        else:
            continue

print("We see " + str(safes) + " safe levels now...")

levels.close()