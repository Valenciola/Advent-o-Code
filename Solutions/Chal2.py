# Variables
games = open("Inputs/Chal2.txt", "r")
total = 0
possibilities = []
cubes = ""

# Functions
def simplify(line):
    # Simplifies each line into my own little code to read
    line = line.replace("Game", "")
    line = line.replace("green", "g")
    line = line.replace("blue", "b")
    line = line.replace("red", "r")
    line = line.replace(" ", "")
    line = line.replace(",", "")
    return line

def interpret(line):
    piece = ""
    # print(line)
    
    for x in line:
        if(x.isdigit()):
            piece = piece + x
            line = line.replace(line[0:1], "", 1)
            # print(line)
        elif(x == ":"):
            identi = int(piece)
            line = line.replace(piece + ":", "", 1)
            piece = ""
        elif(x == "g"):
            if (int(piece) > 13):
                identi = 0
                break
            else:
                piece = ""
                line = line.replace(line[0:1], "", 1)
                # print(line)
                continue
        elif(x == "b"):
            if (int(piece) > 14):
                identi = 0
                break
            else:
                piece = ""
                line = line.replace(line[0:1], "", 1)
                # print(line)
                continue
        elif(x == "r"):
            if (int(piece) > 12):
                identi = 0
                break
            else:
                piece = ""
                line = line.replace(line[0:1], "", 1)
                # print(line)
                continue
    return identi

# Visual Running
for x in range (1, 101):
    cubes = games.readline()
    cubes = simplify(cubes)
    cubes = interpret(cubes)
    print("From line " + str(x) + " we get " + str(cubes))
    possibilities.append(cubes)

for x in possibilities:
    total = total + int(x)

print(total)

games.close()