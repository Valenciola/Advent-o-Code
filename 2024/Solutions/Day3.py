import re

memoryFile = open("2024/Inputs/D3.txt", "r")
memory = ""

for x in range (0, 6):
    memory = memory + memoryFile.readline()
    memory.replace("\n", "")

muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)
multinums = []
total = 0
flag = 1

matchin = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", memory, re.IGNORECASE)
matchins = []
for match in matchin:
    matchins.append(match.start())

do = re.finditer(r"do\(\)", memory, re.IGNORECASE)
dos = []
for match in do:
    dos.append(match.start())

dont = re.finditer(r"don't\(\)", memory, re.IGNORECASE)
donts = []
for match in dont:
    donts.append(match.start())


# Final split and calculations
for x in range (0, len(muls)):
    muls[x] = muls[x].replace("mul(", "")
    muls[x] = muls[x].replace(")", "")
    multinums.append(muls[x].split(","))

for x in range (0, matchins[len(matchins) - 1] + 1):
    #print(x)
    if (x in dos):
        flag = 1
        #print("a do")
    elif (x in donts):
        flag = 0
        #print("a don't")
    
    if ((x in matchins) and (flag)):
        #print("A match!")
        chap = matchins.index(x)
        multi = int(multinums[chap][0]) * int(multinums[chap][1])
        total = total + multi
    else:
        continue

print("Total multiplications gets us to " + str(total))

memoryFile.close()