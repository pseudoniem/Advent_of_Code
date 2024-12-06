import AoC_input_day1 as inp

l_input = [line for line in inp.AoC_input.split('\n')]
print(l_input)


def get_number(s):
    for char in s:
        if char.isdigit():
            p = int(char)
            break

    t = s[::-1]

    for char in t:
        if char.isdigit():
            q = int(char)
            break

    return (10*p + q)


print("Antwoord deel 1 = ", sum([get_number(s) for s in l_input]))

numerals = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}


def get_lnumber_fancy(s):
    for i in range(len(s)):
        for k, v in numerals.items():
            if s[i:].startswith(k) or s[i:].startswith(v):
                p = int(k)
                break
        else:
            continue

        break
    return p


def get_rnumber_fancy(s):
    for i in range(len(s)):
        for k, v in numerals.items():
            if s[-(i+1):].startswith(k) or s[-(i+1):].startswith(v):
                p = int(k)
                break
        else:
            continue

        break
    return p


print("Antwoord deel 2 = ", sum([10*get_lnumber_fancy(s) + get_rnumber_fancy(s) for s in l_input]))