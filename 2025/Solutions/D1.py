ticks = open("2025/Inputs/D1.txt")
position = 50
stops = []

'''
Notes: 100 ticks is a full rotation, so the number would remain the same. Exclude full revolutions first?
'''

for tick in ticks.readlines():
    direction = tick[0]
    click = int(tick[1:])

    click = click % 100

    if direction == 'L':
        stop = position - click
        if stop < 0:
            stop = stop + 100
    else:
        stop = position + click
        if stop > 99:
            stop = stop - 100
    
    stops.append(stop)

    position = stop

print(f"0s in the combo: {stops.count(0)}")