comp = open("2024/Inputs/D17.txt")

def run(instruction, operand):
    global rega, regb, regc, outputs, pointer, flag
    combo = None
    mathhelp = 0

    match operand: # Find what number we're working with depending on the combo
        case 0 | 1 | 2 | 3:
            combo = operand
        case 4:
            combo = rega
        case 5:
            combo = regb
        case 6:
            combo = regc
    match instruction:
        case 0: #adv
            mathhelp = rega / (2**combo)
            rega = int(mathhelp)
        case 1: #bxl
            mathhelp = regb ^ operand
            regb = mathhelp
        case 2: #bst
            mathhelp = combo % 8
            regb = mathhelp
        case 3: #jnz
            if (rega == 0):
                return
            else:
                pointer = operand
                flag = True
        case 4: #bxc
            mathhelp = regb ^ regc
            regb = mathhelp
        case 5: #out
            mathhelp = combo % 8
            outputs.append(mathhelp)
        case 6: #bdv
            mathhelp = rega / (2**combo)
            regb = int(mathhelp)
        case 7: #cdv
            mathhelp = rega / (2**combo)
            regc = int(mathhelp)
    return

# Sort stuff
file = comp.read().splitlines()
rega = int(file[0].replace("Register A: ", ""))
regb = int(file[1].replace("Register B: ", ""))
regc = int(file[2].replace("Register C: ", ""))
program = (file[4].replace("Program: ", "")).split(",")
for x in range(0, len(program)):
    program[x] = int(program[x])

# Other necessary variables
pointer = 0
outputs = []
flag = False
construct = ""

while(not (pointer > len(program) - 1)):
    flag = False
    run(program[pointer], program[pointer + 1])
    if (flag):
        continue
    else:
        pointer += 2

for i in outputs:
    construct = construct + (str(i) + ',')
construct = construct[:-1]

print("Reg A", rega)
print("Reg B", regb)
print("Reg C", regc)
print(outputs)
print(construct)

comp.close()