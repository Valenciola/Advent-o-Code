calinote = open("2024/Inputs/D7.txt", "r")
tests = []
givens = []
ops = ['+', '*', '.']
binary = [] # It's not really binary anymore but I didn't wanna change the name
possibles = []
cal = 0

def bincombs(n):
    for i in range(3**n):
        binarystr = ""
        num = i
        for _ in range(n):
            binarystr = str(num % 3) + binarystr
            num //= 3 # Turns out that we don't need to typecast because // does integer division
        binary.append(binarystr)

def understand(string):
    #print(string)
    if (string.isdigit()):
        #print(string)
        string = int(string)
        return string
    else:
        thought = ""
        opps = 0
        temp = []
        for t in range(0, len(string)):
            if (opps == 2):
                break
            elif (not string[t].isdigit()):
                opps += 1
                temp.append(string[t])
            thought = thought + string[t]
        if (not thought[len(thought) - 1].isdigit()):
            thought = thought[:-1]
        
        if (temp[0] == '.'):
            temp = thought.split('.')
            rep = str(temp[0]) + str(temp[1])
        else:
            rep = str(eval(thought))

        string = string.replace(thought, rep, 1)
        return understand(string)


for x in range(0, 850):
	# Read the lines and split into tests and givens
    line = calinote.readline()
    line = line.split(':')
    tests.append(int(line[0]))
    line = line[1].strip()
    line = line.split()
    for y in range(0, len(line)):
        line[y] = int(line[y])
    givens.append(line)

#print(tests)
#print(givens)
print(len(tests))

for x in range(0, len(givens)):
    print(x, givens[x])
    poss = len(givens[x]) - 1
    #print(poss)
    binary = []
    bincombs(poss)
    #print(binary)
    for a in range(0, len(binary)):
        craft = ""
        for b in range(0, len(givens[x]) + poss):
            if (b % 2 == 0):
                craft = craft + str(givens[x][int(b / 2)])
            else:
                craft = craft + ops[int(binary[a][int(b / 2)])]
            #print(b, craft)
        #print(craft)
        tocomp = understand(craft)
        if (tocomp == tests[x]):
            possibles.append(tests[x])
            break
        else:
            continue

print("\nAre you ready?")
print(possibles)

for i in range(0, len(possibles)):
    cal += possibles[i]

print(cal)

calinote.close()