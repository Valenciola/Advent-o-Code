# Variables
gears = []
symbols = ["*", "&", "@", "%", "+", "=", "#", "/", "$", "-"]
lopp = ""
mechanism = open("Inputs/Chal3.txt", "r")
total = 0
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
        # print(gears)

# Boring laundry stuff
while '' in gears:
    gears.remove('')

for x in range(0, len(gears)):
    if ('\n' in gears[x]):
        gears[x] = gears[x].strip()

print(gears)

# Totaling

for x in range(0, len(gears)):
    total = total + int(gears[x])


print(total)

mechanism.close()