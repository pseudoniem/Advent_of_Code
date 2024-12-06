from AoC_input_day3 import AoC_input_test as inp_test, AoC_input as inp_real

import math

inp = inp_real

res = []

i_dont = inp.find("don't()")

while i_dont != -1:
    inp_left = inp[:i_dont]
    i_do = inp.find("do()", i_dont)
    inp = inp_left + inp[i_do:]
    i_dont = inp.find("don't()")

for i in range(len(inp)):
    if inp[i:i+4] == 'mul(':
        stuk = inp[i:i+12]
        arg_par = stuk[4:]
        try:
            i_par = arg_par.index(')')
            arg = arg_par[:i_par]
        except:
            continue

        if arg.find(' ') == -1 and len(arg.split(',')) == 2:
            res.append(math.prod(int(n) for n in arg.split(',')))
        else:
            continue

print(sum(res))