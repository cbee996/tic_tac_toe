def clean_input(input_str):
    """
    Take a raw input string and attempt to convert it to an integer 1-9.
    Returns the integer if valid, or None if the input is invalid (non-numeric or out of range).
    """
    if input_str is None:
        return None
    try:
        num = int(input_str.strip())
    except ValueError:
        return None
    # Ensure the number is between 1 and 9 inclusive
    if 1 <= num <= 9:
        return num
    return None

def validate_move(board, position):
    """
    Validate that a proposed move is allowed.
    Returns True if the position is between 1 and 9 and the board cell is empty.
    """
    if position < 1 or position > 9:
        return False
    return board.is_empty(position)

def available_moves(board):
    """
    Generator that yields all available move positions (1-9) on the board.
    """
    for pos in range(1, 10):
        if board.is_empty(pos):
            yield pos
