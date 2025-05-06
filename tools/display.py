from game.board import Board  # (Optional import for type hints or direct board access if needed)

def show_welcome(name1, name2):
    """Display a welcome message addressing both players by name."""
    # Ensure names are not empty strings
    if not name1:
        name1 = "Player 1"
    if not name2:
        name2 = "Player 2"
    print(f"\nWelcome, {name1} and {name2}!")

def get_player_name(player_number):
    """
    Prompt the user for a player's name and return it.
    (If the user presses Enter without a name, it will be handled in the Player class defaults.)
    """
    return input(f"Please enter Player {player_number} name: ")

def show_turn(player):
    """Indicate whose turn it is to play."""
    print(f"\n{player.name}'s Turn ({player.marker}):")

def show_invalid_input():
    """Notify the player that their input was not a valid number between 1 and 9."""
    print("Invalid input. Please enter a number between 1 and 9.")

def show_invalid_move():
    """Notify the player that the chosen position is invalid (either taken or out of range)."""
    print("That position is already taken or out of range. Try again.")

def show_winner(player):
    """Announce the winner of the game."""
    print(f"\nCongratulations, {player.name}! You win!")

def show_draw():
    """Announce that the game ended in a draw."""
    print("\nThe game is a draw!")

def ask_play_again():
    """
    Prompt the user to decide if they want to play another game.
    Returns True if the response is 'yes' (or 'y'), False otherwise.
    """
    choice = input("\nWould you like to play again? (yes/no): ")
    if choice is None:
        return False
    choice = choice.strip().lower()
    return choice in ("yes", "y")

def show_goodbye():
    """Display a goodbye message when the players exit the game."""
    print("\nThank you for playing Tic-Tac-Toe! Goodbye.")

def display_board(board):
    """Print the current state of the Tic-Tac-Toe board to the console."""
    print("\nCurrent Board:")
    for line in board.get_lines():
        print(line)

def show_computer_move(player, position):
    """Announce the computer player's chosen move."""
    print(f"{player.name} chooses position {position}.")
