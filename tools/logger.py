from pathlib import Path
import datetime
from game.board import Board  # Importing Board for access to board state lines

class Logger:
    """Logger class responsible for recording the game moves and results to a log file."""
    def __init__(self):
        # Set up base directory for logs (tic_tac_toe/game_log). Create if it doesn't exist.
        base_path = Path(__file__).resolve().parent.parent  # Path to tic_tac_toe/ directory
        self.log_root = base_path / "game_log"
        self.log_root.mkdir(exist_ok=True)
        self.game_number = None
        self.log_file = None

    def start_game_log(self, player1, player2):
        """
        Prepare a new game log file in a new directory (game1, game2, ...) under game_log.
        Writes initial information like player names and who goes first.
        """
        # Determine the next game number by checking existing game directories
        existing_dirs = [d for d in self.log_root.iterdir() if d.is_dir() and d.name.startswith("game")]
        max_num = 0
        for d in existing_dirs:
            try:
                num = int(d.name.replace("game", ""))
                if num > max_num:
                    max_num = num
            except ValueError:
                continue
        # Next game directory index
        self.game_number = max_num + 1
        game_dir = self.log_root / f"game{self.game_number}"
        game_dir.mkdir(exist_ok=True)

        # Open the log file for writing
        self.log_file = open(game_dir / "log.txt", "w", encoding="utf-8")
        # Write header and player info
        self.log_file.write(f"Game {self.game_number} Log\n")
        self.log_file.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        self.log_file.write("Players:\n")
        self.log_file.write(f"- {player1.name} ({player1.marker})\n")
        self.log_file.write(f"- {player2.name} ({player2.marker})\n\n")
        # Note: X always starts in this implementation
        self.log_file.write(f"First move: {player1.name}\n\n")
        self.log_file.write("Moves:\n")
        self.log_file.flush()

    def log_move(self, move_number, player, position, board):
        """
        Record a single move in the log file, including move number, player name, chosen position,
        and the board state after the move.
        """
        if self.log_file is None:
            return  # Logging has not been initialized
        # Log the move details
        self.log_file.write(f"Move {move_number}: {player.name} -> Position {position}\n")
        # Log the board state after this move
        self.log_file.write(f"Board after move {move_number}:\n")
        for line in board.get_lines():
            self.log_file.write(line + "\n")
        self.log_file.write("\n")  # Blank line to separate moves
        self.log_file.flush()

    def log_result(self, result_text):
        """
        Log the final result of the game (win or draw) and close the log file.
        `result_text` should be a string like "Alice wins!" or "Draw".
        """
        if self.log_file is None:
            return
        self.log_file.write(f"Result: {result_text}\n")
        self.log_file.close()
        self.log_file = None
