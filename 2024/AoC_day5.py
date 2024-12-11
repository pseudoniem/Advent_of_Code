from AoC_input_day5 import AoC_input_test as inp_test, AoC_input as inp_real
import math
sgn = lambda x: math.copysign(1, x)
inp = inp_real

inp = inp.split('\n\n')
order = inp[0]
lines = inp[1]

order = [tuple(rule.split('|')) for rule in order.split('\n')]
lines = lines.split('\n')
lines = [line.split(',') for line in lines]
lines = [[num for num in line] for line in lines]


middle_numbers = []
for line in lines:
    middle_num = int(line[int(len(line)/2)])
    while line:
        num = line.pop()
        rest = set(line)
        if rules := {rule[1] for rule in order if rule[0] == num}:
            if rest & rules:
                break

    if not line:
        middle_numbers.append(int(middle_num))

print(f"Antwoord deel 1: {sum(middle_numbers)}")


# def move_before(line, a, b):
#     if (a, b) in order:
#         i_a = line.index(a)
#         i_b = line.index(b)
#         ord = sgn(i_b - i_a)
#         line.sort(key=lambda ab: )