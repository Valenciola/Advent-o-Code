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
    red = 0
    green = 0
    blue = 0
    power = 0
    # print(line)

    line = line.replace(line[0:2], "", 1)
    line = line.replace(";", "")
    
    for x in line:
        # print(line)
        if(x.isdigit()):
            piece = piece + x
            line = line.replace(line[0:1], "", 1)
            # print("Piece is " + piece)
        elif(x == "g"):
            if (int(piece) > int(green)):
                green = int(piece)
                piece = ""
            else:
                piece = ""
                continue
            
            # print("green is " + str(green))
            line = line.replace("g", "", 1)
        elif(x == "b"):
            if (int(piece) > int(blue)):
                blue = int(piece)
                piece = ""
            else:
                piece = ""
                continue
            
            # print("blue is " + str(blue))
            line = line.replace("b", "", 1)
        elif(x == "r"):
            if (int(piece) > int(red)):
                red = int(piece)
                piece = ""
            else:
                piece = ""
                continue
            
            # print("red is " + str(red))
            line = line.replace("r", "", 1)
    print("Green, blue, and red respectively are " + str(green), str(blue), str(red))
    power = red * green * blue
    return power

# Visual Running
for x in range(1, 101):
    cubes = games.readline()
    cubes = simplify(cubes)
    cubes = interpret(cubes)
    print("From line " + str(x) + " we get " + str(cubes))
    # print("From the first line, we got " + str(cubes))
    possibilities.append(cubes)


for x in possibilities:
    total = total + int(x)

print(total)


games.close()