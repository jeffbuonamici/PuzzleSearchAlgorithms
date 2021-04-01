from copy import deepcopy

def get_children(self, parent_node):
    state = parent_node.state
    new_states = []
    row_index = 0
    col_index = 0
    for row in state:
        col_index = 0
        for col in row:
            if(row_index < len(state)-1):
                new_state = swap_down(parent_node, row_index, col_index)
                if new_state not in new_states:
                    new_states.append(new_state)
            if(row_index > 1):
                new_state = swap_up(parent_node, row_index, col_index)
                if new_state not in new_states:
                    new_states.append(new_state)
            if(col_index > 1):
                new_state = swap_left(
                    parent_node, row_index, col_index)
                if new_state not in new_states:
                    new_states.append(new_state)
            if(col_index < len(row)-1):
                new_state = swap_right(
                    parent_node, row_index, col_index)
                if new_state not in new_states:
                    new_states.append(new_state)
            
            col_index += 1
        row_index += 1
    return self.create_nodes(new_states, parent_node)

def swap_up(parent_node, row, col):
    new_state = deepcopy(parent_node.state)
    temp = new_state[row][col]
    new_state[row][col] = new_state[row-1][col]
    new_state[row-1][col] = temp
    return new_state

def swap_left(parent_node, row, col):
    new_state = deepcopy(parent_node.state)
    temp = new_state[row][col]
    new_state[row][col] = new_state[row][col-1]
    new_state[row][col-1] = temp
    return new_state

def swap_down(parent_node, row, col):
    new_state = deepcopy(parent_node.state)
    temp = new_state[row][col]
    new_state[row][col] = new_state[row+1][col]
    new_state[row+1][col] = temp
    return new_state

def swap_right(parent_node, row, col):
    new_state = deepcopy(parent_node.state)
    temp = new_state[row][col]
    new_state[row][col] = new_state[row][col+1]
    new_state[row][col+1] = temp
    return new_state
    

def createGraph(input):
    return input.replace(';', ',').replace('(','[').replace(')',']')
