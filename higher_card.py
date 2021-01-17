import random
import utils

# main function to play coin flip
def play(bet):
    # Early return if bet is <= 0
    if bet <= 0: return utils.handle_zero_bet()
    
    utils.print_with_divider("Let's play a game of cards!", before=True, after=False)
    mine = random_card_value()
    theirs = random_card_value()
    print_selected_cards(mine, theirs)

    #Determines who won and returns either bet, -bet or 0 (in the case of a tie.)
    if mine > theirs:
        print("You won " + str(bet)+" dollars!")
        print_divider()
        return bet
    elif mine < theirs:
        print("You lost " + str(bet)+" dollars!")
        print_divider()
        return -bet
    else:
        print("It was a tie!")
        print_divider()
        return 0

# -----------------------
# Helper functions below
# -----------------------

heads_variants = ["H", "h", "Heads", "heads"]
tails_variants = ["T", "t", "Tails", "tails"]

def flip_coin():
    """Randomly return `"H"` or `"T"` to represent a coin flip.
    """
    return random.choice(['H', "T"])

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

def print_selected_cards(player_card, computer_card):
    """Print the player and computer cards.
    """
    print(f"Your card was {player_card}")
    print(f"Their card was {computer_card}")

def random_card_value():
    # Use 1 to 13 to represent Ace to King
    return random.randint(1, 13)