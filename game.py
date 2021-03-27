import time
import Grid
import HeroCars
import BlockingCars
from sys import maxsize


# Code to build our tree
class Node(object):
    def __init__(self, depth, player_num, nodes_left, value=0):
        self.value = value
        self.nodes_left = nodes_left
        self.player_num = player_num
        self.depth = depth

        self.children = []
        self.create_children()

    def create_children(self):

        if self.depth >= 0:
            for i in range(min, max):
                v = self.nodes_left - i
                self.children.append(Node(self.depth - i,
                                          -self.player_num,
                                          v,
                                          self.RealVal(v)))

    def RealVal(self, value):
        if value == 0:
            return maxsize * self.player_num
        elif value < 0:
            return maxsize * -self.player_num
        return 0

def minmax(node, depth, player):
    if depth == 0 or abs(node.value) == maxsize:
        return node.value
    player_best_val = maxsize * -player

    for i in range(len(node.children)):
        child = node.children[i]
        val = minmax(child, depth - 1, -player)
        if abs(maxsize * player - val) < abs(maxsize * player - player_best_val):
            player_best_val = val

    return player_best_val





class Solver:
    def __init__(self):
        pass

    def min(self):
        pass

    def max(self):
        pass

    def is_valid(self):
        pass


def main():
    game_grid = Grid()
    game_grid.start()
    hc = HeroCars()
    bc = BlockingCars()


main()
