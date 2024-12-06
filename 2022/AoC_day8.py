import AoC_input_day8 as inp

l_input = inp.AoC_input.split('\n')
#print(inp.AoC_input_test)

visible_trees = 0

for row_num in range(1,len(l_input)-1):
    for el_num in range(1,len(l_input[row_num])-1):
        above_coord = ((el_num,y) for y in range(row_num))
        below_coord = ((el_num, y) for y in range(row_num+1,len(l_input)))
        left_coord = ((x, row_num) for x in range(el_num))
        right_coord = ((x, row_num) for x in range(el_num+1,len(l_input[row_num])))

        for direction in (above_coord, below_coord, left_coord, right_coord):
            if int(l_input[row_num][el_num]) > max(int(l_input[r][e]) for e,r in direction):
                #print(f"({row_num},{el_num}) visible (value: {int(l_input[row_num][el_num])})")
                visible_trees += 1
                break

print("Number of visible trees: ", visible_trees + 2*len(l_input) + 2*len(l_input[0]) - 4)

max_scenic_score = 0
for row_num in range(len(l_input)):
    for el_num in range(len(l_input[row_num])):
        above_trees = 0
        below_trees = 0
        left_trees = 0
        right_trees = 0

        #above
        for tree in (int(l_input[r][el_num]) for r in range(row_num-1,-1,-1)):
            if int(l_input[row_num][el_num]) > tree:
                above_trees += 1
            else:
                above_trees += 1
                break

        # below
        for tree in (int(l_input[r][el_num]) for r in range(row_num + 1, len(l_input))):
            if int(l_input[row_num][el_num]) > tree:
                below_trees += 1
            else:
                below_trees += 1
                break

        # left
        for tree in (int(l_input[row_num][e]) for e in range(el_num - 1, -1, -1)):
            if int(l_input[row_num][el_num]) > tree:
                left_trees += 1
            else:
                left_trees += 1
                break

        # right
        for tree in (int(l_input[row_num][e]) for e in range(el_num + 1, len(l_input[row_num]))):
            if int(l_input[row_num][el_num]) > tree:
                right_trees += 1
            else:
                right_trees += 1
                break

        scenic_score = above_trees * below_trees * left_trees * right_trees
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score
        #print(f"Scenic score ({row_num},{el_num}): {above_trees} * {below_trees} * {left_trees} * {right_trees} = {scenic_score}")
        #print(f"Scenic score ({row_num},{el_num}): {below_trees}")

print("Maximum scenic score: ", max_scenic_score)