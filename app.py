from DepthFirst import DepthFirstSearch
from IterativeDeep import IterativeDeepening
from a1 import AStar1
from a2 import AStar2
from node import Node
import numpy


def app():
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    goal_state_scaled = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    goal_state_scaled_little = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    goal_state_scaled_little_more = [[1, 2, 3, 4, 5,6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24],  [25, 26, 27, 28, 29, 30],  [31, 32, 33, 34, 35, 36]]
    goal_state_scaled_more = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42], [43, 44, 45, 46, 47, 48, 49]]

    try:
        input_file = open('input.txt', 'r')
        lines = input_file.readlines()

        dfs = DepthFirstSearch(goal_state, lines)
        itedeep = IterativeDeepening(goal_state, lines)
        a1 = AStar1(goal_state, lines)
        a2 = AStar2(goal_state, lines)
        dfs.search()
        itedeep.search()
        a1.search()
        a2.search()
        
    except FileNotFoundError:
        print("File does not exist!")


if __name__ == '__main__':
    app()
