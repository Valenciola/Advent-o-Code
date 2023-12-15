card = open("Inputs/Chal7.txt", "r")
cardline = None
cards = []
bids = []
cat = ""
ranks = []
total = 0

# Read stuff in the input
for x in range(1, 1001):
    cardline = card.readline()
    ranks.append(1)
    for y in cardline:
        cat = cat + y
        if (y == " "):
            cat = cat.strip(' ')
            cards.append(cat)
            cat = ""
        elif (y == "\n"):
            cat = cat.strip()
            cat = int(cat)
            bids.append(cat)
            cat = ""
cat = cat.strip()
cat = int(cat)
bids.append(cat)

def determine(card):
    # Read in terms of [A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2]
    # print(card)
    # J is arms[3]
    mode = 0
    arms = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in card:
        # print(x)
        if (x == 'A'):
            arms[0] = arms[0] + 1
        elif (x == 'K'):
            arms[1] = arms[1] + 1
        elif (x == 'Q'):
            arms[2] = arms[2] + 1
        elif (x == 'J'):
            arms[3] = arms[3] + 1
        elif (x == 'T'):
            arms[4] = arms[4] + 1
        elif (x == '9'):
            arms[5] = arms[5] + 1
        elif (x == '8'):
            arms[6] = arms[6] + 1
        elif (x == '7'):
            arms[7] = arms[7] + 1
        elif (x == '6'):
            arms[8] = arms[8] + 1
        elif (x == '5'):
            arms[9] = arms[9] + 1
        elif (x == '4'):
            arms[10] = arms[10] + 1
        elif (x == '3'):
            arms[11] = arms[11] + 1
        elif (x == '2'):
            arms[12] = arms[12] + 1
    # print(arms)
    if ((arms.count(5) == 1) or (arms[3] == 4 and arms.count(1) == 1) or (arms[3] == 1 and arms.count(4) == 1)):
        # Five of a kind
        mode = 7
    elif ((arms.count(4) == 1 and arms.count(1) == 1) or (arms[3] == 3 and arms.count(1) == 2) or (arms.count(3) == 1 and arms[3] == 1 and arms.count(1) == 2) or (arms.count(2) == 2 and arms[3] == 2 and arms.count(1) == 1)):
        # Four of a kind
        mode = 6
    elif ((arms.count(3) == 1 and arms.count(2) == 1) or (arms.count(2) == 2 and arms[3] == 1 and arms.count(1) == 1)):
        # Full house
        mode = 5
    elif ((arms.count(3) == 1 and arms.count(1) == 2) or (arms[3] == 2 and arms.count(1) == 3) or (arms.count(2) == 1 and arms[3] == 1 and arms.count(1) == 3)):
        # Three of a kind
        mode = 4
    elif ((arms.count(2) == 2 and arms.count(1) == 1) or (arms.count(2) == 1 and arms[3] == 1 and arms.count(1) == 3)):
        # Two pair
        mode = 3
    elif ((arms.count(2) == 1 and arms.count(1) == 3) or (arms[3] == 1 and arms.count(1) == 5)):
        # One pair
        mode = 2
    else:
        # High card
        mode = 1
    
    # print(mode)
    return mode

def adjust(array):
    # Adjust in case of no card being assigned a 1
    if not (1 in array):
        for x in range(0, len(array)):
            array[x] = array[x] - 1

def flip(text):
    return text[::-1]

def compare(array, term, cards):
    # Compare cards by card
    # [A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2]
    indices = []
    decodes = []
    counter = 0
    for x in range(0, len(array)):
        if (array[x] == term):
            indices.append(x)
    # print(indices)
    
    if (len(indices) == 1):
        # Don't waste time comparing if there's only one occurence
        return
    else:
        for x in indices:
            # Find card values
            # print(cards[x])
            decodes.append(decode(cards[x]))
    
    # print(decodes)
    
    for x in range(0, len(decodes)):
        # Indicate value and index and then sort
        decodes[x] = float(str(decodes[x]) + '.' + flip(str(indices[x])))
    # print(decodes)
    decodes.sort()
    for x in range(0, len(decodes)):
        decodes[x] = str(decodes[x])

    # print(decodes)

    # print(len(indices))
    for x in range(0, len(array)):
        # Adjust array first
        if (array[x] < term and x not in indices):
            pass
        elif (x not in indices):
            array[x] = array[x] + len(indices) - 1
        else:
            pass
    
    # Find the indices again and stuff I don't really know anymore
    indices.clear()
    # print(decodes, indices)
    
    for x in decodes:
        dot = ""
        regul = x.index('.')
        for y in range(regul + 1, len(x)):
            dot = dot + x[y]
        dot = flip(dot)
        # print(dot)
        indices.append(int(dot))
    
    # print(decodes, indices)
    
    for x in indices:
        # print(counter)
        array[x] = array[x] + counter
        counter = counter + 1
    
    # print(decodes)

def decode(card):
    # [A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2]
    value = 0
    buff = pow(10, (len(card) - 1) * 2)
    for x in card:
        # print(buff)
        if (x == '2'):
            value = value + (2 * buff)
        elif (x == '3'):
            value = value + (3 * buff)
        elif (x == '4'):
            value = value + (4 * buff)
        elif (x == '5'):
            value = value + (5 * buff)
        elif (x == '6'):
            value = value + (6 * buff)
        elif (x == '7'):
            value = value + (7 * buff)
        elif (x == '8'):
            value = value + (8 * buff)
        elif (x == '9'):
            value = value + (9 * buff)
        elif (x == 'T'):
            value = value + (10 * buff)
        elif (x == 'J'):
            value = value + (0 * buff)
        elif (x == 'Q'):
            value = value + (11 * buff)
        elif (x == 'K'):
            value = value + (12 * buff)
        elif (x == 'A'):
            value = value + (13 * buff)
        buff = int(buff / 100)

    # print(card, value)
    return value

# print(cards)
# print(bids)
for x in range(0, len(cards)):
    # Initial rank the cards by type
    # print(x + 1, determine(cards[x]))
    ranks[x] = determine(cards[x])
    # print(cards[x], bids[x], "M" , ranks[x], " ")

adjust(ranks)
# compare(ranks, 1, cards)
# print(ranks)

for x in range(1, 1001):
    compare(ranks, x, cards)
# print(ranks)

for x in range(0, 1000):
    # print(cards[x], bids[x], "R" , ranks[x], " ")
    total = total + (ranks[x] * bids[x])

print(total)

card.close()