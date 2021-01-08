# Those imports will be useful when OCR will be running
#from utilities.codematrix import CodeMatrix
#from utilities.buffer import Buffer
from utilities.solver import *

# Fill codematrix
codematrix = [["1C", "E9", "55", "55", "1C"],
              ["55", "BD", "E9", "55", "E9"],
              ["BD", "55", "55", "1C", "BD"],
              ["BD", "1C", "E9", "BD", "E9"],
              ["E9", "1C", "1C", "1C", "1C"]]

# Fill sequences
sequences = [["E9", "1C"], ["E9", "E9"], ["BD", "BD", "1C"]]

# Declare buffer size
buffer_size = 4

# Generate combinations
combinations = generate_combinations(sequences, buffer_size)

# Check existence of sequences in combinations
possible_combinations = check_sequences_in_combinations(sequences, combinations, buffer_size)

# Check if best (covering all sequences) solution is possible
best_solution = get_best_combination(combinations, possible_combinations)

# If there is no best solution
if best_solution == None:
    required_solution = get_required_combination(combinations, possible_combinations, [2])
    # Best solution is nowe required solution
    best_solution = required_solution

# Get possible matrix traversal paths
paths = traverse_matrix(codematrix, buffer_size)

# For larger matrix and buffer consider reading pregenerated paths
# in this case read file for matrix size 8x8 and buffer size of 8 - real RAM killer

#paths = list()
#with open("m8b8.txt") as file:
#    line = file.readline()
#    while line:
#        paths.append(line)
#        line = file.readline()

# Find solution among paths
solution = compare_paths_and_combinations(codematrix, paths, best_solution)

# Let's print out solution - it prints listo of matrix [i][j] positions - traversal path
print(solution)
