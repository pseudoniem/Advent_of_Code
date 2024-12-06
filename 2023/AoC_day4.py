import AoC_input_day4 as inp
import math

l_input = [line.split(': ') for line in inp.AoC_input.split('\n')]
d_input = {int(l[0].lstrip('Card ')): tuple(l[1].split(' | ')) for l in l_input}
print(l_input)
print(d_input)

# Reformat:
for k, v in d_input.items():
    d_input[k] = tuple(set(i.split(' ')).difference({''}) for i in v)

for k, v in d_input.items():
    d_input[k] = ({int(i) for i in v[0]}, {int(i) for i in v[1]})
print(d_input)


cards_with_points = {k: 2 ** (len(v[0].intersection(v[1])) - 1) if v[0].intersection(v[1]) != set() else 0 for k, v in d_input.items()}

print(cards_with_points)

print("Antwoord deel 1:", sum(v for v in cards_with_points.values()))
print()
print('==================================================================================')
print()


cards_with_wins = {k: len(v[0].intersection(v[1])) if v[0].intersection(v[1]) != set() else 0 for k, v in d_input.items()}
number_of_cards = {k: 1 for k in cards_with_points}

for i in range(len(number_of_cards)):
    i += 1
    for _ in range(number_of_cards[i]):
        for j in range(cards_with_wins[i]):
            j += 1
            number_of_cards[i + j] += 1

print("Antwoord deel 2:", sum(v for v in number_of_cards.values()))