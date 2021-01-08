import itertools
import copy
from utilities.node import Node

def solve():
    pass

def check_sequences_in_combinations(sequences, combinations, buffer_size):

    # Check if there are multiple sequences or only one
    # If one return sequence from args - no need to be analyzed anymore
    if not isinstance(sequences[0], list):
        return ['True']

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
    for i in sequences:
        length_of_combination += len(i)
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
        print('\x1b[6;30;42m' + "Do not need to generate combinations" + '\x1b[0m')

    # This variable will hold unique elements
    elements = list()

    # Get unique elements (blocks) from all sequences
    for i in range(0, len(sequences)):
        for j in range(0, len(sequences[i])):
            if str(sequences[i][j]) not in elements:
                elements.append(str(sequences[i][j]))

    # Generate combinations of unique elements (blocks) from sequences
    # Combinatios could be shorter than whole buffer :)
    #combinations = list(itertools.product(elements, repeat=buffer_size))

    # New approach, generate all combinations from-to length:
    # minimum - shortest sequence
    # maximum - buffer size (buffer_size length also, so +1)
    combinations = list()                   
    for k in range(get_shortest_sublist_length(sequences), buffer_size + 1):
        combinations.extend(list(itertools.product(elements, repeat=k)))

    return combinations

def get_best_combination(combinations, possible_combinations):

    # Create best what row in possible combinations could be
    # will be used for searching possible_combinations list
    row_to_lookup = ['True']*len(possible_combinations[0])

    # Find row/s where required sequences are present
    # and get its index
    findings = list()
    found = False
    for i in range(0, len(possible_combinations)):
        if possible_combinations[i] == row_to_lookup:
            findings.append(i)
            found = True

    if found:
        #return combinations[best]
        combinations_to_return = list()
        # Get combinations from index value and put them into list
        for i in range(0, len(findings)):
            combinations_to_return.append(combinations[findings[i]])
        return combinations_to_return
    else:
        return None

def get_required_combination(combinations, possible_combinations, required_sequences):
    # This should be used when all sequences cannot be done

    # Check if sequence number is not exceeeding allowed values
    biggest_possible = len(possible_combinations[0]) - 1
    for i in required_sequences:
        if i > biggest_possible:
            # TODO: handle this in future
            print("Exceeded maximum index allowed. TIP: Count from 0 like programmers do!")
            return None

    row_to_lookup = list()
    # Generate row to be found in possible combinations list
    for i in range(0,len(possible_combinations[0])):
        if i in required_sequences:
            row_to_lookup.append('True')
        else:
            row_to_lookup.append('False')

    # Find row/s where required sequences are present
    # and get its index
    findings = list()
    found = False
    for i in range(0, len(possible_combinations)):
        if possible_combinations[i] == row_to_lookup:
            findings.append(i)
            found = True

    if found:
        combinations_to_return = list()
        # Get combinations from index value and put them into list
        for i in range(0, len(findings)):
            combinations_to_return.append(combinations[findings[i]])
        return combinations_to_return
    else:
        return None

def get_shortest_sublist_length(some_list):
    shortest = len(some_list[0])
    for i in some_list:
        if len(i) < shortest:
            shortest = len(i)

    return shortest

def traverse_matrix(matrix, buffer_size):
    # Get possible paths from codematrix with max lenght of buffer size

    # Initialize nodes for first run
    nodes = list()
    for i in range(0, len(matrix[0])):
        matrix_copy = mark_visited(matrix, [(0,i)])
        nodes.append(Node((0,i),matrix_copy))

    # Start from picking vertically
    direction = True
    for i in range(0, buffer_size - 1):
        new_nodes = list()
        for j in range(0,len(nodes)):
            # Get possible places for next move
            avaliable = get_possible_movement(nodes[j].get_state(), nodes[j].get_position(), direction)
            for k in avaliable:
                # Get path that leads to this node
                current_path = nodes[j].get_path()
                # Get new state matrix
                new_matrix = mark_visited(matrix, current_path)
                new_matrix = mark_visited(new_matrix, [(k[0], k[1])])
                new_node = Node(k, new_matrix, current_path=current_path)
                new_nodes.append(new_node)
        # Free some memory (8x8 matrix and size 8 buffer is memory killer)
        del nodes
        # For next loop evaluate new cases (nodes)
        nodes = new_nodes
        # Switch directions
        direction = not direction

    # Rewrite paths to list and
    # remove nodes (no more needed)
    paths = list()
    for node in nodes:
        paths.append(node.get_path())
        del node

    return paths

def get_possible_movement(matrix, position, direction):

    position_row = position[0]
    position_col = position[1]
    possible_movement = list()

    if direction:
        # Vertical - PION
        for i in range(0, len(matrix)):
            if "X" not in str(matrix[i][position_col]):
                possible_movement.append((i, position_col))

    else:
        # Horizontal - POZIOM
        for i in range(0, len(matrix[0])):
            if "X" not in str(matrix[position_row][i]):
                possible_movement.append((position_row, i))

    return possible_movement

def mark_visited(matrix, places):

    new_matrix = copy.deepcopy(matrix)

    for i in places:
        new_matrix[i[0]][i[1]] = "X"

    return new_matrix

def elements_in_path(matrix, path):
    # Switch indexes in pathlist to elements in matrix
    # will be used for comparing combinations and elements in path
    elements = list()
    for coords in path:
        elements.append(matrix[coords[0]][coords[1]])
    return elements

def compare_paths_and_combinations(matrix, paths, picked_sequences, only_one=True):
    # Find combinations in paths, and return one or every that was found
    elem_in_path = list()
    for path in paths:
        elem_in_path.append(elements_in_path(matrix, path))

    # If not only one, init list
    if only_one:
        selected_path = None
    else:
        selected_path = list()

    found = False
    for i in range(0, len(picked_sequences)):
        for j in range(0, len(elem_in_path)):
            # Comparision on strings :)
            combi = ''.join(picked_sequences[i])
            path = ''.join(elem_in_path[j])
            if combi in path:
                #print("Found path:")
                #print("-----------")
                #print("Combination:")
                #print(picked_sequences[i])
                #print("Path:")
                #print(paths[j])
                #print("-------------------------")
                found = True
                if only_one:
                    selected_path = paths[j]
                    break
                else:
                    selected_path.append(paths[j])
        if only_one and found:
            break
    # If path is found return it, else return None
    return selected_path
