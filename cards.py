import HeroCars
import BlockingCars


def shift_grid():
    while True:
        grid = input("Do you want to shift {L}eft, {R}ight or {M}iddle grid? (x to exit) ")
        if grid.upper() == "L":
            direction_left = input("Press 1 to shift up, 0 to shift down")
            if direction_left == "1":
                print("Shifting left grid upwards")
            elif direction_left == "0":
                print("Shifting left grid downwards")
            elif direction_left == "x":
                print("Ending turn")
                break
            else:
                print("Invalid input! Try again!")
        elif grid.upper() == "R":
            direction_right = input("Press 1 to shift up, 0 to shift down")
            if direction_right == "1":
                print("Shifting right grid upwards")
            elif direction_right == "0":
                print("Shifting right grid downwards")
            elif direction_right == "x":
                print("Ending turn")
                break
            else:
                print("Invalid input! Try again!")
        elif grid.upper() == "M":
            direction_mid = input("Press 1 to shift up, 0 to shift down")
            if direction_mid == "1":
                print("Shifting middle grid upwards")
            elif direction_mid == "0":
                print("Shifting middle grid downwards")
            elif direction_mid == "x":
                print("Ending turn")
                break
            else:
                print("Invalid input! Try again!")
        elif grid.upper() == "x":
            print("Exiting shifting")
            break
        else:
            print("Invalid input! Try again!")


class Cards:
    discard_pile = []

    cards = []

    def __init__(self):
        self.cards = []
        self.discard_pile = []

    def main(self):
        shift_grid()

    def look_at_deck(self):
        pass

    def move(self):
        pass

    if __name__ == '__main__':
        main()
