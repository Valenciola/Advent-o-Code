mapped = open("2024/Inputs/D11.txt", "r")
row = mapped.readline()
stones = row.split()

for f in stones:
    stones[stones.index(f)] = int(f)
print(stones)

for a in range(0, 25):
    print(a)
    for x in range(0, len(stones)):
        #print(stones[x])
        if (stones[x] == 0):
            stones[x] = 1
        elif (len(str(stones[x])) % 2 == 0):
            even = [0, 0]
            even[0] = int(str(stones[x])[0:int(len(str(stones[x])) / 2)])
            even[1] = int(str(stones[x])[int(len(str(stones[x])) / 2):int(len(str(stones[x])))])
            stones[x] = even
        else:
            stones[x] = stones[x] * 2024
    for y in stones:
        if (str(type(y)) == "<class 'int'>"):
            continue
        else:
            if (stones.index(y) == len(stones) - 1):
                stones[len(stones) - 1] = y[0]
                stones.append(y[1])
            else:
                stones.insert(stones.index(y) + 1, y[1])
                stones[stones.index(y)] = y[0]
    #print(stones)

print("We got " + str(len(stones)) + " stones!")

mapped.close()