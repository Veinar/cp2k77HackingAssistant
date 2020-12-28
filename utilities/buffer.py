class Buffer:

    def __init__(self, buffer_size):
        self.buffer = [None]*buffer_size

    def push(self, element):
        # Add element at zero position and remove last element (maintain fixed size)
        self.buffer.insert(0,element)
        self.buffer = self.buffer[:-1]

    def print_buffer(self):
        print(self.buffer)

    def get_buffer_size(self):
        return len(self.buffer)
