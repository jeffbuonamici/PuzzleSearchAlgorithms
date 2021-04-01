from node import Node
from queue import PriorityQueue
import util
import time
from timeit import default_timer as timer

class AStar1:
    # setup starting node (random puzzle state)
    def __init__(self,goal_state,lines):
        self.goal_state = goal_state
        self.lines = lines
        open("a1_analysis.txt", "w")

    def reset(self, start_node):
        self.open_nodes = []
        self.visited_nodes = []
        self.start_node = start_node
        self.open_nodes = PriorityQueue()
        self.open_nodes.put((start_node.fscore, start_node))

    def search(self):
        total_search = 0
        total_sol = 0
        total_time = 0
        total_cost = 0
        for input_line in self.lines:
            input = eval(util.createGraph(input_line))
            start_node = Node(input, None, 0, 0)
            self.reset(start_node)
            sol, search, depth, time = self.run()
            total_search += search
            total_sol += sol
            total_time += time
            total_cost += depth
        a = open("a1_analysis.txt", "a")
        a.write("Average solution length : "+str(total_sol/len(self.lines))+"\n")
        a.write("Average search length : "+str(total_search/len(self.lines))+"\n")
        a.write("Average time : "+str(total_time/len(self.lines))+"\n")
        a.write("Average cost : "+str(total_cost/len(self.lines))+"\n")
        a.write("Total solution length : "+str(total_sol)+"\n")
        a.write("Total search length : "+str(total_search)+"\n")
        a.write("Total time : "+str(total_time)+"\n")
        a.write("Total cost : "+str(total_cost)+"\n")
        
    def run(self):
        print("START")
        print(self.start_node.state)
        timeout = time.time() +(60 * 5)
        start_time = time.time()
        while self.open_nodes:
            current = self.open_nodes.get()[1]
            self.visited_nodes.append(current)

            if time.time() > timeout:
                self.report(current, True, self.clean(self.start_node.state))
                break

            # check if node is goal node
            if(current.state == self.goal_state):
                self.report(current, False , self.clean(self.start_node.state))
                break
                # end
            
            children = util.get_children(self,current)
            for child in children:
                if self.unique(child.state):
                    self.open_nodes.put((child.fscore, child))
        end_time = time.time()

        a = open("a1_analysis.txt", "a")
        a.write("State: " + str(self.start_node.state) +", Solution length: "+str(len(self.get_path_to_root(current)))+", Search length: "+str(len(self.visited_nodes))+", Cost: "+str(current.depth)+", Time: "+str(end_time-start_time)+"\n")
        print("END")
        return (len(self.get_path_to_root(current))), (len(self.visited_nodes)), (current.depth), (end_time-start_time)
    
    def create_nodes(self, new_states, parent_node):
        new_nodes = []
        for state in new_states:
            f = self.get_manhattan_distance(state) + parent_node.depth + 1
            new_nodes.append(Node(state, parent_node, parent_node.depth + 1, f))
        return new_nodes

    def get_manhattan_distance(self, state):
        f = 0
        for y_val in range(len(state)):
            for x_val in range(len(state[y_val])):
                vals = self.get_goal_coordinates(state[y_val][x_val])
                f += abs(x_val - vals[0]) + abs(y_val - vals[1])
        return f

    def get_goal_coordinates(self, value):
        for y_val in range(len(self.goal_state)):
            for x_val in range(len(self.goal_state[y_val])):
                if(value == self.goal_state[y_val][x_val]):
                    return x_val, y_val
        return 0, 0

    def report(self, node, is_timeout, filename):
        sol = open("output/manhattanSolution" + filename + ".txt", "w")
        sol.write("--------- dfsSolution.txt ---------\n")
        search = open("output/manhattanSearch" + filename + ".txt", "w")
        search.write("--------- dfsSearch.txt ---------\n")
       
        if(is_timeout):
            sol.write("No Solution")
            search.write("No Solution")
        else:
            for node in self.get_path_to_root(node):
                sol.write(str(node.state) + "\n")
            for node in self.visited_nodes:
                search.write(str(node.state) + "\n")
        
    def unique(self, node_state):
        open_states = []
        visited_states = []
        for open_node in self.open_nodes.queue:
            open_states.append(open_node[1].state) 
        for visited_node in self.visited_nodes:
            visited_states.append(visited_node.state) 

        if node_state not in open_states and node_state not in visited_states:
            return True     
        return False
    
    def get_path_to_root(self, node):
        path = []
        while node is not None:
            path.append(node)
            node = node.parent
        path.reverse()
        return path
        
    def clean(self, input):
        return ''.join(str(e) for e in input)
        
