class Node:

    def __init__(self, state, parent, depth, fscore):
        self.parent = parent
        self.depth = depth
        self.state = state
        self.fscore = fscore

    def __lt__(self, other):
        if(self.depth < other.depth):
            return self
        else:
            return other