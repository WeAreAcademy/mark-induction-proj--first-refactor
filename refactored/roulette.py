import random
import utils

# main function to play roulette
def play(guess, bet):
    """Return the net winnings (`int`) from a roulette game with the associated wager. Guesses can be either `"Odd"`, `"Even"` or a string/integer representing `"00"`, `"0"`, `"1"`, ... `"36"`
    """
    # Early return if bet is <= 0
    if bet <= 0: return utils.handle_zero_bet()

    parsed_guess = str(guess) # convert guess to string for predictability
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
    if is_even_win(player_guess, roulette_result):
        return utils.GAME_WIN
    elif is_odd_win(player_guess, roulette_result):
        return utils.GAME_WIN
    elif is_straight_win(player_guess, roulette_result):
        return utils.GAME_WIN_ROULETTE_EXACT
    else:
        return utils.GAME_LOSS

def is_even_win(guess, roulette_result):
    if roulette_result in non_standard_numbers:
        # Ensure "0" and "00" don't get counted as even
        return False
    else:
        roulette_num = int(roulette_result) # type conversion from string
        return utils.is_even(guess) and roulette_num % 2 is 0

def is_odd_win(guess, roulette_result):
    roulette_num = int(roulette_result) # type conversion from string
    return utils.is_odd(guess) and roulette_num % 2 is 1

def is_straight_win(guess, roulette_result):
    return str(guess) is roulette_result # roulette_result is a string

def print_roulette_result(roulette_result):
    print(f"The wheel landed on {roulette_result}")

def print_selected_cards(player_card, computer_card):
    print(f"Your card was {player_card}")
    print(f"Their card was {computer_card}")

def spin_wheel():
    integer = random.randint(0, 37)
    if integer is 37:
        return "00" # Using 37 to model 00
    else:
        # return a string for type consistency
        return str(integer)

