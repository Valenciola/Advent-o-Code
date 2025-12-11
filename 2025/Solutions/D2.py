ranges = open("2025/Inputs/D2.txt", "r")
checks = []
ids = []
total = 0

for ran in ranges.read().split(','):
    checks = []
    invalids = []

    ran = ran.split('-')
    start = ran[0]
    end = ran[1]
    
    for i in range(0, len(ran)):
        if (len(ran[i]) % 2) == 0:
            checks.append(i)
        else:
            pass
    
    start = int(start)
    end = int(end)

    if not (checks == []):
        for x in checks:
            grab = int(len(ran[x]) / 2)
            half = (ran[x][0:grab])
            # print(ran, half)
            
            check = half + half
            if x == 0:
                while (int(check) <= end):
                    check = half + half
                    # print(check)
                    if start <= int(check) <= end:
                        # print("Accept " + check)
                        invalids.append(int(check))
                    
                    half = str(int(half) + 1)
            else:
                while (int(check) >= start) and int(half) > 0:
                    check = half + half
                    # print(check)
                    if start <= int(check) <= end:
                        # print("Accept " + check)
                        invalids.append(int(check))
                    
                    half = str(int(half) - 1)
            
            

        invalids = list(set(invalids))
        # print(invalids)
        if not invalids == []:
            ids.append(invalids)
    
    print(ran, sorted(invalids))

# print(ids)

for run in ids:
    for digit in run:
        total = total + digit

print(total)