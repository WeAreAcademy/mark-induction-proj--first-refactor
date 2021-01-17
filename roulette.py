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

    #A standard roulette wheel has the numbers 0 through 36 as well as 00. We'll use 37 to represent 00.
    utils.print_with_divider("Let's play roulette!", before=True, after=False)
    result = spin_wheel()
    if result == 37:
        print("The wheel landed on 00")
    else:
        print("The wheel landed on " + str(result))

    #Checks to see if we guessed Even and the result was even. If the result was 0, the player shouldn't win
    if guess == "Even" and result % 2 == 0 and result != 0:
        print(str(result) + " is an even number.")
        print("You won " + str(bet)+" dollars!")
        print_divider()
        return bet

    #Checks to see if we guessed Odd and the result was odd. If the result was 37, the player shouldn't win, since that's what we are using to represent 00.
    elif guess == "Odd" and result % 2 == 1 and result != 37:
        print(str(result) + " is an odd number.")
        print("You won " + str(bet)+" dollars!")
        print_divider()
        return bet

    # If you guessed a number and the result was that number, you should win 35 times the amount they bet
    elif guess == result:
        print("You guessed " + str(guess) + " and the result was " + str(result))
        print("You won " + str(bet * 35)+" dollars!")
        print_divider()
        return bet * 35

    # If none of the above are true, you lost.
    else:
        print("You lost " + str(bet)+" dollars!")
        print_divider()
        return -bet

# -----------------------
# Helper functions below
# -----------------------

even_variants = ["even", "Even"]
odd_variants = ["odd", "Odd"]

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
    return guess in even_variants and dice_total % 2 is 0

def is_odd_win(guess, dice_total):
    """Check whether the game has an odd win.

    Args:
        guess (str): The player guess
        dice_total (int): The dice total
    """
    return guess in odd_variants and dice_total % 2 is 1

def print_dice_total(dice_total):
    print(f"The sum of the two dice is {dice_total}")

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
      return f"{integer}"

