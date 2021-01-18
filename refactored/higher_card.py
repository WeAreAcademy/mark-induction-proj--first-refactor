import random
import utils

# main function to play higher card
def play(bet):
    """Return the net winnings (`int`) from a higher card game with the associated wager.
    """
    # Early return if bet is <= 0
    if bet <= 0: return utils.handle_zero_bet()
    
    utils.print_with_divider("Let's play a game of cards!", before=True, after=False)
    # Using destructuring to get the first two elements of a list
    player_card, computer_card, *_ = generate_shuffled_deck()
    print_selected_cards(player_card, computer_card)
    outcome = find_outcome(player_card, computer_card)
    return utils.find_and_print_winnings(bet, outcome)

# -----------------------
# Helper functions below
# -----------------------

def find_outcome(player_value, computer_value):
    if player_value > computer_value:
        return utils.GAME_WIN
    elif player_value is computer_value:
        return utils.GAME_TIE
    else:
        return utils.GAME_LOSS

def generate_deck_values():
    deck = []
    # Populate deck with values of four suits
    for n in range(4):
        deck += generate_suit_values()
    return deck

def generate_shuffled_deck():
    deck = generate_deck_values()
    random.shuffle(deck) # shuffles in-place (mutates)
    return deck

def generate_suit_values():
    # Use 1 to 13 to represent Ace to King
    return list(range(1, 13))

def print_selected_cards(player_card, computer_card):
    print(f"Your card was {player_card}")
    print(f"Their card was {computer_card}")