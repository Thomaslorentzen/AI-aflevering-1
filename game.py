import time
import Grid
import HeroCars
import BlockingCars


class Maingame:
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.current_state = []

    def draw_board(self):
        pass

    def min(self):
        px = None
        py = None



    def max(self):
        px = None
        py = None


def main():
    game_grid = Grid()
    game_grid.start()
    hc = HeroCars()
    bc = BlockingCars()


main()
