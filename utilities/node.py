class Node:

    def __init__(self, position, state, current_path=None):
        self.position = position
        self.state = state
        if current_path == None:
            self.path = list()
        else:
            self.path = list()
            for i in current_path:
                self.append_path(i)
        self.append_path(position)

    def get_state(self):
        return self.state

    def get_position(self):
        return self.position

    def append_path(self, waypoint):
        self.path.append(waypoint)

    def set_state(self, new_state):
        self.state = new_state

    def get_path(self):
        return self.path
