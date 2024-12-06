import AoC_input_day20 as inp

class Number:
    def __init__(self, num, turn_number):
        self.num = num
        self.turn_number = turn_number # first turn has turn_number 0

    def __eq__(self, other):
        return self.num == other.num and self.turn_number == other.turns_number

    def __str__(self):
        return self.num

    def __repr__(self):
        return f"{self.__class__.__name__}({self.num}, (%{self.num % 6}), {self.turn_number})"


number_of_rounds = 10
decryption_key = 811589153

l_input = inp.AoC_input.split('\n')
sequence = [Number(decryption_key * int(l_input[i]), i) for i in range(len(l_input))]

for round in range(number_of_rounds, 0, -1):
    for turn in range(len(sequence)):
        for i in range(len(sequence)):
            if sequence[i].turn_number == turn:
                # print(l_input[i])
                sequence.insert((i+sequence[i].num) % (len(sequence)-1), sequence.pop(i))
                break

for number in sequence:
    if number.num == 0:
        zero = number
        break

print("Sum of grove coordinates: ", sum(sequence[(sequence.index(zero) + i) % len(sequence)].num for i in (1000, 2000, 3000)))