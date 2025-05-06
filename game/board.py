class Board:
    """Board class for managing the Tic-Tac-Toe board state and checking win/draw conditions."""
    def __init__(self):
        # Initialize a 3x3 board represented as a list of 9 cells (None indicates an empty cell).
        self.grid = [None] * 9

    def get_lines(self):
        """Return a list of strings representing the current board state in a human-friendly format."""
        # Use position numbers 1-9 for empty cells, or the player's marker (X or O) for occupied cells.
        lines = []
        lines.append(f" {self._cell_str(1)} | {self._cell_str(2)} | {self._cell_str(3)} ")
        lines.append("-----------")
        lines.append(f" {self._cell_str(4)} | {self._cell_str(5)} | {self._cell_str(6)} ")
        lines.append("-----------")
        lines.append(f" {self._cell_str(7)} | {self._cell_str(8)} | {self._cell_str(9)} ")
        return lines

    def _cell_str(self, position):
        """Helper method to get the display string for a cell: a number if empty, or the marker if filled."""
        value = self.grid[position - 1]
        return str(position) if value is None else str(value)

    def place_marker(self, position, marker):
        """Place a player's marker ('X' or 'O') on the board at the given position (1-9)."""
        index = position - 1
        if self.grid[index] is None:
            self.grid[index] = marker

    def check_win(self, marker):
        """Check if the given marker ('X' or 'O') has achieved three in a row (win condition)."""
        b = self.grid  # alias for brevity
        # All possible winning combinations of indices (using 0-based indexing for the list).
        winning_combinations = [
            (0, 1, 2),  # rows
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),  # columns
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),  # diagonals
            (2, 4, 6)
        ]
        # Check each winning combination to see if all three positions hold the marker
        for (i, j, k) in winning_combinations:
            if b[i] == b[j] == b[k] == marker:
                return True
        return False

    def is_draw(self):
        """Check if the game is a draw (board is full with no winner). Should be called after check_win."""
        # If no cell is None, the board is full. Assuming check_win was false, it's a draw.
        return all(cell is not None for cell in self.grid)

    def is_empty(self, position):
        """Return True if the given board position (1-9) is empty."""
        return self.grid[position - 1] is None
