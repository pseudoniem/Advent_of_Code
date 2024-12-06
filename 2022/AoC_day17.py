import AoC_input_day17 as inp

gas_bursts = inp.AoC_input

rocks = {0: {(0,0), (1,0), (2,0), (3,0)},
         1: {(1,0), (0,1), (1,1), (2,1), (1,2)},
         2: {(0,0), (1,0), (2,0), (2,1), (2,2)},
         3: {(0,0), (0,1), (0,2), (0,3)},
         4: {(0,0), (1,0), (0,1), (1,1)}
         }

shifts = {"<": -1, ">": 1}

def spawn_rock(seed, rock):
    return {(seed[0] + r[0], seed[1] + r[1]) for r in rocks[rock]}


class Rock:
    def __init__(self, coordinates: set, falling=True):
        self.coordinates = coordinates
        self.falling = falling

    def __contains__(self, item):
        return item in self.coordinates

    def __iter__(self):
        yield from self.coordinates

    def move(self, new_coordinates):
        self.coordinates = new_coordinates


class Cave:
    def __init__(self):
        self.floor = {(x, 0) for x in range(1, 8)}
        self.landed_rocks = self.floor
        self.falling_rocks = set()
        self.rocks_fallen = 0
        self.gas_bursts_been = 0
        self.rock_gas = {0:[], 1:[], 2:[], 3:[], 4:[]}

    def __str__(self, top = None):
        cave_map = ""
        height = max(p[1] for p in self.falling_rocks.union(self.landed_rocks))
        if top is None:
            topnrows = -1
        else:
            topnrows = height - top -1
        for y in range(height, topnrows, -1):
            cave_map += f"{y}"
            for x in range(9):
                if x in (0, 8):
                    cave_map += "|"
                elif y == 0:
                    cave_map += "-"
                elif (x, y) in self.landed_rocks:
                    cave_map += "#"
                elif (x, y) in self.falling_rocks:
                    cave_map += "@"
                else:
                    cave_map += "."
            cave_map += "\n"
        return cave_map

    def height(self):
        return max(p[1] for p in self.landed_rocks)

    def drop_rock(self):
        spawn_point = (3, max(p[1] for p in self.landed_rocks) + 4)
        rock = Rock(spawn_rock(spawn_point, self.rocks_fallen % len(rocks)))
        self.falling_rocks = rock.coordinates
        self.rock_gas[self.rocks_fallen % len(rocks)].append(self.gas_bursts_been % len(gas_bursts))
        #print(f"Rock {self.rocks_fallen % len(rocks)}: {rock_gas[self.rocks_fallen % len(rocks)]}")

        while rock.falling:
            self.rock_shifts(rock, gas_bursts[self.gas_bursts_been % len(gas_bursts)])
            self.gas_bursts_been += 1

            self.rock_falls(rock)

    def rock_falls(self, rock):
        below_rock = {(r[0], r[1] - 1) for r in rock}
        if below_rock.intersection(self.landed_rocks):
            self.landed_rocks.update(rock)
            self.landed_rocks = {p for p in self.landed_rocks}
            self.falling_rocks = set()
            rock.falling = False
            self.rocks_fallen += 1
        else:
            rock.move(below_rock)
            self.falling_rocks = rock.coordinates

    def rock_shifts(self, rock, direction):
        shifted_rock = {(r[0] + shifts[direction], r[1]) for r in rock}
        if shifted_rock.intersection(self.landed_rocks) or min(p[0] for p in shifted_rock) < 1 or max(p[0] for p in shifted_rock) > 7:
            pass
        else:
            rock.move(shifted_rock)
            self.falling_rocks = rock.coordinates


C = Cave()

for _ in range(len(rocks)):
    C.drop_rock()

repeat = False
while not repeat:
    C.drop_rock()
    repeat_num = 0
    for k in C.rock_gas:
        repeat_num += C.rock_gas[k][-1] in C.rock_gas[k][0:-1]
    if repeat_num == len(rocks):
        break

D = Cave()

while D.gas_bursts_been < min(C.rock_gas[k][-1] for k in C.rock_gas):
    D.drop_rock()

base_num_rocks = D.rocks_fallen
base_height = D.height()

#print(D.__str__(20))
len_cycle = C.rocks_fallen - len(rocks) - D.rocks_fallen

print("Rocks in cycle: ", len_cycle)

for _ in range(len_cycle):
    D.drop_rock()

print(f"Check: C.rocks_fallen -  len(rocks) == D.rocks_fallen: {C.rocks_fallen -  len(rocks) == D.rocks_fallen}")

height_after_first_cycle = D.height()
cycle_height = D.height() - base_height

print("Base height: ", base_height)
print("Cycle height: ", cycle_height)

number_of_full_cycles = (1000000000000 - base_num_rocks) // len_cycle

print(f"Height after all full cycles: {base_height + number_of_full_cycles * cycle_height}")

rocks_left = 1000000000000 - number_of_full_cycles * len_cycle - base_num_rocks

for _ in range(rocks_left):
    D.drop_rock()

height_rocks_left = D.height() - height_after_first_cycle

print(f"Total height: {base_height} + {number_of_full_cycles} * {cycle_height} + {height_rocks_left} = {base_height + number_of_full_cycles * cycle_height + height_rocks_left}")