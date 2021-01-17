GAME_TIE = 'tie'
GAME_LOSS = 'lose'
GAME_WIN = 'win'

def calculate_winnings(amount, bet_outcome):
    """Returns the net bet winnings.

    Args:
        is_win (boolean): Whether or not the bet was won
        bet_outcome (str): One of `"win"`, `"lose"` or `"tie"`
    """
    if is_win(bet_outcome):
        # bet doubled
        return amount
    elif is_tie(bet_outcome):
        # bet gained back - no net winnings
        return 0
    else:
        # bet lost
        return -amount


def handle_zero_bet():
    print_with_divider("Your bet should be above 0.", before=True, after=True)
    return 0

def is_loss(bet_outcome):
    return bet_outcome is GAME_LOSS

def is_tie(bet_outcome):
    return bet_outcome is GAME_TIE

def is_win(bet_outcome):
    return bet_outcome is GAME_WIN

def find_and_print_winnings(amount, bet_outcome):
    """Returns the net bet winnings and prints the outcome to the terminal.

    Args:
        is_win (boolean): Whether or not the bet was won
        bet_outcome (str): One of `"win"`, `"lose"` or `"tie"`
    """
    print_bet_outcome(amount, bet_outcome)
    return calculate_winnings(amount, bet_outcome)

def print_bet_outcome(amount, bet_outcome):
    """Announce the bet outcome.

    Args:
        amount (number): The amount wagered.
        bet_outcome (str): One of `"win"`, `"lose"` or `"tie"`
    """
    if is_win(bet_outcome):
        print_with_divider(f"You won {amount} dollars!")
    elif is_loss(bet_outcome):
        print_with_divider(f"You lost {amount} dollars!")
    else:
        print_with_divider("It was a tie!")

def print_divider():
    """Print a divider.
    """
    print("------------------")

def print_with_divider(message, before=False, after=True):
    """Print a string message followed by a divider, optionally sandwiching with a starting divider as well.

    Args:
        message (str): The message to print.
        before (boolean): Whether or not to lead with a divider
        after (boolean): Whether or not to end with a divider
    """
    if before: print_divider()
    print(message)
    if after: print_divider()