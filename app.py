from DepthFirst import DepthFirstSearch
from node import Node
import numpy


def app():
    input = eval(createGraph('((6; 1; 2); (7; 7; 3); (5; 4; 9))'))
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start_node = Node(input, None, 0)

    dfs = DepthFirstSearch(goal_state,start_node)
    dfs.start()



def createGraph(input):
    return input.replace(';', ',').replace('(','[').replace(')',']')


if __name__ == '__main__':
    app()
