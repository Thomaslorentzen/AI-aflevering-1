class BlockingCars:

    def small_blocking_cars(self):
        width = 1
        length = 1
        cars = [width, length]

    def big_blocking_cars(self):
        width = 1
        length = 2
        cars = [width, length]

    def movement_blocking_cars(self, Direction):
        if Direction == "up":
            if self.row > 0:
                if self.CollisionCheck("up") == False:
                    self.column -= 1

        elif Direction == "DOWN":
            if self.Row < MapSize - 1:
                if self.CollisionCheck("DOWN") == False:
                    self.Row += 1

        Map.update()

    def Location(self):
        print("Coordinates: " + str(self.Column) + ", " + str(self.Row))

    def CollisionCheck(self,
                       Direction):  # Checks if anything is on top of the grass in the direction that the character wants to move. Used in the move function
        if Direction == "UP":
            if len(Map.Grid[self.Column][(self.Row) - 1]) > 1:
                return True
        elif Direction == "DOWN":
            if len(Map.Grid[self.Column][(self.Row) + 1]) > 1:
                return True
        return False
