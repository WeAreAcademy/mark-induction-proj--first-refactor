import random
import utils

# main function to play Cho Han
def play(guess, bet):
    """Return the net winnings (`int`) from a Cho Han game with the associated wager. Guesses can be either `"Odd"` or `"Even"`.
    """
    # Early return if bet is <= 0
    if bet <= 0: return utils.handle_zero_bet()

    utils.print_with_divider("Let's play Cho-Han!", before=True, after=False)
    dice_total = roll_die() + roll_die()
    print_dice_total(dice_total)
    outcome = find_outcome(guess, dice_total)
    return utils.find_and_print_winnings(bet, outcome)

# -----------------------
# Helper functions below
# -----------------------


def find_outcome(player_guess, dice_total):
    is_win = is_even_win(player_guess, dice_total) or is_odd_win(player_guess, dice_total)
    return utils.GAME_WIN if is_win else utils.GAME_LOSS

def is_even_win(guess, dice_total):
    return utils.is_even(guess) and dice_total % 2 == 0

def is_odd_win(guess, dice_total):
    return utils.is_odd(guess) and dice_total % 2 == 1

def print_dice_total(dice_total):
    print(f"The sum of the two dice is {dice_total}")

def print_selected_cards(player_card, computer_card):
    print(f"Your card was {player_card}")
    print(f"Their card was {computer_card}")

def roll_die():
    return random.randint(1, 6)