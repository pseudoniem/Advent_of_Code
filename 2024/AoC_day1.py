from AoC_input_day1 import AoC_input_test as inp_t, AoC_input as inp_real

inp = inp_real

l_in = [line.split('  ') for line in inp.split('\n')]

left = [int(line[0]) for line in l_in]
right = [int(line[1]) for line in l_in]

left.sort()
right.sort()

dif = (abs(right[i] - left[i]) for i in range(len(left)))

scores = (left[i] * right.count(left[i]) for i in range(len(left)))

print(sum(dif))

print(sum(scores))


def calculate_total_distance(input_data):
    # Parse input into two lists of integers
    left_list, right_list = zip(*[map(int, line.split()) for line in input_data.splitlines()])

    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Calculate total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

    return total_distance


# Call the function and print the result
result = calculate_total_distance(inp)
print(f"Total distance between the lists: {result}")







