import AoC_input_day12 as inp
import networkx as nx

l_input = inp.AoC_input.split('\n')

#NB: (rij, kolom), dus niet (x,y)
punten = [(rij, kolom) for rij in range(len(l_input)) for kolom in range(len(l_input[0]))]


alfabet = "abcdefghijklmnopqrstuvwxyz"
hoogtes = {alfabet[i]:i for i in range(len(alfabet))}
hoogtes["S"]=hoogtes['a']
hoogtes["E"]=hoogtes['z']
#print(hoogtes)

G = nx.DiGraph()

G.add_nodes_from(knoop for knoop in punten)

for knoop in G.nodes:
    G.nodes[knoop]["hoogte"] = hoogtes[l_input[knoop[0]][knoop[1]]]

for knoop_van in G.nodes:
    G.add_edges_from(((knoop_van, knoop_naar) for knoop_naar in G.nodes if abs(knoop_van[0]-knoop_naar[0]) + abs(knoop_van[1]-knoop_naar[1]) == 1 if G.nodes[knoop_naar]["hoogte"] - G.nodes[knoop_van]["hoogte"] <= 1), weging = 1)

for knoop in punten:
    if l_input[knoop[0]][knoop[1]] == "S":
        S = knoop
    elif l_input[knoop[0]][knoop[1]] == "E":
        E = knoop

#print(f"S: {S}, E: {E}")
#lengte_pad = nx.shortest_path_length(G,S,E)
#print(lengte_pad)

mogelijke_antwoorden = []

for s in G.nodes:
    if G.nodes[s]["hoogte"] == 0:
        try:
            mogelijke_antwoorden.append(nx.shortest_path_length(G, s, E))
        except:
            pass

print(min(mogelijke_antwoorden))