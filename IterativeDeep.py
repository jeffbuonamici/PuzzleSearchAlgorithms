from node import Node
from copy import deepcopy
import time

class IterativeDeepening:
    # setup starting node (random puzzle state)

    def __init__(self, goal, start_node, max_search_depth):
        self.open_nodes = []
        self.visited_nodes = []
        self.goal_state = goal
        self.start_node = start_node
        self.open_nodes.append(start_node)
        self.max_search_depth = max_search_depth

    def start(self):
        print("\nGOAL")
        print(self.goal_state)
        print("Starting Node")
        print(self.open_nodes[0].state)
        timeout = time.time() +(60 * 1)
        while self.open_nodes:
            current = self.open_nodes.pop()
            self.visited_nodes.append(current)

            if time.time() > timeout:
                print("timeout")
                self.report(current, True, self.clean(self.start_node.state))
                break
           

            # check if node is goal node
            if(current.state == self.goal_state):
                print('Solution found')
                self.report(current, False , self.clean(self.start_node.state))
                break
                # end
            
            children = self.get_children(current)
            for child in children:
                if self.unique(child.state) and child.depth <= self.max_search_depth:
                    self.open_nodes.append(child)
            if not self.open_nodes:
                self.max_search_depth += 1
                self.visited_nodes.clear()
                self.open_nodes.append(self.start_node)

        print("END")
        
      

    def get_children(self, parent_node):
        state = parent_node.state
        new_states = []
        row_index = 0
        col_index = 0
        for row in state:
            col_index = 0
            for col in row:
                if(row_index < len(state)-1):
                    new_state = self.swap_down(
                        parent_node, row_index, col_index)
                    if new_state not in new_states:
                        new_states.append(new_state)
                if(row_index > 1):
                    new_state = self.swap_up(parent_node, row_index, col_index)
                    if new_state not in new_states:
                        new_states.append(new_state)
                if(col_index > 1):
                    new_state = self.swap_left(
                        parent_node, row_index, col_index)
                    if new_state not in new_states:
                        new_states.append(new_state)
                if(col_index < len(row)-1):
                    new_state = self.swap_right(
                        parent_node, row_index, col_index)
                    if new_state not in new_states:
                        new_states.append(new_state)
               
                col_index += 1
            row_index += 1
        return self.create_nodes(new_states, parent_node)

    def swap_up(self, parent_node, row, col):
        new_state = deepcopy(parent_node.state)
        temp = new_state[row][col]
        new_state[row][col] = new_state[row-1][col]
        new_state[row-1][col] = temp
        return new_state

    def swap_left(self, parent_node, row, col):
        new_state = deepcopy(parent_node.state)
        temp = new_state[row][col]
        new_state[row][col] = new_state[row][col-1]
        new_state[row][col-1] = temp
        return new_state

    def swap_down(self, parent_node, row, col):
        new_state = deepcopy(parent_node.state)
        temp = new_state[row][col]
        new_state[row][col] = new_state[row+1][col]
        new_state[row+1][col] = temp
        return new_state

    def swap_right(self, parent_node, row, col):
        new_state = deepcopy(parent_node.state)
        temp = new_state[row][col]
        new_state[row][col] = new_state[row][col+1]
        new_state[row][col+1] = temp
        return new_state

    def unique(self, node_state):
        open_states = []
        visited_states = []
        for open_node in self.open_nodes:
            open_states.append(open_node.state) 
        for visited_node in self.visited_nodes:
            visited_states.append(visited_node.state) 

        if node_state not in open_states and node_state not in visited_states:
            return True     
        return False

    
    def create_nodes(self, new_states, parent_node):
        new_nodes = []
        for state in new_states:
            new_nodes.append(Node(state, parent_node, parent_node.depth + 1))
        return new_nodes

    def report(self, node, is_timeout, filename):
        sol = open("deepSolution" + filename + ".txt", "w")
        sol.write("--------- deepSolution.txt ---------\n")
        search = open("deepSearch" + filename + ".txt", "w")
        search.write("--------- deepSearch.txt ---------\n")
       
        if(is_timeout):
            sol.write("No Solution")
            search.write("No Solution")
        else:
            for node in self.get_path_to_root(node):
                sol.write(str(node.state) + "\n")
            for node in self.visited_nodes:
                search.write(str(node.state) + "\n")
        
        
        

    def get_path_to_root(self, node):
        path = []
        while node is not None:
            path.append(node)
            node = node.parent
        path.reverse()
        return path
        
    def clean(self, input):
        return ''.join(str(e) for e in input)
        
