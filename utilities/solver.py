import itertools
from utilities.buffer import Buffer

def solve(picked_sequences):
    # TODO: Create solving function
    row_blocked = True
    row_blocked_num = 0
    column_blocked = False
    column_blocked_num = 0
    solved = False

    while not solved:
        # We are picking in column
        if row_blocked:
            pass
        # We are picking in row
        if column_blocked:
            pass

def check_possible_sequences(sequences, buffer_size):
    # Check how many hacks can be applied
    # TODO: Check which sequences could be done and in which order
    temp_buffer = Buffer(buffer_size)
    #every_possible_combination = []
    #print(every_possible_combination)
    possibilities = permute_sequences(sequences)
    print(possibilities)


def permute_sequences(sequences):
    # Check if there are multiple sequences or only one
    # If one return sequence from args - no need to be analyzed anymore
    if not isinstance(sequences[0], list):
        return sequences

    # Generate all possible setting of sequences
    permutations = list(itertools.permutations(list(range(0,len(sequences)))))
    # This variable will hold combined sequences in given order
    combinations = list()

    # For every permutation (list containing possible positions of sequences)
    for i in range(0, len(permutations)):
        # Declare list variable for holding one combined sequences
        combination = list()
        # For every element in one permutation
        for j in range(0, len(permutations[i])):
            # Get sequence no. permutations[i][j], and for every element in that sequence
            for k in range(len(sequences[permutations[i][j]])):
                # Add item from sequence list to new array - create combination
                combination.append(sequences[permutations[i][j]][k])

        combinations.append(combination)       
    return combinations
