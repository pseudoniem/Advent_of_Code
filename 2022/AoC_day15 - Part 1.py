import AoC_input_day15 as inp

l_input = inp.AoC_input.split('\n')
l_input = [x.split(":")[0] + x.split(":")[1] for x in l_input]
l_input = [x.split("Sensor at ")[1] for x in l_input]
l_input = [x.split(" closest beacon is at ") for x in l_input]
l_input = [[x[i].split(", ") for i in (0,1)] for x in l_input]
l_input = [[(int(x[i][0][2:]), int(x[i][1][2:])) for i in (0,1)] for x in l_input]

def distance_M(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


no_beacons = set()

for x in l_input:
    d = distance_M(x[0], x[1])
    update_generator = ((x[0][0] + a, 2000000) for a in range(-d, d+1))
    no_beacons.update(set(no_beacon for no_beacon in update_generator if distance_M(x[0], no_beacon) <= d if no_beacon != x[1]))
    print("*")


def no_beacons_in_row(n):
    i = 0
    for x in no_beacons:
        if x[1] == n:
            i += 1
    return i


print(len(no_beacons))