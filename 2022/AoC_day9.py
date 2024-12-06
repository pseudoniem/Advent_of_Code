import AoC_input_day9 as inp

l_input = [(line[0], int(line[2:])) for line in inp.AoC_input.split('\n')]
print(l_input)

class Knot:
    def __init__(self):
        self.location = (0,0)
        self.adj_orth = self.set_adj_orth()
        self.adj = self.set_adj()
        self.past_locations = {self.location}

    def set_adj_orth(self):
        return {(self.location[0] + x, self.location[1] + y) for x in (-1,0,1) for y in (-1,0,1) if x**2 != y**2}

    def set_adj(self):
        return {(self.location[0] + x, self.location[1] + y) for x in (-1,0,1) for y in (-1,0,1) if (x,y) != (0,0)}


H = Knot()
T = Knot()

rope = {}
for knot in range(10):
    rope[knot] = Knot()



def distance(head, tail):
    return max(abs(head.location[0]-tail.location[0]), abs(head.location[1]-tail.location[1]))


def move_to_H(head, tail):
    if distance(head,tail) > 1:
        try:
            tail.location = tail.adj.intersection(head.adj_orth).pop()
        except:
            tail.location = tail.adj.intersection(head.adj).pop()

        tail.adj_orth = tail.set_adj_orth()
        tail.adj = tail.set_adj()
        tail.past_locations.add(tail.location)


#H.location = (2,0)
#H.adj_orth = H.set_adj_orth()

#move_to_H(H,T)

#print("H:", H.location, "T: ", T.location)



stdr = {"R": (1,0), "L": (-1,0), "U": (0,1), "D": (0,-1)}

for direction, dist in l_input:
    #print(direction, distance)
    for _ in range(dist):
        H.location = (H.location[0] + stdr[direction][0], H.location[1] +stdr[direction][1])
        #print(H.location)
        H.adj_orth = H.set_adj_orth()
        H.adj = H.set_adj()
        move_to_H(H,T)

#print(T.past_locations)
print(len(T.past_locations))

for direction, dist in l_input:
    #print(direction, distance)
    for _ in range(dist):
        rope[0].location = (rope[0].location[0] + stdr[direction][0], rope[0].location[1] + stdr[direction][1])
        rope[0].adj_orth = rope[0].set_adj_orth()
        rope[0].adj = rope[0].set_adj()
        #print(rope[0])
        #print(rope[0].location)


        for H,T in ((rope[i],rope[i+1]) for i in range(len(rope)-1)):
            #print(H.location)
            #print(T.location)
            #print()
            move_to_H(H,T)


print(len(rope[9].past_locations))
#print(len(T.past_locations))




