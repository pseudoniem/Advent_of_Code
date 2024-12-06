from AoC_input_day2 import AoC_input_test as inp_test, AoC_input as inp_real

import math

inp = inp_real

l_in = [line.split(' ') for line in inp.split('\n')]
l_in = [[int(num) for num in line] for line in l_in]


safe1 = []
safe2 = []

def safe_line(line):
    if max(line) == line[0]: #Afnemend
        r = -1
    elif max(line) == line[-1]: #Toenemend
        r = 1
    else:
        r = 0
    return all(r * (line[i + 1] - line[i]) in [1, 2, 3] for i in range(len(line) - 1))


for line in l_in:
    if safe_line(line):
        safe1.append(line)
        safe2.append(line)
    else:
        remove_one_gen = (line[0:i] + line[i+1:] for i in range(len(line)))
        if any(safe_line(l) for l in remove_one_gen):
            safe2.append(line)


print(f"Veilige regels 1: {len(safe1)}")
print(f"Veilige regels 2: {len(safe2)}")