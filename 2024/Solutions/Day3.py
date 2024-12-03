import re

memoryFile = open("2024/Inputs/D3.txt", "r")
memory = ""

for x in range (0, 6):
    memory = memory + memoryFile.readline()
    memory.replace("\n", "")

muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)
multinums = []
total = 0


for x in range (0, len(muls)):
    muls[x] = muls[x].replace("mul(", "")
    muls[x] = muls[x].replace(")", "")
    multinums.append(muls[x].split(","))

for x in multinums:
    if (not(x[0].isdigit() and x[1].isdigit())):
        multinums.remove(x)

for x in range (0, len(multinums)):
    multi = int(multinums[x][0]) * int(multinums[x][1])
    total = total + multi

print("Total multiplications gets us to " + str(total))

# 189331402 is too low

memoryFile.close()