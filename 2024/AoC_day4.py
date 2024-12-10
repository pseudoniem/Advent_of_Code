from AoC_input_day4 import AoC_input_test as inp_test, AoC_input as inp_real

import math

# Tering, wat is dit lelijk

inp = inp_real

xmas = "XMAS"

inp = inp.split('\n')





lines = len(inp)
cols = len(inp[0])


letters = {(x, y): inp[y][x] for y in range(lines) for x in range(cols)}


def get_letter(x, y):
    return letters.get((x,y),'')


def adjacent(point, letter, field):
    adj = {k: v for k, v in field.items() if max(abs(point[0] - k[0]), abs(point[1] - k[1])) == 1}
    return {k: v for k, v in adj.items() if v == letter}


def mas(x,y):
    if letters.get((x,y)) == 'A':
        up = ((x-1, y-1), (x+1, y+1))
        down = ((x-1, y+1), (x+1, y-1))

        UP = ''.join(letters.get(c, '') for c in up)
        DOWN = ''.join(letters.get(c, '') for c in down)

        ok = ['MS', 'SM']

        if UP in ok and DOWN in ok:
            return True

    return False


def line(p, v):
    for i in range(4):
        yield (p[0] + i * v[0], p[1] + i * v[1])


A = {k: v for k, v in letters.items() if v == 'A'}


#print(XMAS)
count = 0

#for coord in X.keys():
#    for v in [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if i or j]:
#        if ''.join(get_letter(*p) for p in line(coord, v)) == 'XMAS':
#            count += 1

print(count)

print(sum(mas(*coord) for coord in A))