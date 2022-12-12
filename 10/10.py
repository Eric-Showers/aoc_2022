def updateSignalStrength(regx, cycle, signalStrengthSum):
    if ((cycle + 20) % 40) == 0:
        signalStrengthSum += cycle * regx
    return signalStrengthSum

def getPixel(curCycle, curRegx):
    curPosition = (curCycle - 1) % 40
    if abs(curPosition - regx) > 1:
        return '.'
    else:
        return '#'

cycle = 0
regx = 1
signalStrength = 0
crtString = ''
for instruction in open("input.txt").read().splitlines():
    command = instruction[:4]
    # Start cycle i
    cycle += 1
    # During cycle i
    signalStrength = updateSignalStrength(regx, cycle, signalStrength)
    crtString += getPixel(cycle, regx)
    if command == 'addx':
        value = int(instruction[4:])
        # During cycle i+1
        cycle += 1
        signalStrength = updateSignalStrength(regx, cycle, signalStrength)
        crtString += getPixel(cycle, regx)
        regx += value

print(signalStrength)
for i in range(6):
    print(crtString[i*40:(i+1)*40-1])