import AoC_input_day13 as inp
import ast

class mylist(list):
    def __lt__(self, other):
        if isinstance(other, list):
            return list(self) < other
        else:
            return list(self) < [other]

    def __le__(self, other):
        if isinstance(other, list):
            return list(self) <= other
        else:
            return list(self) <= [other]

    def __gt__(self, other):
        if isinstance(other, list):
            return list(self) > other
        else:
            return list(self) > [other]

    def __ge__(self, other):
        if isinstance(other, list):
            return list(self) >= other
        else:
            return list(self) >= [other]

    def __eq__(self, other):
        if isinstance(other, list):
            return list(self) == other
        else:
            return list(self) == [other]

l_input = inp.AoC_input.split('\n\n')
l_input = [x.split('\n') for x in l_input]
l_input = [[ast.literal_eval(x[0]), ast.literal_eval(x[1])] for x in l_input]

def cast_to_mylist(lst):
    x = mylist()
    for i in lst:
        if isinstance(i, list):
            x.append(cast_to_mylist(i))
        else:
            x.append(i)
    return x



#l_input = [cast_to_mylist(x) for x in l_input]
l_input = cast_to_mylist(l_input)
#print(l_input)

lines = []
line = 0
#for pair in range(len(l_input)):
#    try:
#        print(f"{mylist(l_input[pair][0]) <= mylist(l_input[pair][1])}: {l_input[pair][0]} < {l_input[pair][1]}")
#    except TypeError:
#        print(f"Error for {l_input[pair][0]} vs {l_input[pair][1]}")
#        print(type(l_input[pair][0]), type(l_input[pair][1]))
#    print()

for pair in range(len(l_input)):
    line += 1
    if mylist(l_input[pair][0]) <= mylist(l_input[pair][1]):
        lines.append(line)

print(f"Answer part 1: {sum(lines)}")

l = [[[2]],[[6]]]
l = cast_to_mylist(l)
all_lines = l.copy()

for left, right in l_input:
    all_lines.append(left)
    all_lines.append(right)

all_lines.sort()



print(f"Answer part 2: {(all_lines.index(l[0])+1) * (all_lines.index(l[1])+1)}")