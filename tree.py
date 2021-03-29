import time
import Grid
import HeroCars
import BlockingCars
from sys import maxsize


# Code to build our tree
# class Game_tree():

#   def __init__(self, board, root_node, tree_depth):
#      self.board = board
#     self.root_node = root_node
#    self.depth = tree_depth

# def add_node(self):
#   pass


class Node:
    def __init__(self, node_depth, value, board_state):
        self.node_depth = node_depth
        self.value = value
        self.children = []
        self.board_state = board_state
        self.add_node()

    board = Grid.Board

    def add_node(self, node_depth, value, board_state):
        self.children.append(Node(node_depth, value, board_state))
