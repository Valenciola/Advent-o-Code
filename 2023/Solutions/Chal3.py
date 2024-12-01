# Variables
gears = []
symbols = ["*", "&", "@", "%", "+", "=", "#", "/", "$", "-"]
lopp = ""
mechanism = open("Inputs/Chal3.txt", "r")
total = 0
ratios = []
# Keep in mind that each line is 140 chars long and we got 140 lines

for x in mechanism:
    lopp = lopp + x


# print(lopp)
# print(lopp[19])

'''
def looksee(position):
    print("The stuff around position " + str(x) + " (" + lopp[x] + ")")
    print(lopp[position - 141 - 1])
    print(lopp[position - 141])
    print(lopp[position - 141 + 1])
    print(lopp[position - 1])
    print(lopp[position + 1])
    print(lopp[position + 141 - 1])
    print(lopp[position + 141])
    print(lopp[position + 141 + 1])
'''

def looksee(position):
    # print("The stuff around position " + str(x) + " (" + lopp[x] + ")")
    positions = []
    if (lopp[position - 141 - 1].isdigit()):
        positions.append(position - 141 - 1)
    if(lopp[position - 141].isdigit()):
        positions.append(position - 141)
    if(lopp[position - 141 + 1].isdigit()):
        positions.append(position - 141 + 1)
    if(lopp[position - 1].isdigit()):
        positions.append(position - 1)
    if(lopp[position + 1].isdigit()):
        positions.append(position + 1)
    if(lopp[position + 141 - 1].isdigit()):
        positions.append(position + 141 - 1)
    if(lopp[position + 141].isdigit()):
        positions.append(position + 141)
    if(lopp[position + 141 + 1].isdigit()):
        positions.append(position + 141 + 1)
    return positions

def search(places):
    reply = 0
    boadd = []
    skip = []
    for x in places:
        boadd.clear()
        y = x
        z = x
        while (lopp[y] != '.' and lopp[y] not in symbols):
            y = y - 1
        y = y + 1
        boadd.append(y)

        while (lopp[z] != '.' and lopp[z] not in symbols):
            z = z + 1
        z = z - 1
        boadd.append(z)
        # print(boadd)
        gears.append(extract(boadd, skip))

def extract(boundary, skips):
    x = boundary[0]
    y = boundary[1]
    cat = ""
    for z in range (x, y + 1):
        if z in skips:
            break
        else:
            cat = cat + lopp[z]
    skips.append(x)
    skips.append(y)
    # print(cat)
    return cat

def trail(ratiolas):
    total = 1
    # print(ratiolas)
    for x in range(0, len(ratiolas)):
        if (ratiolas[x].isdigit()):
            if (ratiolas[x - 1] == '|' and ratiolas[x + 1] == '|'):
                total = 0
                pass
            else:
                print("Taking " + str(ratiolas[x]))
                total = total * int(ratiolas[x])
        else:
            print("We got a gear with value " + str(total))
            ratios.append(total)
            total = 1

'''
def ration(numbers):
    total = 1
    for x in numbers:
        total = total * int(numbers[x])
    ratios.append(total)
'''

for x in range (0, len(lopp)):
    drawer = 0
    extracts = []
    if (x < 140):
        pass
    elif (lopp[x] == '.'):
        pass
    elif (lopp[x] in symbols):
        drawer = looksee(x)
        search(drawer)
        gears.append("|")
        # print(gears)

# Boring laundry stuff
while '' in gears:
    gears.remove('')

for x in range(0, len(gears)):
    if ('\n' in gears[x]):
        gears[x] = gears[x].strip()

trail(gears)
# print(ratios)
# print(gears)


# Totaling

for x in range(0, len(ratios)):
    print(ratios[x])
    total = total + int(ratios[x])


print(total)

mechanism.close()