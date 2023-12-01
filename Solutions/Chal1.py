# Variables
calis = open("Inputs/Chal1.txt", "r")
strng = ""
total = 0
translates = []

# Functions
def decode(line):
    #Replaces the weirdo strings with numbers
    line = line.replace("one", "1")
    line = line.replace("two", "2")
    line = line.replace("three", "3")
    line = line.replace("four", "4")
    line = line.replace("five", "5")
    line = line.replace("six", "6")
    line = line.replace("seven", "7")
    line = line.replace("eight", "8")
    line = line.replace("nine", "9")
    line = line.replace("ten", "10")
    return line

def clean(line):
    for x in line:
        if not (x.isdigit()):
            line = line.replace(x, "")
    return line

def calib(line):
    full = []
    for x in line:
        full.append(x)
    line = (full[0] + full[len(full) - 1])
    return line

# Visual Things
for x in range (1, 1001):
    strng = calis.readline()
    # strng = decode(strng)
    strng = clean(strng)
    strng = calib(strng)
    print("From line " + str(x) + " we get " + strng)
    translates.append(strng)


for x in translates:
    total = total + int(x)

print (total)

calis.close()