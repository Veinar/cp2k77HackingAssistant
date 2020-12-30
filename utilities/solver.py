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

    # Generate possible combination of unique elements with length of buffer size
    combinations = generate_combinations(sequences, buffer_size)

    # Projection of all combinations to String type
    combi_as_str = list()
    for i in range(0, len(combinations)):
        temp = ""
        for j in range(0, len(combinations[i])):
            temp += combinations[i][j]
        combi_as_str.append(temp)

    # Projection of all sequences to String type
    sequen_as_str = list()
    for i in range(0, len(sequences)):
        temp = ""
        for j in range(0, len(sequences[i])):
            temp += sequences[i][j]
        sequen_as_str.append(temp)

    # Check if combinations is present in generated combinations
    # True present in row indicates presence of sequence in combination so:
    # If every is present, output row should be [True] times sequences length
    # If none is present, output row should be [False] times sequences lenght
    possible = list()
    for i in range(0, len(combi_as_str)):
        has_every = list()
        for j in range(0, len(sequen_as_str)):
            if sequen_as_str[j] in combi_as_str[i]:
                has_every.append('True')
            else:
                has_every.append('False')
        print(has_every)
        print(combi_as_str[i])
        possible.append(has_every)

    return possible

    # Should be done on lists but there is no simple and suitable method
    # for checking if list contains sublist (with fixed positions of elements)
    #for i in combinations:
    #    has_every = list()
    #    for j in sequences:
    #        #if all(elem in i for elem in j):
    #        if is_ordered_sublist(j,i):
    #            has_every.append('True')
    #        else:
    #            has_every.append('False')
    #    print(has_every)
    #    print(i)

#def is_ordered_sublist(xs, ys):
#
#    xset = {*xs}
#    return all(x == y for x, y in zip(xs, (y for y in ys if y in xset)))

# In 99% only usable with large buffer - probably will be deleted
def permute_sequences(sequences, buffer_size):
    # Check if there are multiple sequences or only one
    # If one return sequence from args - no need to be analyzed anymore
    if not isinstance(sequences[0], list):
        return sequences

    #If buffer is too small to handle every sequence combined
    length_of_combination = 0
    for x in sequences:
        length_of_combination += len(x)
    if length_of_combination > buffer_size:
        return None

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

def generate_combinations(sequences, buffer_size):

    in_order_length = 0
    for i in range(0, len(sequences)):
        in_order_length += len(sequences[i])

    if in_order_length == buffer_size:
        print("Do not need to generate combinations")

    # This variable will hold unique elements
    elements = list()

    # Get unique elements (blocks) from all sequences
    for i in range(0, len(sequences)):
        for j in range(0, len(sequences[i])):
            if str(sequences[i][j]) not in elements:
                elements.append(str(sequences[i][j]))

    # Generate combinations of unique elements (blocks) from sequences
    combinations = list(itertools.product(elements, repeat=buffer_size))

    return combinations
