import Grid
import tree


# TODO: Lav AI
# Lav tjeks for at der ikke er biler der blokerer for et træk
# Lav et search tree til at vurdere det
# Minimax algoritme til det
# Rapport


class Player:
    car_dict = {

    }

    def __init__(self, id, board):
        self.id = id
        self.board = board
        self.car_dict = self.board.get_car_dict()

    def update_carpos(self):
        self.car_dict = self.board.get_car_dict()

    def turn_move_car(self, fields_to_move, car_id, driving_direction):
        self.board.move_car(car_id, fields_to_move, driving_direction)


class Game:
    game_is_running = True
    whose_turn = False
    grid = [0][0]
    player1 = None
    player2 = None

    def create_game_tree(self, initial_board):
        self.initial_board = initial_board
        tree_depth = 0
        root_node = tree.Node(tree_depth, 0, initial_board)
        node_holder = root_node
        tree_depth += 1
        board_1 = None
        board_states = []
        is_game_over = self.initial_board.is_game_won()
        player_turn = 1

        while not is_game_over:
            while player_turn == 1:
                node_holder.add_node(tree_depth, 0, initial_board.move_car("H1", 0, "Right"))
                node_holder.add_node(tree_depth, 0, initial_board.move_car("H1", 0, "Left"))
                node_holder = None

            while player_turn == 2:
                node_holder.add_node(tree_depth, 0, initial_board.move_car("H2", 0, "Right"))
                node_holder.add_node(tree_depth, 0, initial_board.move_car("H1", 0, "Left"))

    def evaluate_tree(self):
        pass

    def init_game(self):
        self.grid = Grid.Board()
        self.grid.initiate_board()
        self.grid.print_board()
        self.player1 = Player("H1", self.grid)
        self.player2 = Player("H2", self.grid)

    def run_game(self):
        self.init_game()
        while self.game_is_running:
            if not self.whose_turn:
                self.grid.print_board()
                self.grid.print_car_dir()
                breakpoint()
                car_to_move = input("What car do you want to move?")
                no_of_fields = input("How many fields should it be moved?")
                driving_direction = input("What direction do you want to move?")
                self.player1.turn_move_car(no_of_fields, car_to_move, driving_direction)
                self.grid.print_car_dir()
                self.whose_turn = True
                breakpoint()
                if self.grid.car_list["H1"].X_coord == 13:
                    print("Player 1 has won")
                    self.game_is_running = False
            elif self.whose_turn:
                self.grid.print_board()
                self.grid.print_car_dir()
                car_to_move = input("What car do you want to move?")
                no_of_fields = input("How many fields should it be moved?")
                driving_direction = input("What direction do you want to move?")
                self.player2.turn_move_car(no_of_fields, car_to_move, driving_direction)
                self.grid.print_car_dir()
                self.whose_turn = False
                if self.grid.car_list["H2"].X_coord == 0:
                    print("Player 2 has won")
                    self.game_is_running = False


game = Game()
game.run_game()
