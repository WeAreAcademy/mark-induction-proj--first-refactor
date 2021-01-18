# Utility functions common for games

# Helpful constants
GAME_TIE = 'tie'
GAME_LOSS = 'lose'
GAME_WIN = 'win'
GAME_WIN_ROULETTE_EXACT = 'roulette-straight-up'

even_variants = ["even", "Even"]
odd_variants = ["odd", "Odd"]

def calculate_winnings(wagered_amount, bet_outcome):
    """Returns the net bet winnings (i.e. negative value for a loss)
    """
    if is_win(bet_outcome):
        # bet doubled
        return wagered_amount
    elif is_tie(bet_outcome):
        # bet gained back - no net winnings
        return 0
    elif is_roulette_straight_win(bet_outcome):
        # special case in roulette that returns 35x payout
        return 35 * wagered_amount
    else:
        # bet lost
        return -wagered_amount

def find_and_print_winnings(amount, bet_outcome):
    print_bet_outcome(amount, bet_outcome)
    return calculate_winnings(amount, bet_outcome)

def handle_zero_bet():
    print_with_divider("Your bet should be above 0.", before=True, after=True)
    return 0

def is_even(string):
    return string in even_variants

def is_loss(bet_outcome):
    return bet_outcome is GAME_LOSS

def is_odd(string):
    return string in odd_variants

def is_roulette_straight_win(bet_outcome):
    return bet_outcome is GAME_WIN_ROULETTE_EXACT

def is_tie(bet_outcome):
    return bet_outcome is GAME_TIE

def is_win(bet_outcome):
    return bet_outcome is GAME_WIN

def print_bet_outcome(amount, bet_outcome):
    if is_win(bet_outcome) or is_roulette_straight_win(bet_outcome):
        print_with_divider(f"You won {amount} dollars!")
    elif is_loss(bet_outcome):
        print_with_divider(f"You lost {amount} dollars!")
    elif is_tie(bet_outcome):
        print_with_divider("It was a tie!")

def print_divider():
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