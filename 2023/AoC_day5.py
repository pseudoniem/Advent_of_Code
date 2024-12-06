import AoC_input_day5 as inp

l_input = [line.split(':') for line in inp.AoC_input.split('\n\n')]
d_input = {line[0]: line[1].lstrip() for line in l_input}


d_input['seeds'] = [int(i) for i in d_input['seeds'].split(' ')]

seeds = d_input.pop('seeds')

d_input = {k: v.split('\n') for k, v in d_input.items()}
d_input = {k: [tuple(line.split(' ')) for line in v] for k, v in d_input.items()}
d_input = {k[:-4]: [(int(tup[0]), int(tup[1]), int(tup[2])) for tup in v] for k, v in d_input.items()}

d_input_ranges = {k: [(t[0], t[1], range(t[1], t[1] + t[2])) for t in v] for k, v in d_input.items()}

print(l_input)
print(d_input)
print(d_input_ranges)


def map_to(x, rows):
    for row in rows:
        if x in row[2]:
            return row[0] + (x - row[1])
    else:
        return x

def seed_to_location(seed):
    for k in d_input_ranges:
        seed = map_to(seed, d_input_ranges[k])

    return seed

print(f"Antwoord deel 1: {min(seed_to_location(s) for s in seeds)}")
print('======================================================\n')


seeds = [range(seeds[i], seeds[i] + seeds[i+1]) for i in range(len(seeds)) if i%2 == 0]

all_seeds = set()

for r in seeds:
    all_seeds.update(r)

print(f"Antwoord deel 2: {min(seed_to_location(s) for s in all_seeds)}")
