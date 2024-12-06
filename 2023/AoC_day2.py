import AoC_input_day2 as inp
import math

l_input = [line.split(': ') for line in inp.AoC_input.split('\n')]
d_input = {int(l[0].removeprefix('Game ')): tuple(l[1].split('; ')) for l in l_input}
print(l_input)
print(d_input)

# Reformat to RGB-tuples:
for k, v in d_input.items():
    d_input[k] = tuple(i.split(', ') for i in v)

print(d_input)

def make_RGB_tuple(tlist):
    (red, green, blue) = (0, 0, 0)

    for i in tlist:
        if i.endswith(' red'):
            red = int(i.removesuffix(' red'))
        elif i.endswith(' green'):
            green = int(i.removesuffix(' green'))
        elif i.endswith(' blue'):
            blue = int(i.removesuffix(' blue'))
        else:
            print(i, ' has no red, green or blue. WTF!!')

    return (red, green, blue)

for k,v in d_input.items():
    v = tuple(make_RGB_tuple(i) for i in v)
    d_input[k] = v

print(d_input)
print('====================================================================================================')
print()

max_red = 12
max_green = 13
max_blue = 14

def possible_combination(t):
    if t[0] > max_red or t[1] > max_green or t[2] > max_blue:
        return False
    else:
        return True


def possible_game(t):
    if sum(possible_combination(hand) for hand in t) < len(t):
        return False
    else:
        return True


print("Antwoord deel 1:", sum(k for k,v in d_input.items() if possible_game(v)))
print()
print('==================================================================================')
print()

def min_tuple(game):
    return tuple(max(t[i] for t in game) for i in range(3))


power_of_games = {k: math.prod(min_tuple(v)) for k, v in d_input.items()}


print("Antwoord deel 2:", sum(v for v in power_of_games.values()))