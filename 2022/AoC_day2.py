import AoC_input_day2 as input

def points_in_strategie(y):
    x = y.split('\n')
    points = 0
    for i in x:
        if i == "A X":
            points += 1+3
        elif i == "A Y":
            points += 2+6
        elif i == "A Z":
            points += 3+0
        elif i == "B X":
            points += 1+0
        elif i == "B Y":
            points += 2+3
        elif i == "B Z":
            points += 3+6
        elif i == "C X":
            points += 1+6
        elif i == "C Y":
            points += 2+0
        elif i == "C Z":
            points += 3+3
    
    return points


def points_in_strategie2(y):
    x = y.split('\n')
    points = 0
    for i in x:
        if i == "A X":
            points += 0+3
        elif i == "A Y":
            points += 3+1
        elif i == "A Z":
            points += 6+2
        elif i == "B X":
            points += 0+1
        elif i == "B Y":
            points += 3+2
        elif i == "B Z":
            points += 6+3
        elif i == "C X":
            points += 0+2
        elif i == "C Y":
            points += 3+3
        elif i == "C Z":
            points += 6+1
    
    return points


points_in_strategie(inp.strategie)


points_in_strategie2(inp.strategie)