from DepthFirst import DepthFirstSearch
from IterativeDeep import IterativeDeepening
from node import Node
import numpy


def app():
    try:
        input_file = open('input.txt', 'r')
        lines = input_file.readlines()
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for input_line in lines:
            print(input_line)
            input = eval(createGraph(input_line))
            start_node = Node(input, None, 0)

            dfs = IterativeDeepening(goal_state,start_node)
            dfs.start()
    except FileNotFoundError:
        print("File does not exist!")



def createGraph(input):
    return input.replace(';', ',').replace('(','[').replace(')',']')

if __name__ == '__main__':
    app()
