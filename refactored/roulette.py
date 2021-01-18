import random
import utils

# main function to play Roulette
def play(guess, bet):
    """Play a roulette game with the associated wager. Guesses can be either `"Odd"`, `"Even"` or a string/integer representing `"00"`, `"0"`, `"1"`, ... `"36"`

    Args:
        guess (str or int)
        bet (int): The amount waged

    Returns: (int) the net winnings
    """
    # Early return if bet is <= 0
    if bet <= 0: return utils.handle_zero_bet()

    parsed_guess = str(guess) # convert guess to string for predictability

    #A standard roulette wheel has the numbers 0 through 36 as well as 00. We'll use 37 to represent 00.
    utils.print_with_divider("Let's play roulette!", before=True, after=False)
    result = spin_wheel()
    print_roulette_result(result)
    outcome = find_outcome(parsed_guess, result)
    return utils.find_and_print_winnings(bet, outcome)

# -----------------------
# Helper functions below
# -----------------------

# 0 and 00 don't count as odd or even
non_standard_numbers = ["0", "00"]

def find_outcome(player_guess, roulette_result):
    """Return the game outcome based on the player guess and dice total.

    Args:
        player_guess (str): The predicted coin flip
        roulette_result (str): The roulette result
    """
    if is_even_win(player_guess, roulette_result):
        return utils.GAME_WIN
    elif is_odd_win(player_guess, roulette_result):
        return utils.GAME_WIN
    elif is_straight_win(player_guess, roulette_result):
        return utils.GAME_WIN_ROULETTE_EXACT
    else:
        return utils.GAME_LOSS

def is_even_win(guess, roulette_result):
    """Check whether the game has an even win.

    Args:
        guess (str): The player guess
        roulette_result (str): The roulette result
    """
    if roulette_result in non_standard_numbers:
        # Ensure "0" and "00" don't get counted as even
        return False
    else:
        roulette_num = int(roulette_result) # type conversion from string
        return utils.is_even(guess) and roulette_num % 2 is 0

def is_odd_win(guess, roulette_result):
    """Check whether the game has an odd win.

    Args:
        guess (str): The player guess
        roulette_result (str): The roulette result
    """
    roulette_num = int(roulette_result) # type conversion from string
    return utils.is_odd(guess) and roulette_num % 2 is 1

def is_straight_win(guess, roulette_result):
    """Check whether the game has a 'straight up' win, where the player guesses the precise roulette wheel outcome (e.g. `"17"`)

    Args:
        guess (str): The player guess
        roulette_result (str): The roulette result
    """
    return str(guess) is roulette_result # roulette_result is a string

def print_roulette_result(roulette_result):
    print(f"The wheel landed on {roulette_result}")

def print_selected_cards(player_card, computer_card):
    print(f"Your card was {player_card}")
    print(f"Their card was {computer_card}")

def spin_wheel():
    """Return a string representing the result of a roulette wheel spin
    """
    integer = random.randint(0, 37)
    if integer is 37:
        return "00" # Using 37 to model 00
    else:
        # return a string for type consistency
        return str(integer)

