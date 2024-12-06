import AoC_input_day1 as inp

def convert_string_to_dict(y):
    x = y.split('\n')
    for i in x:
        if i == "":
            x[x.index(i)] = "stop"
            
    j=1
    Elves_cal={}
    for i in range(len(x)):
        if x[i] == "stop":
            j += 1
        else:
            if j in Elves_cal.keys():
                Elves_cal[j] += int(x[i])
            else: Elves_cal[j] = int(x[i])
    
    return Elves_cal


Elves = convert_string_to_dict(inp.AoC_input)


for i in Elves:
    #print(i)
    #print(Elves[i])
    #print('\n')
    if Elves[i] == max(Elves.values()):
        print(f"Elf {i} is carrying {Elves[i]} calories.")


elf1 = Elves.pop(130)
print(f"elf1: {elf1}")


elf2 = Elves.pop(227)
print(f"elf2: {elf2}")

elf3 = Elves.pop(196)
print(f"elf3: {elf3}")


ans = elf1 + elf2 + elf3

print(f"Answer: {ans}")