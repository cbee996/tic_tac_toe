import random
from game import utils
import tools.display as disp

class Player:
    """Player class representing a Tic-Tac-Toe player (human or computer)."""
    def __init__(self, name, marker, is_computer=False):
        """
        Initialize a Player with a name, marker ('X' or 'O'), and type (human or computer).
        If the player is a computer and no name is provided, defaults to 'Computer'.
        If the player is human and no name is provided, defaults to 'Player'.
        """
        if is_computer and (not name or name.strip() == ""):
            name = "Computer"
        elif not name or name.strip() == "":
            name = "Player"
        self.name = name
        self.marker = marker
        self.is_computer = is_computer

    def get_move(self, board):
        """
        Determine the next move for the player.
        - For a human player: prompt for input until a valid move is entered.
        - For a computer player: select a random available move on the board.
        """
        if self.is_computer:
            # Computer player's turn: choose a random available position.
            disp.show_turn(self)  # Announce the computer's turn
            available = list(utils.available_moves(board))
            if not available:
                return None  # No moves available (shouldn't happen if game isn't over)
            move = random.choice(available)
            # Announce the computer's chosen move
            disp.show_computer_move(self, move)
            return move
        else:
            # Human player's turn: keep prompting until a valid move is entered.
            while True:
                disp.show_turn(self)
                user_input = input("Enter a position (1-9): ")
                position = utils.clean_input(user_input)
                if position is None:
                    # Input is not a valid integer in the range 1-9
                    disp.show_invalid_input()
                    continue
                if not utils.validate_move(board, position):
                    # The position is either out of range or already occupied
                    disp.show_invalid_move()
                    continue
                # Valid move entered; return it as an integer
                return position
