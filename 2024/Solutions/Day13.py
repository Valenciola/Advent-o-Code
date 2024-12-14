# Why is AoC just... pain? What if the Chief Historian doesn't wanna be found? At least then, could we justify all the time we've been wasting???
import math

notes = open("2024/Inputs/D13.txt", "r")
bas = []
bbs = []
prizes = []
total = 0

for _ in range(0, 1279):
    # Get every line and manipulate it
    line = notes.readline()
    if ("Button A" in line):
        line = line.replace("Button A: ", "")
        line = line.replace("X+", "")
        line = line.replace("Y+", "")
        line = line.strip()
        line = line.split(",")
        for x in range(0, len(line)):
            line[x] = int(line[x])
        bas.append(line)
    elif ("Button B" in line):
        line = line.replace("Button B: ", "")
        line = line.replace("X+", "")
        line = line.replace("Y+", "")
        line = line.strip()
        line = line.split(",")
        for x in range(0, len(line)):
            line[x] = int(line[x])
        bbs.append(line)
    elif ("Prize" in line):
        line = line.replace("Prize: ", "")
        line = line.replace("X=", "")
        line = line.replace("Y=", "")
        line = line.strip()
        line = line.split(",")
        for x in range(0, len(line)):
            line[x] = int(line[x])
        prizes.append(line)
    else:
        continue

# Listen... consider we have that ax * aval + bx * bval = px and ay * aval + by * bval = py, where ax, bx, and px (and their y counterparts) are given...

def solve(index):
    # ax * aval + bx * bval = px
    # ay * aval + by * bval = py
    buttona = bas[index]
    buttonb = bbs[index]
    prize = prizes[index]

    prize[0] = prize[0] + 10000000000000
    prize[1] = prize[1] + 10000000000000

    #print(buttona, buttonb, prize)

    b = (buttona[1] * prize[0] - buttona[0] * prize[1]) / (buttona[1] * buttonb[0] - buttona[0] * buttonb[1])
    a = (prize[0] - buttonb[0] * b) / buttona[0]

    # Is this even a valid solution??? (Yeah we gotta tighten security because we got some float imposters hanging around)
    if (a >= 0 and b >= 0 and (math.floor(a) == a) and (math.floor(b) == b)):
        return [int(a), int(b)]
    else:
        return [0, 0]

for x in range(0, len(bas)):
    tokens = solve(x)
    print("Machine", str(x + 1) + ":", tokens, "->", (tokens[0] * 3 + tokens[1]), "token(s)")
    total += tokens[0] * 3 + tokens[1]

print("You'll be spending minimum " + str(total) + " tokens")

notes.close()