import BlockingCars
from HeroCars import HeroCars
from BlockingCars import BlockingCars
import random
from pprint import pprint


# Vi skal få X og Y koordinaterne i bilklassen til at stemme overens med hvor de placeres på boardet
# TYPE not subscriptable - hvad betyder det?
#

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
    Grid1_x_end = 5
    Grid1_y_start = 5
    Grid1_y_end = 11

    Grid2_x_start = 5
    Grid2_x_end = 9
    Grid2_y_start = 5
    Grid2_y_end = 11

    Grid3_x_start = 9
    Grid3_x_end = 14
    Grid3_y_start = 5
    Grid3_y_end = 11

    car_list = {

    }

    Board = []

    cars_to_place = 10

    start_pos1_y = 8
    start_pos1_x = 0

    start_pos2_y = 7
    start_pos2_x = 13

    def print_board(self):
        for row in self.Board:
            print(row)
        # print(self.Board)

        # for i in self.car_list.keys():
        #    print(self.car_list.values())

        print("Our direction for c1 is {}".format(Board.car_list["c1"].direction))
        print("our x-coordinates for c1 are {}".format(Board.car_list["c1"].X_coord))
        print("our y coordinates for c1 are {}".format(Board.car_list["c1"].Y_coord))

    def initiate_board(self):

        self.Board = [[["", 0] for i in range(self.board_x)] for j in range(self.board_y)]
        for i in range(self.Grid1_y_start, self.Grid1_y_end):
            for j in range(self.Grid1_x_start, self.Grid1_x_end):
                self.Board[i][j] = ["", 1]

        for i in range(self.Grid2_y_start, self.Grid2_y_end):
            for j in range(self.Grid2_x_start, self.Grid2_x_end):
                self.Board[i][j] = ["", 2]

        for i in range(self.Grid3_y_start, self.Grid3_y_end):
            for j in range(self.Grid3_x_start, self.Grid3_x_end):
                self.Board[i][j] = ["", 3]

        self.Board[self.start_pos1_y][self.start_pos1_x][0] = "H1"
        self.Board[self.start_pos2_y][self.start_pos2_x][0] = "H2"

        while self.cars_to_place > 0:

            random_x = random.randrange(self.Grid1_x_start, self.Grid3_x_end)
            random_y = random.randrange(self.Grid1_y_start, self.Grid3_y_end)
            direction = ""
            is_occupied = self.Board[random_x][random_y][0] == ""
            # print("value: {}".format(is_occupied))
            # print("{}".format(self.cars_to_place))
            # print("{} and {} are our coordinates".format(random_x, random_y))
            if self.Board[random_x][random_y][0] == "":
                print("Du er i if statement chap, med " + str(self.cars_to_place) + " biler at skulle placere din nar")
                print("{} and {} are our coordinates".format(random_x, random_y))
                # car = Car("c" + str(self.cars_to_place), random_x, random_y, direction)
                if random.randrange(0, 2) == 0:
                    direction = "vertical"
                else:
                    direction = "horizontal"
                car = Car("c" + str(self.cars_to_place), random_x, random_y, direction)
                self.Board[random_y][random_x][0] = ["c" + str(self.cars_to_place)]
                self.cars_to_place = self.cars_to_place - 1
                self.car_list["c" + str(self.cars_to_place)] = car
            else:
                continue
        # for obj in self.car_list:

    #            print(obj.id, obj.direction)

    # print(self.car_list.keys())
    # print(self.car_list.values())

    #  These functions are shifting the grid. They need to first remark the fields that was the original grid to 0.
    #  Then It will mark the fields that now mark the grids new position with the numbers 1,2 or 3 depending on the grid.
    #  Finaly it needs to check for car placements on the old grid and then save thosee to put into the new grid.

    def move_car(self, car, movement_num, direction):
        self.car = car
        self.movement_num = movement_num
        self.direction = direction

        if self.car in Board.car_list.keys():
            if Board.car_list[self.car].direction == "vertical":
                if self.direction == "up":
                    test_i_board = Board.car_list[self.car].Y_coord - movement_num < 5
                    print("Værdien er {}".format(test_i_board))
                    if not Board.car_list[self.car].Y_coord - movement_num < 5:
                        test = self.Board[Board.car_list[self.car].Y_coord - movement_num][Board.car_list[self.car].X_coord][0] == ""
                        print("Der er ikke nogen bil her")
                        print("koordinaterne er {}, {}".format(Board.car_list[self.car].X_coord, Board.car_list[self.car].Y_coord))

                        return False
                    if self.Board[Board.car_list[self.car].Y_coord
                                  - movement_num][Board.car_list[self.car].X_coord][0] == "":
                        print("Du er helt inde nu!")

                        self.Board[Board.car_list[self.car].Y_coord][Board.car_list[self.car].X_coord] = ""
                        self.Board[Board.car_list[self.car].Y_coord - movement_num][Board.car_list \
                            [self.car].X_coord][0] = Board.car_list[self.car].id
                        # self.Board.car_list[self.car.Y_coord - movement_num][self.car.X_coord][0] = Board.car_list[self.car].id
                        Board.car_list[self.car].Y_coord = Board.car_list[self.car].Y_coord - movement_num
                        print("Vi er i else statement nu!")
                    else:
                        pass
                        #self.Board[Board.car_list[self.car].Y_coord][Board.car_list[self.car].X_coord] = ""
                        #self.Board[Board.car_list[self.car].Y_coord - movement_num][Board.car_list\
                        #[self.car].X_coord][0] = Board.car_list[self.car].id
                        #self.Board.car_list[self.car.Y_coord - movement_num][self.car.X_coord][0] = Board.car_list[self.car].id
                        #Board.car_list[self.car].Y_coord = Board.car_list[self.car].Y_coord - movement_num
                        #print("Vi er i else statement nu!")

        if self.car in Board.car_list:
            if Board.car_list[self.car].direction == "vertical":
                if self.direction == "down":
                    if car.Y_coord + movement_num > 11:
                        return False
                    if not Board[car.X_coord][car.Y_coord + movement_num][0]:
                        return False
                    else:
                        Board[car.X_coord][car.Y_coord][0] = ""
                        Board[car.X_coord][car.Y_coord + movement_num][0] = car.id
                        car.Y_coord = car.Y_coord + movement_num

        if self.car in Board.car_list:
            if Board.car_list[self.car].direction == "horizontal":
                if self.direction == "left":
                    if car.X_coord - movement_num < 0:
                        return False
                    if not Board[car.X_coord - movement_num][car.Y_coord][0]:
                        return False
                    else:
                        Board[car.X_coord][car.Y_coord][0] = ""
                        Board[car.X_coord - movement_num][car.Y_coord][0] = car.id
                        car.X_coord = car.X_coord - movement_num

        if self.car in Board.car_list:
            if Board.car_list[self.car].direction == "horizontal":
                if self.direction == "right":
                    if car.X_coord + movement_num > 13:
                        return False
                    if not Board[car.X_coord + movement_num][car.Y_coord][0]:
                        return False
                    else:
                        Board[car.X_coord][car.Y_coord][0] = ""
                        Board[car.X_coord + movement_num][car.Y_coord][0] = car.id
                        car.X_coord = car.X_coord + movement_num


# tests
Board1 = Board()
print("initiate board")

Board1.initiate_board()

Board1.print_board()
# print("vi forsøger at bevæge bilen for helvede")
Board1.move_car("c1", 1, "up")
Board1.print_board()
