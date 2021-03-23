import BlockingCars
from HeroCars import HeroCars
from BlockingCars import BlockingCars
import random


class Car:
    def __init__(self, id, X_coord, Y_coord, direction):
        self.id = id
        self.direction = direction
        self.Y_coord = Y_coord
        self.X_coord = X_coord


class Board:
    board_x = 14
    board_y = 16

    # The different grids that can be shifted with the shift card. Start and end positions for the loops

    Grid1_x_start = 0
    Grid1_x_end = 4
    Grid1_y_start = 5
    Grid1_y_end = 11

    Grid2_x_start = 5
    Grid2_x_end = 8
    Grid2_y_start = 5
    Grid2_y_end = 11

    Grid3_x_start = 9
    Grid3_x_end = 14
    Grid3_y_start = 5
    Grid3_y_end = 11

    Carlist = []

    Board = []
    pair = ["", 0]
    pair1 = ["", 1]
    pair2 = ["", 2]
    pair3 = ["", 3]
    cars_to_place = 10

    # should be its own function to initializee board.
    for Row in range(board_x):
        Board.append([pair])
        for Column in range(board_y):
            Board[Row].append([pair])

    for Row in range(Grid1_x_start, Grid1_x_end):
        for Column in range(Grid1_y_start, Grid1_y_end):
            Board[Row][Column] = [pair1]

    for Row in range(Grid2_x_start, Grid2_x_end):
        for Column in range(Grid2_y_start, Grid2_y_end):
            Board[Row][Column] = [pair2]

    for Row in range(Grid3_x_start, Grid3_x_end):
        for Column in range(Grid3_y_start, Grid3_y_end):
            Board[Row][Column] = [pair3]

    while cars_to_place > 0:
        random_x = random.randrange(Grid1_x_start, Grid3_x_end)
        random_y = random.randrange(Grid1_y_start, Grid3_y_end)
        direction = "vertical"
        temp = Board[random_x][random_y]
        print("Du er inde i while loopet :D ")
        if not temp[0][0]:
            print("Du er i if statement chap, med " + str(cars_to_place) + " biler at skulle placere din nar")
            car = Car("c" + str(cars_to_place), random_x, random_y, direction)
            temp[0][0] = car.id
            cars_to_place = cars_to_place - 1
        else:
            print("Du er en tard " + str(cars_to_place))
            continue

    #  These functions are shifting the grid. They need to first remark the fields that was the original grid to 0.
    #  Then It will mark the fields that now mark the grids new position with the numbers 1,2 or 3 depending on the grid.
    #  Finaly it needs to check for car placements on the old grid and then save thosee to put into the new grid.

    def shiftGrid(self, Grid, shift):
        # Check if grid is valid
        if Grid not in range(1, 3):
            print("grid not valid. Pick a number between 1 and 3")

        #  Check the if the shift is valid. Remmeber to expand this to the new positions of the grids after a shift. Validity should rely on the new x positions of the grid.
        if shift not in range(-5, 5):
            print("shift is out of bounds, make sure shift is within the board")

        #  Removes the old grid
        elif Grid == 1:
            for Row in range(self.Grid1_x_start, self.Grid1_x_end):
                for Column in range(self.Grid1_y_start, self.Grid1_y_end):
                    self.Board[Row][Column] = [Board.pair]

            #  Marks the new grid
            for Row in range(self.Grid1_x_start, self.Grid1_x_end):
                for Column in range(self.Grid1_y_start + shift, self.Grid1_y_end + shift):
                    self.Board[Row][Column] = [Board.pair1]

            Board.Grid1_y_start += shift
            Board.Grid1_y_end += shift


        #  Removes the old grid
        elif Grid == 2:

            for Row in range(Board.Grid2_x_start, Board.Grid2_x_end):
                for Column in range(self.Grid1_y_start, self.Grid1_y_end):
                    self.Board[Row][Column] = [Board.pair]

            #  Marks the new grid
            for Row in range(self.Grid2_x_start, self.Grid2_x_end):
                for Column in range(self.Grid1_y_start + shift, self.Grid1_y_end + shift):
                    self.Board[Row][Column] = [Board.pair2]

            Board.Grid2_y_start += shift
            Board.Grid2_y_end += shift

        #  Removes the old grid
        elif Grid == 3:

            for Row in range(self.Grid3_x_start, self.Grid3_x_end):
                for Column in range(self.Grid1_y_start, self.Grid1_y_end):
                    self.Board[Row][Column] = [Board.pair]

            #  Marks the new grid
            for Row in range(self.Grid3_x_start, self.Grid3_x_end):
                for Column in range(self.Grid1_y_start + shift, self.Grid1_y_end + shift):
                    self.Board[Row][Column] = [Board.pair3]

            Board.Grid3_y_start += shift
            Board.Grid3_y_end += shift


# tests
Board1 = Board()
print("Board1 before shift:")
print(Board1.Board)

Board1.shiftGrid(1, 4)

car = HeroCars()
print("Board1 after shift: ")
print(Board1.Board)
