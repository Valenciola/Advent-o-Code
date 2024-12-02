'''
# ALL OF THIS WAS PART 1

localist = open("2024/Inputs/D1.txt", "r")
left = []
right = []
total = 0
store = ""

# Split numbers
def sepalist():
    store = localist.readline()
    broken = store.split()
    # print(broken)
    left.append(int(broken[0]))
    right.append(int(broken[1]))
    return

for x in range (1, 1001):
    sepalist()

# Sort in ascending
left.sort()
right.sort()

# Calculate
for x in range (0, 1000):
    total = total + abs(right[x] - left[x])

print("Total distance: " + str(total))

localist.close()
'''

localist = open("2024/Inputs/D1.txt")
left = []
right = []
count = []
store = ""
total = 0

# Split numbers
def sepalist():
    store = localist.readline()
    broken = store.split()
    # print(broken)
    left.append(int(broken[0]))
    right.append(int(broken[1]))
    return

# Get similarity scores
def similarity():
    for x in range (0, len(left)):
        compare = left[x]
        for y in range (0, len(right)):
            if compare == right[y]:
                count[x] = count[x] + 1
            else:
                continue

for x in range (0, 1000):
    sepalist()

for x in range (0, len(left)):
    count.append(0)

similarity()

for x in range (0, 1000):
    total = total + (left[x] * count[x])

print("Total similarity score: " + str(total))