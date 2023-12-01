# Variables
calis = open("Inputs/Chal1.txt", "r")
strng = ""
total = 0
translates = []

# Functions
def decode(line):
    #Replaces the weirdo strings with numbers
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
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
    strng = decode(strng)
    strng = clean(strng)
    strng = calib(strng)
    print("From line " + str(x) + " we get " + strng)
    translates.append(strng)


for x in translates:
    total = total + int(x)

print (total)


calis.close()