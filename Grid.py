import BlockingCars
from HeroCars import HeroCars
from BlockingCars import BlockingCars
import random
from pprint import pprint


class Car:
    def __init__(self, id, X_coord, Y_coord, direction):
        self.id = id
        self.direction = direction
        self.Y_coord = Y_coord
        self.X_coord = X_coord


class Board:

    # should be its own function to initializee board.

    def __init__(self):
        pass

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

    car_list = []

    Board = []

    cars_to_place = 10

    start_pos1_x = 0
    start_pos1_y = 7

    start_pos2_x = 13
    start_pos2_y = 7

    def initiate_board(self):
        for Row in range(self.board_x):
            self.Board.append(["", 0])
            for Column in range(self.board_y):
                self.Board[Row].append(["", 0])

        for Row in range(self.Grid1_x_start, self.Grid1_x_end):
            for Column in range(self.Grid1_y_start, self.Grid1_y_end):
                self.Board[Row][Column] = ["", 1]

        for Row in range(self.Grid2_x_start, self.Grid2_x_end):
            for Column in range(self.Grid2_y_start, self.Grid2_y_end):
                self.Board[Row][Column] = ["", 2]

        for Row in range(self.Grid3_x_start, self.Grid3_x_end):
            for Column in range(self.Grid3_y_start, self.Grid3_y_end):
                self.Board[Row][Column] = ["", 3]

        self.Board[self.start_pos1_x][self.start_pos1_y][0] = "H1"
        self.Board[self.start_pos2_x][self.start_pos2_y][0] = "H2"

        while self.cars_to_place > 0:

            random_x = random.randrange(self.Grid1_x_start, self.Grid3_x_end)
            random_y = random.randrange(self.Grid1_y_start, self.Grid3_y_end)
            direction = "vertical"
            if not self.Board[random_x][random_y][0]:
                print("Du er i if statement chap, med " + str(self.cars_to_place) + " biler at skulle placere din nar")
                print("{} and {} are our coordinates".format(random_x, random_y))
                car = Car("c" + str(self.cars_to_place), random_x, random_y, direction)
                if random.randrange(0, 2) == 0:
                    car.direction = "vertical"
                else:
                    car.direction = "horizontal"
                self.Board[random_x][random_y][0] = car.id
                self.cars_to_place = self.cars_to_place - 1
                self.car_list.append(car)
            else:
                continue
        for obj in self.car_list:
            print(obj.id, obj.direction)

    #  These functions are shifting the grid. They need to first remark the fields that was the original grid to 0.
    #  Then It will mark the fields that now mark the grids new position with the numbers 1,2 or 3 depending on the grid.
    #  Finaly it needs to check for car placements on the old grid and then save thosee to put into the new grid.

    def move_car(self, car, movement_num, Board, direction):
        self.car = car
        self.movement_num = movement_num
        self.board = Board
        self.direction = direction

        if car.id in Board.car_list:
            if car.direction == "vertical":
                if self.direction == "up":
                    if car.Y_coord - movement_num < 5:
                        return False
                    if not Board[car.X_coord][car.Y_coord - movement_num][0]:
                        return False
                    else:
                        Board[car.X_coord][car.Y_coord][0] = ""
                        Board[car.X_coord][car.Y_coord - movement_num][0] = car.id
                        car.Y_coord = car.Y_coord - movement_num

        if car.id in Board.car_list:
            if car.direction == "vertical":
                if self.direction == "down":
                    if car.Y_coord + movement_num > 11:
                        return False
                    if not Board[car.X_coord][car.Y_coord + movement_num][0]:
                        return False
                    else:
                        Board[car.X_coord][car.Y_coord][0] = ""
                        Board[car.X_coord][car.Y_coord + movement_num][0] = car.id
                        car.Y_coord = car.Y_coord + movement_num

        if car.id in Board.car_list:
            if car.direction == "horizontal":
                if self.direction == "left":
                    if car.X_coord - movement_num < 0:
                        return False
                    if not Board[car.X_coord - movement_num][car.Y_coord][0]:
                        return False
                    else:
                        Board[car.X_coord][car.Y_coord][0] = ""
                        Board[car.X_coord - movement_num][car.Y_coord][0] = car.id
                        car.X_coord = car.X_coord - movement_num

        if car.id in Board.car_list:
            if car.direction == "horizontal":
                if self.direction == "right":
                    if car.X_coord + movement_num > 13:
                        return False
                    if not Board[car.X_coord + movement_num][car.Y_coord][0]:
                        return False
                    else:
                        Board[car.X_coord][car.Y_coord][0] = ""
                        Board[car.X_coord + movement_num][car.Y_coord][0] = car.id
                        car.X_coord = car.X_coord + movement_num

    def print_board(self):
        for x in Board.board_x:
            for y in Board.board_y:
                print("{:4}".format(y),
                      print())

        # for x in range(self.board_x):
        #   for y in range(self.board_y):
        #      print(x, y,  end = " ")
        #     print()
        # print("Koordinaterne x og y er {} og {}".format(x, y))
        # pprint(self.Board[x][y])


# tests
Board1 = Board()
print("Board1 before shift:")
Board1.print_board()
# pprint(Board1)
# Board1.shiftGrid(1, 4)
Board1.initiate_board()
car = HeroCars()
# Board1.move_car()
print("Board1 after shift: Jeg er sej")
print(Board1.Board)
