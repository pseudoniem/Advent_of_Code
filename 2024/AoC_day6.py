from AoC_input_day6 import AoC_input_test as inp_test, AoC_input as inp_real

inp = inp_real
inp = inp.split('\n')

lines = len(inp)
cols = len(inp[0])


points = {(x, y): inp[y][x] != '#' for y in range(lines) for x in range(cols)}
start = [p for p in points if inp[p[1]][p[0]] == '^'][0]

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)


def _turn(dir):
    if dir == up:
        return right
    elif dir == right:
        return down
    elif dir == down:
        return left
    elif dir == left:
        return up
    else:
        raise Exception("DaFUK")


class Guard:
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir

    def point_infront(self):
        return tuple(self.pos[i] + self.dir[i] for i in range(2))

    def turn(self):
        self.dir = _turn(self.dir)

    def step(self):
        self.pos = self.point_infront()


guard = Guard(start, up)


trail = {start}


def walk():
    steps = 0
    finished = False
    while steps <= len(points):
        steps += 1
        pt_infront = guard.point_infront()
        next_pt = points.get(pt_infront, 'BYE!')
        if next_pt is True:
            trail.add(pt_infront)
            guard.step()
        elif next_pt == 'BYE!':
            # print('BYE!')
            finished = True
            break
        else:
            guard.turn()

    return finished


walk()

print(f"Lengte pad: {len(trail)}")

old_trail = {p for p in trail if p != start}

possible_obstacle_points = set()

for point in old_trail:
    guard = Guard(start, up)
    points[point] = False
    if not walk():
        possible_obstacle_points.add(point)
    points[point] = True


print(f'Mogelijke obstructiepunten: {len(possible_obstacle_points)}')