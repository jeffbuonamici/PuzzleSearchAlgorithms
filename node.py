class Node:
    parent: None
    depth: None
    state: []

    def __init__(self, state, parent, depth):
        self.parent = parent
        self.depth = depth
        self.state = state

    def get_parent(self):
        return self.parent

    def get_depth(self):
        return self.depth

    def get_state(self):
        return self.state

    # Function that creates all possible horizontal and vertical transistions that will be used as nodes in a graph
