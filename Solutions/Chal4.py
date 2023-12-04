cards = open("Inputs/Chal4.txt", "r")
points = []
total = 0

# The colon in all cards is character 9 (or 8 for the code)
# Numbers never occur twice in the same line (unless they're winning, of course)

# Functions
def clean(array):
    # Get rid of extra characters and unnecessary stuff
    while ':' in array:
        array.remove(':')
    while '' in array:
        array.remove('')
    while '|' in array:
        array.remove('|')
    while '\n' in array:
        array.remove('\n')
    array.append(' ')

def interpret(array):
    # Read the array and get the numbers
    copy = []
    # print(copy)
    num = ""
    for x in array:
        # print("Num is " + num)
        if(x.isdigit()):
            num = num + x
        else:
            copy.append(num)
            num = ""

        while ' ' in copy:
            copy.remove(' ')
        
        clean(copy)
        copy.pop(len(copy) - 1)

    return copy

def compare (wins, gives):
    matches = 0
    for x in wins:
        if x in gives:
            matches = matches + 1
        else:
            pass
    return matches

def add(matches):
    value = 0
    for x in range (1, matches + 1):
        # print("x is " + str(x))
        if (x == 1):
            value = 1
        else:
            value = value * 2
    # print("End value is " + str(value))
    return value

# Visual
for x in range (1, 206):
    card = cards.readline()
    code = 0
    pairs = 0
    winnings = []
    givens = []

    # Initial Read
    for x in range (8, len(card)):
        if (card[x] == '|'):
            code = 1
        
        if (code == 1):
            givens.append(card[x])
        else:
            winnings.append(card[x])

    # Polishing
    clean(winnings)
    winnings = interpret(winnings)
    # print(winnings)
    clean(givens)
    givens = interpret(givens)
    # print(givens)

    # Actual Work
    pairs = compare(winnings, givens)
    # print("We found " + str(pairs) + " matches.")
    points.append(add(pairs))

print(points)

for x in points:
    total = total + x

print(total)

cards.close()