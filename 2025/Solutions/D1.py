# PART 2
ticks = open("2025/Inputs/D1.txt")
position = 50
stops = []
passes = 0

for tick in ticks.readlines():
    direction = tick[0]
    click = int(tick[1:])

    passes = passes + int(click / 100)
    click = click % 100

    if direction == 'L':
        stop = position - click
        end = stop
        if stop < 0:
            stop = stop + 100
    else:
        stop = position + click
        end = stop
        if stop > 99:
            stop = stop - 100
    
    print(tick.strip(), position, end)

    # Handle passes
    if position == 0 or end == 0:
        pass
    else:
        if (position > 0 and end < 0) or (position > 0 and end > 100):
            # print("Passed 0")
            passes = passes + 1
     
    stops.append(stop)

    position = stop

print(f"0s in the combo: {stops.count(0) + passes}")

'''
PART 1
ticks = open("2025/Inputs/D1.txt")
position = 50
stops = []

Notes: 100 ticks is a full rotation, so the number would remain the same. Exclude full revolutions first?

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
'''