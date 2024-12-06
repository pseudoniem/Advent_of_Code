import AoC_input_day11 as inp

l_input =  inp.AoC_input.split('\n\n')
for i in range(len(l_input)):
    l_input[i] = l_input[i].split('\n')

for i in range(len(l_input)):
    l_input[i][0] = int(l_input[i][0][:-1][len("Monkey "):])

for i in range(len(l_input)):
    l_input[i][1] = l_input[i][1][len("  Starting items: "):]
    l_input[i][1] = l_input[i][1].split(', ')
    for j in range(len(l_input[i][1])):
        l_input[i][1][j] = int(l_input[i][1][j])

for i in range(len(l_input)):
    l_input[i][2] = l_input[i][2][len("  Operation: new = old "):]
    l_input[i][2] = [l_input[i][2][0],l_input[i][2][2:]]

for i in range(len(l_input)):
    l_input[i][3] = int(l_input[i][3][len("  Test: divisible by "):])

for i in range(len(l_input)):
    l_input[i][4] = int(l_input[i][4][len("    If true: throw to monkey "):])

for i in range(len(l_input)):
    l_input[i][5] = int(l_input[i][5][len("    If false: throw to monkey "):])
#print(test)

print(l_input)


class Aap:
    def __init__(self, begin_waardes: list, bewerking_bewerking_waarde, delen_door:int, test_waarAap: int, test_onwaarAap: int):
        self.voorwerpen = begin_waardes
        self.bewerking = bewerking_bewerking_waarde[0]
        if bewerking_bewerking_waarde[1] == "old":
            self.bewerking_waarde = bewerking_bewerking_waarde[1]
        else:
            self.bewerking_waarde = int(bewerking_bewerking_waarde[1])
        self.delen_door = delen_door
        self.test_waarAap = test_waarAap
        self.test_onwaarAap = test_onwaarAap
        self.bewerkingen = {"+": lambda x,y: x+y,
                   "-": lambda x,y: x-y,
                   "*": lambda x,y: x*y,
                   "/": lambda x,y: x/y}
        self.voorwerpen_geïnspecteerd = 0


    def __bewerking__(self, x):
        if self.bewerking_waarde == "old":
            return self.bewerkingen[self.bewerking](x,x)
        else:
            return self.bewerkingen[self.bewerking](x,self.bewerking_waarde)

    def ontvang(self, voorwerp):
        self.voorwerpen.append(voorwerp)

    def gooi(self, andere):
        andere.ontvang(self.voorwerpen.pop(0))

    def beurt(self):
        self.voorwerpen_geïnspecteerd += len(self.voorwerpen)
        self.voorwerpen = [self.__bewerking__(w) % product_alles for w in self.voorwerpen]
        for _ in range(len(self.voorwerpen)):
            if self.voorwerpen[0] % self.delen_door == 0:
                self.gooi(apen[self.test_waarAap])
            else:
                self.gooi(apen[self.test_onwaarAap])

apen = {aap[0]:Aap(aap[1], aap[2], aap[3], aap[4], aap[5]) for aap in l_input}

product_alles = 1
for aap in apen.values():
    product_alles *= aap.delen_door

print(product_alles)

#print(apen)
for n, aap in apen.items():
    print(f"Aap {n}: {aap.voorwerpen}")

for rounds in range(10000):
    print(rounds)
    for aap in apen.values():
        aap.beurt()


print()
for aap in apen.values():
    print(f"Aap heeft {aap.voorwerpen_geïnspecteerd} voorwerpen geïnspecteerd.")

def apenstreken(x):
    apstr = [a.voorwerpen_geïnspecteerd for a in x.values()]
    apstr.sort(reverse=True)
    return apstr[0] * apstr[1]

print(f"Apenstrekenniveau: {apenstreken(apen)}")

