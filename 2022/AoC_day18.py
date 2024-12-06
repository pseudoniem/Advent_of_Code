import AoC_input_day18 as inp

l_input = {tuple(int(line.split(",")[i]) for i in range(3)) for line in inp.AoC_input.split("\n")}

adj = (-1,0,1)
surface = 0
for cube in l_input:
    orth_adj_cubes_per_cube = {(cube[0] + i, cube[1] + j, cube[2] + k) for i in adj for j in adj for k in adj if abs(i) + abs(j) + abs(k) == 1}
    adj_cubes = orth_adj_cubes_per_cube.difference(l_input)
    surface += len(adj_cubes)

print(f"Total surface: {surface}")

min_cx = min(cube[0] for cube in l_input) - 3
max_cx = max(cube[0] for cube in l_input) + 3
min_cy = min(cube[1] for cube in l_input) - 3
max_cy = max(cube[1] for cube in l_input) + 3
min_cz = min(cube[2] for cube in l_input) - 3
max_cz = max(cube[2] for cube in l_input) + 3
enveloping_cube_border_full = {(x, y, z) for x in range(min_cx, max_cx+1) for y in range(min_cy, max_cy+1) for z in range(min_cz, max_cz+1)}
enveloping_cube_border_int = {(x, y, z) for x in range(min_cx+1, max_cx) for y in range(min_cy+1, max_cy) for z in range(min_cz+1, max_cz)}
enveloping_cube_border = enveloping_cube_border_full.difference(enveloping_cube_border_int)

outside_air_seed = ()
for cube in l_input:
    if cube[0] == max(c[0] for c in l_input):
        outside_air_seed = (cube[0] +1, cube[1], cube[2])
        break
# outside_air_seed is now some cube of air that is definitely on the outside and touches on a face.

outside_air = {outside_air_seed}
outside_air_incomplete = True
#count = 0
while outside_air_incomplete:
    #count += 1
    #print(count)
    outside_air_add = set()
    for air_cube in outside_air:
        orth_adj_air_cubes_all = {(air_cube[0] + i, air_cube[1] + j, air_cube[2] + k) for i in adj for j in adj for k in adj if abs(i) + abs(j) + abs(k) == 1}
        # We need only those inside an enveloping cube
        orth_adj_air_cubes = orth_adj_air_cubes_all.difference(enveloping_cube_border)
        outside_air_add.update(orth_adj_air_cubes.difference(l_input))

    if outside_air_add == outside_air.intersection(outside_air_add):
        outside_air_incomplete = False
    else:
        outside_air.update(outside_air_add)

outer_surface = 0
for cube in l_input:
    orth_adj_cubes_per_cube = {(cube[0] + i, cube[1] + j, cube[2] + k) for i in adj for j in adj for k in adj if abs(i) + abs(j) + abs(k) == 1}
    adj_cubes = orth_adj_cubes_per_cube.difference(l_input).intersection(outside_air)
    outer_surface += len(adj_cubes)

print(f"Outer surface: {outer_surface}")
