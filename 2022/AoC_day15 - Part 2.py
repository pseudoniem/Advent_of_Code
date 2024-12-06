import AoC_input_day15 as inp

l_input = inp.AoC_input.split('\n')
l_input = [x.split(":")[0] + x.split(":")[1] for x in l_input]
l_input = [x.split("Sensor at ")[1] for x in l_input]
l_input = [x.split(" closest beacon is at ") for x in l_input]
l_input = [[x[i].split(", ") for i in (0,1)] for x in l_input]
l_input = [[(int(x[i][0][2:]), int(x[i][1][2:])) for i in (0,1)] for x in l_input]

def distance_M(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def make_circle(centre, radius):
    return {(centre[0] + (s * i), centre[1] + (t * (radius - i))) for i in range(radius + 1) for s in (-1, 1) for t in (-1, 1)}

possible_locations = set()

for sensor, beacon in l_input:
    possible_locations.update(make_circle(sensor, distance_M(sensor, beacon) + 1))

param = 4000000
grid_generator = (s for s in possible_locations if 0 <= s[0] <= param if 0 <= s[1] <= param)

c = 0
for p in grid_generator:
    c += 1
    if c % 10000 == 0:
        print(c)
    
    if sum(distance_M(p, line[0]) <= distance_M(line[0], line[1]) for line in l_input) == 0:
        print()
        print(p)
        print(4000000 * p[0] + p[1])
        break

