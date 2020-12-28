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
    print(temp_buffer.get_buffer_size())
