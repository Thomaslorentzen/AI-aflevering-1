class BlockingCars(object):

    def __init__(self, length, width, coord, direction):
        self.coord = coord
        self.length = length - 1
        self.width = width - 1
        self.direction = direction

    def move(self, direction, distance):
        if direction == 'up':
            self.coord['y'] -= distance

        if direction == 'down':
            self.coord['y'] += distance

        if direction == 'left':
            self.coord['x'] -= distance

        if direction == 'right':
            self.coord['x'] += distance

    def __repr__(self):
        if self.orientation == Orientation.HORIZONTAL:
            other_coord = {'x': self.coord['x'] + self.length,
                           'y': self.coord['y']}
            return "{} [{},{}]".format(self.name, self.coord, other_coord)
        else:
            other_coord = {'x': self.coord[
                'x'], 'y': self.coord['y'] + self.length}
            return "{} [{},{}]".format(self.name, self.coord, other_coord)
