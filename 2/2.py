# Dicts to translate
opPlays = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}
myPlays = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}
scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}
outcomes = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

def getScore(opChar, myChar):
    opMove = opPlays[opChar]
    myMove = myPlays[myChar]
    if opMove == myMove:
        return 3 + scores[myMove]
    elif opMove == 'rock':
        if myMove == 'paper':
            return 6 + scores[myMove]
        else:
            return 0 + scores[myMove]
    elif opMove == 'paper':
        if myMove == 'scissors':
            return 6 + scores[myMove]
        else:
            return 0 + scores[myMove]
    else:
        if myMove == 'rock':
            return 6 + scores[myMove]
        else:
            return 0 + scores[myMove]

def getDesiredScore(opChar, outcome):
    opMove = opPlays[opChar]
    desiredOutcome = outcomes[outcome]
    if desiredOutcome == 'draw':
        return 3 + scores[opMove]
    elif desiredOutcome == 'lose':
        if opMove == 'rock':
            return 0 + scores['scissors']
        elif opMove == 'paper':
            return 0 + scores['rock']
        else:
            return 0 + scores['paper']
    else:
        if opMove == 'rock':
            return 6 + scores['paper']
        elif opMove == 'paper':
            return 6 + scores['scissors']
        else:
            return 6 + scores['rock']

# Read all data from file split by line
data = open("input.txt", "r").read().split("\n")
myScore = 0
myScorePart2 = 0
for game in data:
    myScore += getScore(game[0], game[2])
    myScorePart2 += getDesiredScore(game[0], game[2])
print(myScore)
print(myScorePart2)