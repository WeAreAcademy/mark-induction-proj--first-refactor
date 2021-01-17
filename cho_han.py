import random
import utils

# main function to play Cho Han
def play(guess, bet):
    """Play a higher card game with the associated wager.

    Args:
        bet (int): The amount waged

    Returns: (int) the net winnings
    """
    # Early return if bet is <= 0
    if bet <= 0: return utils.handle_zero_bet()

    utils.print_with_divider("Let's play Cho-Han!", before=True, after=False)
    dice_total = roll_dice(2)
    print_dice_total(dice_total)
    outcome = find_outcome(guess, dice_total)
    return utils.find_and_print_winnings(bet, outcome)

# -----------------------
# Helper functions below
# -----------------------


def find_outcome(player_guess, dice_total):
    """Return the game outcome based on the player guess and dice total.

    Args:
        player_guess (str): The predicted coin flip
        bet (int): The amount waged
    """
    is_win = is_even_win(player_guess, dice_total) or is_odd_win(player_guess, dice_total)
    return utils.GAME_WIN if is_win else utils.GAME_LOSS

def is_even_win(guess, dice_total):
    """Check whether the game has an even win.

    Args:
        guess (str): The player guess
        dice_total (int): The dice total
    """
    return utils.is_even(guess) and dice_total % 2 is 0

def is_odd_win(guess, dice_total):
    """Check whether the game has an odd win.

    Args:
        guess (str): The player guess
        dice_total (int): The dice total
    """
    return utils.is_odd(guess) and dice_total % 2 is 1

def print_dice_total(dice_total):
    print(f"The sum of the two dice is {dice_total}")

def print_selected_cards(player_card, computer_card):
    print(f"Your card was {player_card}")
    print(f"Their card was {computer_card}")

def roll_die():
    return random.randint(1, 6)

def roll_dice(dice_count = 2):
    total = 0
    for die in range(dice_count):
        total += roll_die()
    return total