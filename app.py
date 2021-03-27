def app():
    input = '((6; 1; 2); (7; 7; 3); (5; 4; 9))'
    graph = createGraph(input)
    print(graph)

def createGraph(input):
    return input.replace(';', ',')

if __name__ == '__app__':
    app()

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
    
    def get_state():
        return self.state

    # Function that creates all possible horizontal and vertical transistions that will be used as nodes in a graph

class DepthFirstSearch:
    #setup starting node (random puzzle state)
    open_nodes = []
    visited_nodes = []
    goal_node = []

    def set_goal_node(self, goal_node):
        self.goal_node = goal_node
    
    #'((6; 1; 2); (7; 7; 3); (5; 4; 9))'
    def set_start_node(self, start_node):
        self.open_nodes.append(start_node)

    def start():
        while(open_nodes.len > 0):
            node = open_nodes.pop()

            #check if node is goal node
            if(node == goal_node):
                print('done')
                #end
            
            children = get_children(node)
            for child in children:
                if child !is_open(child) and !is_visited(child):
                    open_nodes.append(child)

            visited_nodes.append(node)

    def get_children(parent_node):
        state = parent_node.state
        number_of_rows = len(state)
        number_of_cols = 0
        col = 1
        row = 1
        new_states = []
        for row in state
            number_of_cols = len(row)
            for i in row
                # Can it swap up?
                if(row > 1)
                    new_state = swap_up(state)
                    if new_state not in new_states
                        new_states.append(new_state)
                # Can it swap right?
                if(col < number_of_cols)
                    new_state = swap_right(state)
                    if new_state not in new_states
                        new_states.append(new_state)
                # Can it swap down?
                if(row < number_of_rows)
                    new_state = swap_down(state)
                    if new_state not in new_states
                        new_states.append(new_state)
                # Can it swap left?
                if(col > 1)
                    new_state = swap_left(state)
                    if new_state not in new_states
                        new_states.append(new_state)
                col = col + 1
            row = row + 1

    def is_open(node):
        for i in range(len(open_nodes))
            if(node.state == open_nodes[i].state)
                return true
            else
                return false

    def is_visited(node):
        for i in range(len(visited_nodes))
            if(node.state == visited_nodes[i].state)
                return true
            else
                return false

        
