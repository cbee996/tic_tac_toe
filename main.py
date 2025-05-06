import tools.display as disp
import tools.logger as log_tool
from game.board import Board
from game.players import Player

def main():
    """Main function to control game flow of Tic-Tac-Toe."""
    # Create a Logger instance for logging games
    logger = log_tool.Logger()
    while True:
        # Prompt for player names (Player 2 can be 'Computer' for AI)
        name1 = disp.get_player_name(1)
        name2 = disp.get_player_name(2)
        # Set default names if inputs are empty, and determine if Player 2 is a computer
        is_computer = False
        if name1 is None or name1.strip() == "":
            name1 = "Player 1"
        if name2 is None or name2.strip() == "" or name2.strip().lower() == "computer":
            name2 = "Computer"
            is_computer = True

        # Display a welcome message with the player names
        disp.show_welcome(name1, name2)

        # Initialize Player objects, the Board, and start a new game log
        player1 = Player(name1, 'X')
        player2 = Player(name2, 'O', is_computer=is_computer)
        board = Board()
        logger.start_game_log(player1, player2)

        # X always starts first
        current_player = player1
        move_number = 0
        game_over = False

        # Show the initial empty board
        disp.display_board(board)

        # Main gameplay loop
        while not game_over:
            # Get the current player's move (handles input or computer decision)
            move = current_player.get_move(board)
            # Place the move on the board
            board.place_marker(move, current_player.marker)
            move_number += 1
            # Log this move in the game log
            logger.log_move(move_number, current_player, move, board)
            # Display the board after the move
            disp.display_board(board)
            # Check for win or draw conditions
            if board.check_win(current_player.marker):
                # Current player wins
                disp.show_winner(current_player)
                logger.log_result(f"{current_player.name} wins!")
                game_over = True
            elif board.is_draw():
                # Board is full and no winner -> draw
                disp.show_draw()
                logger.log_result("Draw")
                game_over = True
            else:
                # Switch turns and continue
                current_player = player2 if current_player == player1 else player1

        # Ask if players want to play again; if not, exit the loop
        if not disp.ask_play_again():
            disp.show_goodbye()
            break

if __name__ == "__main__":
    main()
