import random
import utils

# main function to play coin flip
def play(guess, bet):
    """Play a coin flip game with the associated wager.

    Args:
        guess (str): The predicted coin flip
        bet (number): The amount waged

    Returns: (number) the net winnings
    """
    # Early return if bet is <= 0
    if bet <= 0: return utils.handle_zero_bet()

    utils.print_with_divider(f"Let's flip a coin! You guessed {guess}", before=False, after=True)
    flip_result = flip_coin()
    print_flip(flip_result)
    outcome = find_outcome(guess, flip_result)
    return utils.find_and_print_winnings(bet, outcome)

# -----------------------
# Helper functions below
# -----------------------

heads_variants = ["H", "h", "Heads", "heads"]
tails_variants = ["T", "t", "Tails", "tails"]

def flip_coin():
    """Randomly return `"H"` or `"T"` to represent a coin flip.
    """
    return random.choice(['H', "T"])

def find_outcome(flip_one, flip_two):
    """Return the game outcome based on two coin flip results.
    """
    is_win = has_coin_flip_equivalence(flip_one, flip_two)
    return utils.GAME_WIN if is_win else utils.GAME_LOSS

def has_coin_flip_equivalence(str_one, str_two):
    """Check whether two strings represent equivalent coin flip states.
    """
    if is_heads(str_one) and is_heads(str_two):
        return True
    elif is_tails(str_one) and is_tails(str_two):
        return True
    else:
        return False

def is_heads(string):
    """Check whether a string represents a coin heads.
    """
    return string in heads_variants

def is_tails(string):
    """Check whether a string represents a coin tails.
    """
    return string in tails_variants

def print_flip(string):
    """Print a coin flip result
    """
    if is_heads(string):
        print("Heads!")
    elif is_tails(string):
        print("Tails!")