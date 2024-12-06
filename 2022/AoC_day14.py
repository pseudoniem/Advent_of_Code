import AoC_input_day14 as inp

l_input = [x.split(" -> ") for x in inp.AoC_input.split('\n')]
l_input = [[tuple(int(x.split(",")[i]) for i in range(2)) for x in line] for line in l_input]


def steenlijn(c1, c2):
    if c1[0] != c2[0]:
        return {(x, c1[1]) for x in range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1)}
    elif c1[1] != c2[1]:
        return {(c1[0], y) for y in range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1)}


steencoördinaten = set()
for line in l_input:
    for i in range(len(line) - 1):
        steencoördinaten.update(steenlijn(line[i], line[i + 1]))
# print(steencoördinaten)


vallend_zand_coördinaten = {(500, 0)}

geland_zand_coördinaten = set()


class Grot:
    def __init__(self, steen: set, zand_vallend: set, zand_geland: set):
        self.steen = steen
        self.zand_vallend = zand_vallend
        self.zand_geland = zand_geland
        self.bodem = set()
        self.__spoorgeheugen__ = []
        self.vol = False

    def __str__(self):
        self.kaart = ""
        for y in range(max(coörd[1] for coörd in self.steen.union(self.bodem)) + 1):
            for x in range(min(coörd[0] for coörd in self.steen.union(self.bodem)),
                           max(coörd[0] for coörd in self.steen.union(self.bodem)) + 1):
                if (x, y) in self.steen.union(self.bodem):
                    self.kaart += "#"
                elif (x, y) in self.zand_vallend:
                    self.kaart += "+"
                elif (x, y) in self.zand_geland:
                    self.kaart += "."
                else:
                    self.kaart += " "
            self.kaart += "\n"

        return self.kaart

    def korrel_valt(self, korrel, vallen=True):
        controleverzameling = self.steen.union(self.zand_geland).union(self.bodem)
        if (korrel[0], korrel[1] + 1) not in controleverzameling:
            self.zand_vallend.remove(korrel)
            korrel = (korrel[0], korrel[1] + 1)
            self.zand_vallend.add(korrel)
        elif (korrel[0] - 1, korrel[1] + 1) not in controleverzameling:
            self.zand_vallend.remove(korrel)
            korrel = (korrel[0] - 1, korrel[1] + 1)
            self.zand_vallend.add(korrel)
        elif (korrel[0] + 1, korrel[1] + 1) not in controleverzameling:
            self.zand_vallend.remove(korrel)
            korrel = (korrel[0] + 1, korrel[1] + 1)
            self.zand_vallend.add(korrel)
        else:
            self.zand_vallend.remove(korrel)
            self.zand_geland.add(korrel)
            vallen = False
        korrel_time += time.time() - start_time
        return (korrel, vallen)

    def zand_valt(self):
        if len(self.__spoorgeheugen__) <= 2:
            bron = (500, 0)
            self.zand_vallend = {bron}
        elif len(self.__spoorgeheugen__) > 100:
            bron = self.__spoorgeheugen__[-100]
        else:
            bron = self.__spoorgeheugen__[0]

        korrel = bron
        self.zand_vallend.add(bron)
        spoorgeheugen = [bron]
        vallen = True

        while vallen and korrel[1] + 1 <= max(coörd[1] for coörd in steencoördinaten):
            spoorgeheugen.append(korrel)
            korrel, vallen = self.korrel_valt(korrel, vallen)
            self.zand_vallend.add(bron)

        self.__spoorgeheugen__ = spoorgeheugen

        if vallen:
            self.vol = True

    def zand_valt2(self):
        if len(self.__spoorgeheugen__) <= 2:
            bron = (500, 0)
            self.zand_vallend = {bron}
        elif len(self.__spoorgeheugen__) > 50:
            bron = self.__spoorgeheugen__[-50]
        else:
            bron = self.__spoorgeheugen__[0]

        korrel = bron
        self.zand_vallend.add(bron)
        spoorgeheugen = [bron]
        vallen = True

        while vallen and bron not in self.zand_geland:
            # print(self.__str__())
            # print("------------------------------------------------------------------------------------")
            if korrel[1] == max(coörd[1] for coörd in steencoördinaten) + 1:
                self.bodem.update({(korrel[0] + e, korrel[1] + 1) for e in range(-10, 10)})

            spoorgeheugen.append(korrel)
            korrel, vallen = self.korrel_valt(korrel, vallen)
            self.zand_vallend.add(bron)

        self.__spoorgeheugen__ = spoorgeheugen

        if (500, 0) in self.zand_geland:
            self.zand_vallend = set()
            self.vol = True


grot = Grot(steencoördinaten, vallend_zand_coördinaten, set())

aantal_korrels = 0
while True:
    grot.zand_valt2()
    if grot.vol:
        break
    aantal_korrels += 1
    if (aantal_korrels + 1) % 100 == 0:
        print(f"Aantal korrels: {aantal_korrels + 1}")

f = open('Grot_day14.txt', 'w')
f.write(f"Aantal korrels: {aantal_korrels}")
f.write(grot.__str__())
f.close()