class HeroCars:
    def player_hero_car(self):
        hero_width = 1
        hero_length = 1
        hero_car = [hero_length, hero_width]

    def movement_hero_cars(self, Direction):
        if Direction == "RIGHT":
            if self.Column < MapSize - 1:
                if self.CollisionCheck("RIGHT") == False:
                    self.Column += 1
        map.update()

    def CollisionCheck(self, Direction):
        if Direction == "RIGHT":
            if len(Map.Grid[self.Column + 1][(self.Row)]) > 1:
                return True
        return False
