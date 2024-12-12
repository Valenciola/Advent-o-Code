mapped = open("2024/Inputs/D11.txt", "r")
row = mapped.readline()
stones = row.split()
for f in stones:
    stones[stones.index(f)] = int(f)

def helpmeh(stones, blinks):
    stoneob = {} # I've literally never touched dictionaries I miss you Javascript ;-;
    cache = {}

    for x in stones:
        if(not x in stoneob):
            stoneob[x] = 0
        stoneob[x] += 1

    for i in range(0, blinks):
        newstoneob = {}
        for s in list(stoneob.keys()):
            stoco = stoneob[s]

            if (not s in cache): # Cache stuff which is fun to explore
                if (s == 0):
                    cache[s] = 1
                elif(len(str(s)) % 2 == 0):
                    broke = int(len(str(s)) / 2)
                    cache[s] = [int(str(s)[0:broke]), int(str(s)[broke:len(str(s))])]
                else:
                    cache[s] = s * 2024
            
            if (len(str(s)) % 2 == 0):
                if (not cache[s][0] in newstoneob):
                    newstoneob[cache[s][0]] = 0
                if (not cache[s][1] in newstoneob):
                    newstoneob[cache[s][1]] = 0
                
                newstoneob[cache[s][0]] += stoco
                newstoneob[cache[s][1]] += stoco
            else:
                if (not cache[s] in newstoneob):
                    newstoneob[cache[s]] = 0
                
                newstoneob[cache[s]] += stoco
            
            for a in newstoneob:
                if newstoneob[a] == 0:
                    del newstoneob[a]
        
        stoneob = newstoneob
    
    stonecount = 0
    for y in stoneob:
        stonecount += stoneob[y]

    return stonecount

print(stones)
sol = helpmeh(stones, 75)
print(sol)

mapped.close()

'''
# The part 1 solution that just wasn't meant to be reused (sobs) rest in comments

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
'''