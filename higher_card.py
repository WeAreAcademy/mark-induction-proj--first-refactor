import random
import utils

# main function to play coin flip
def play(bet):
    """Play a higher card game with the associated wager.

    Args:
        bet (int): The amount waged

    Returns: (int) the net winnings
    """
    if bet <= 0: return utils.handle_zero_bet()
    
    utils.print_with_divider("Let's play a game of cards!", before=True, after=False)
    player_card = pick_random_card()
    computer_card = pick_random_card()
    print_selected_cards(player_card, computer_card)
    outcome = find_outcome(player_card, computer_card)
    return utils.find_and_print_winnings(bet, outcome)

# -----------------------
# Helper functions below
# -----------------------

def find_outcome(player_value, computer_value):
    """Return the game outcome based on two numbers.
    """
    if player_value > computer_value:
        return utils.GAME_WIN
    elif player_value is computer_value:
        return utils.GAME_TIE
    else:
        return utils.GAME_LOSS

def print_selected_cards(player_card, computer_card):
    """Print the player and computer cards.
    """
    print(f"Your card was {player_card}")
    print(f"Their card was {computer_card}")

def pick_random_card():
    # Use 1 to 13 to represent Ace to King
    return random.randint(1, 13)