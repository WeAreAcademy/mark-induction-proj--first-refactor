import random
import utils

# main function to play coin flip
def play(guess, bet):
    """Return the net winnings (`int`) from a coin flip game with the associated wager.
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
    return random.choice(['H', "T"])

def find_outcome(flip_one, flip_two):
    is_win = has_coin_flip_equivalence(flip_one, flip_two)
    return utils.GAME_WIN if is_win else utils.GAME_LOSS

def has_coin_flip_equivalence(string_one, string_two):
    is_two_heads = is_heads(string_one) and is_heads(string_two)
    is_two_tails = is_tails(string_one) and is_tails(string_two)
    return is_two_heads or is_two_tails

def is_heads(string):
    return string in heads_variants

def is_tails(string):
    return string in tails_variants

def print_flip(string):
    if is_heads(string):
        print("Heads!")
    elif is_tails(string):
        print("Tails!")