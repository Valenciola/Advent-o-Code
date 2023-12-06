import math # Floor numbers by doing math.floor(input)
post = open("Inputs/Chal6.txt", "r")
line = post.readline()
times = []
tobeat = []
ways = []
cat = ""
total = 1

def getways(time, record):
    # -x^2 + tx - d
    init = 0
    end = 0
    way = 0
    adjust = False
    square = pow(time, 2)
    init = ((time * -1) + math.sqrt(square - (4 * record))) / -2
    end = ((time * -1) - math.sqrt(square - (4 * record))) / -2
    # print(init, end)
    if(end.is_integer() or init.is_integer()):
        adjust = True
    init = math.floor(init)
    end = math.floor(end)
    way = end - init
    if(adjust == True):
        way = way - 1
    
    # print(way)
    return way


# Initial reads
for x in line:
    if(x.isdigit()):
        cat = cat + x
    else:
        if not (cat == ''):
            cat = int(cat)
            times.append(cat)
            cat = ""
        else:
            pass
line = post.readline() + ' '
for x in line:
    if(x.isdigit()):
        cat = cat + x
    else:
        if not (cat == ''):
            cat = int(cat)
            tobeat.append(cat)
            cat = ""
        else:
            continue

for x in range (0, len(times)):
    ways.append(getways(times[x], tobeat[x]))

print(times)
print(tobeat)
print(ways)

for x in ways:
    total = total * x

print(total)

post.close()