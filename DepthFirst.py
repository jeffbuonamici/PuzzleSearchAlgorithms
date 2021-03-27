from node import Node
from copy import deepcopy
import time

class DepthFirstSearch:
    # setup starting node (random puzzle state)
    open_nodes = []
    visited_nodes = []
    goal_state = None

    def __init__(self, goal, start_node):
        self.goal_state = goal
        self.open_nodes.append(start_node)

    def start(self):
        timeout = time.time() +60
        while self.open_nodes:
            if time.time() > timeout:
                print("timeout")
                break
            current = self.open_nodes.pop()

            # check if node is goal node
            if(current.state == self.goal_state):
                print('done')
                # end

            children = self.get_children(current)
            for child in children:
                if not self.is_open(child) and not self.is_visited(child):
                    self.open_nodes.append(child)

            self.visited_nodes.append(current)

    def get_children(self, parent_node):
        state = parent_node.state
        new_states = []
        row_index = 0
        col_index = 0
        for row in state:
            col_index = 0
            for col in row:
                if(row_index > 1):
                    new_state = self.swap_up(parent_node, row_index, col_index)
                    if new_state not in new_states:
                        new_states.append(new_state)
                if(col_index < len(row)-1):
                    new_state = self.swap_right(
                        parent_node, row_index, col_index)
                    if new_state not in new_states:
                        new_states.append(new_state)
                if(row_index < len(state)-1):
                    new_state = self.swap_down(
                        parent_node, row_index, col_index)
                    if new_state not in new_states:
                        new_states.append(new_state)
                if(col_index > 1):
                    new_state = self.swap_left(
                        parent_node, row_index, col_index)
                    if new_state not in new_states:
                        new_states.append(new_state)
                col_index += 1
            row_index += 1
        return new_states

    def swap_up(self, parent_node, row, col):
        new_state = deepcopy(parent_node.state)
        temp = new_state[row][col]
        new_state[row][col] = new_state[row-1][col]
        new_state[row-1][col] = temp
        return Node(new_state, parent_node, parent_node.depth+1)

    def swap_left(self, parent_node, row, col):
        new_state = deepcopy(parent_node.state)
        temp = new_state[row][col]
        new_state[row][col] = new_state[row][col-1]
        new_state[row][col-1] = temp
        return Node(new_state, parent_node, parent_node.depth+1)

    def swap_down(self, parent_node, row, col):
        new_state = deepcopy(parent_node.state)
        temp = new_state[row][col]
        new_state[row][col] = new_state[row+1][col]
        new_state[row+1][col] = temp
        return Node(new_state, parent_node, parent_node.depth+1)

    def swap_right(self, parent_node, row, col):
        new_state = deepcopy(parent_node.state)
        temp = new_state[row][col]
        new_state[row][col] = new_state[row][col+1]
        new_state[row][col+1] = temp
        return Node(new_state, parent_node, parent_node.depth+1)

    def is_open(self, node):
        for i in range(len(self.open_nodes)):
            if(node.state == self.open_nodes[i].state):
                return True
        return False

    def is_visited(self, node):
        for i in range(len(self.visited_nodes)):
            if(node.state == self.visited_nodes[i].state):
                return True
        return False
