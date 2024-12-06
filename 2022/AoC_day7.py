import AoC_input_day7 as inp

l_input = inp.AoC_input.split('\n')

class Bestand:

    def __init__(zelf, grootte, naam):
        zelf.grootte  = int(grootte)
        zelf.naam     = naam

    def __len__(zelf):
        return zelf.grootte

    def __str__(zelf):
        return zelf.naam

class Map:

    def __init__(zelf, naam, supermap):
        zelf.naam = naam
        zelf.supermap = supermap
        zelf.inhoud = {}
        zelf.grootte = 0

    def __str__(zelf):
        return zelf.naam

    def __len__(zelf):
        zelf.grootte = 0
        for key, value in zelf.inhoud.items():
            zelf.grootte += len(value)

        return zelf.grootte

hoofdmap = Map("/","SUPER")
huidige_map = hoofdmap

def lees_regel(regel):
    global huidige_map
    if regel[0] == '$': #regel is commando
        if regel[2:4] == "cd": #commando is cd. Verander huidige_map
            if regel[5:] == "..":
                huidige_map = huidige_map.supermap
            else:
                huidige_map = huidige_map.inhoud[regel[5:]]
        else: #in geval van "$ ls" niks doen
            pass
    else: #regel is geen commando, dus een dir of een file
        if regel[0:3] == "dir":
            #voeg een nieuwe map to aan huidige map
            huidige_map.inhoud[regel[4:]]=Map(regel[4:],huidige_map)
        else:
            #voeg een bestand toe aan huidige map
            l_regel = regel.split(' ') # --> ['grootte', 'naam']
            l_regel[0] = int(l_regel[0])
            huidige_map.inhoud[l_regel[1]] = Bestand(l_regel[0],l_regel[1])

for line in l_input[1:]:
    lees_regel(line)

def nrange_bestanden(x):
    """Itereer door alle bestanden in de map x. Geeft x terug als x geen map is. """
    if isinstance(x,Map):
        for K, V in x.inhoud.items():
            #print("First for: ", V, isinstance(V,Map))
            for v in nrange_bestanden(V):
                #print("Second for: ", isinstance(v,Map))
                yield v
                #print("After yield: ")
    else:
        yield x

def nrange_mappen(x):
    """Itereer door alle mappen in de map x."""
    if isinstance(x, Map):
        yield x
        for K, V in x.inhoud.items():
            # print(V)
            for v in nrange_mappen(V):
                #print(v)
                yield v
    else:
        pass

print(hoofdmap.inhoud)

sum_of_sizes = 0
for i in nrange_mappen(hoofdmap):
    if len(i) <= 100000:
        sum_of_sizes += len(i)

print(sum_of_sizes)

space_not_used = 70000000 - len(hoofdmap)
#print(space_not_used)

space_to_be_deleted =  30000000 - space_not_used
#print(space_to_be_deleted)

#for i in nrange_mappen(hoofdmap):
#    if len(i) >= space_to_be_deleted:
#        print(i)

x = [folder for folder in nrange_mappen(hoofdmap) if len(folder) >= space_to_be_deleted]

smallest_folder = hoofdmap
for f in x:
    if len(f) <= len(smallest_folder):
        smallest_folder = f

print(smallest_folder, len(smallest_folder))