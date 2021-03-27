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

    cars_to_place = 10

    start_pos1_x = 0
    start_pos1_y = 7

    start_pos2_x = 13
    start_pos2_y = 7



    # should be its own function to initializee board.



    for Row in range(board_x):
        Board.append(["", 0])
        for Column in range(board_y):
            Board[Row].append(["", 0])

    for Row in range(Grid1_x_start, Grid1_x_end):
        for Column in range(Grid1_y_start, Grid1_y_end):
            Board[Row][Column] = ["", 1]

    for Row in range(Grid2_x_start, Grid2_x_end):
        for Column in range(Grid2_y_start, Grid2_y_end):
            Board[Row][Column] = ["", 2]

    for Row in range(Grid3_x_start, Grid3_x_end):
        for Column in range(Grid3_y_start, Grid3_y_end):
            Board[Row][Column] = ["", 3]

    Board[start_pos1_x][start_pos1_y][0] = "H1"
    Board[start_pos2_x][start_pos2_y][0] = "H2"

    while cars_to_place > 0:
        random_x = random.randrange(Grid1_x_start, Grid3_x_end)
        random_y = random.randrange(Grid1_y_start, Grid3_y_end)
        direction = "vertical"
        if not Board[random_x][random_y][0]:
            print("Du er i if statement chap, med " + str(cars_to_place) + " biler at skulle placere din nar")
            print("{} and {} are our coordinates".format(random_x, random_y))
            car = Car("c" + str(cars_to_place), random_x, random_y, direction)
            Board[random_x][random_y][0] = car.id
            cars_to_place = cars_to_place - 1
        else:
            continue

    #  These functions are shifting the grid. They need to first remark the fields that was the original grid to 0.
    #  Then It will mark the fields that now mark the grids new position with the numbers 1,2 or 3 depending on the grid.
    #  Finaly it needs to check for car placements on the old grid and then save thosee to put into the new grid.



# tests
Board1 = Board()
print("Board1 before shift:")
print(Board1.Board)

#Board1.shiftGrid(1, 4)

car = HeroCars()
print("Board1 after shift: Jeg er sej")
print(Board1.Board)
