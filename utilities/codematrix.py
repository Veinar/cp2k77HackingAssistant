class CodeMatrix:

    def __init__(self, size):
        # Code matrix is always a square - initialize with zeros
        # 4x4 is the smallest possible ?
        self.matrix = [[0]*size for i in range(size)]

    def print_matrix(self):
        # Thanks to georg from Stackoverflow :)
        # For debugging purposes
        strings = [[str(e) for e in row] for row in self.matrix]
        lens = [max(map(len, col)) for col in zip(*strings)]
        fmt = "\t".join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in strings]
        print ("\n".join(table))

    def fill_matrix(self, input_matrix):
        self.matrix = input_matrix

    def get_matrix(self):
        return self.matrix
