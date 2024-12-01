init = open("Inputs/Chal15.txt", "r")
seq = init.read()
cat = ""
strngs = []
hashes = []
box = []
total = 0

def hash(line):
    val = 0
    for x in line:
        val = val + ord(x)
        val = val * 17
        val = val % 256
    return val

def getlab(line):
    kit = ""
    for x in line:
        if (x == '=' or x == '-' or x == ' '):
            break
        else:
            kit = kit + x
    # print(kit)
    return kit

def consid(array, line):
    # print(line)
    label = getlab(line)
    # print(label)
    box = 0
    lens = ''
    construct = ""
    flag = True
    if '-' in line:
        # Removal
        for x in range(0, len(array)):
            toma = array[x]
            toma = getlab(toma)
            if (label == toma):
                array.pop(x)
                break
            else:
                continue 
    elif '=' in line:
        # Additions
        for x in range(0, len(array)):
            # Check for duplicates (false if there is one)
            toma = array[x]
            toma = getlab(toma)
            if (label == toma):
                toma = x
                flag = False
                break

        box = hash(label)
        lens = line[len(label) + 1]
        construct = label + " " + lens + "." + str(box)
        if flag == True:
            array.append(construct)
        else:
            array[toma] = construct

def focals(array, box):
    box = str(box)
    lenses = []
    power = 0
    inbox = 0
    bo = 0
    for x in array:
        # Search by box
        bo = x.index('.')
        bo = x[bo + 1:len(x)]
        # print(bo)
        if (bo == box):
            lenses.append(x)
        else:
            continue
    # print(lenses)

    if len(lenses) == 0:
        return 0
    else:
        pass

    box = int(box) + 1
    for x in lenses:
        # Parse each box
        # print(x)
        tare = x.index(' ')
        tore = x.index('.')
        slot = lenses.index(x) + 1
        focal = int(x[tare + 1:tore])
        # print(box, slot, focal)
        power = box * slot * focal
        # print(power)
        inbox = inbox + power
    return inbox

for x in seq:
    if(x == ','):
        strngs.append(cat)
        cat = ""
    else:
        cat = cat + x
strngs.append(cat)

# print(strngs)

for x in strngs:
    consid(box, x)

print(box)

for x in range(0, 256):
    total = total + focals(box, x)

print(total)

'''
~ Part 1 Implementations ~
for x in strngs:
    doma = hash(x)
    hashes.append(doma)

for x in hashes:
    total = total + x
'''

init.close()