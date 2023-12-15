init = open("Inputs/Chal15.txt", "r")
seq = init.read()
cat = ""
strngs = []
hashes = []
total = 0

def hash(line):
    val = 0
    for x in line:
        val = val + ord(x)
        val = val * 17
        val = val % 256
    return val

for x in seq:
    if(x == ','):
        strngs.append(cat)
        cat = ""
    else:
        cat = cat + x
strngs.append(cat)

for x in strngs:
    doma = hash(x)
    hashes.append(doma)

for x in hashes:
    total = total + x

print(total)

init.close()