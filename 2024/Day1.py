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