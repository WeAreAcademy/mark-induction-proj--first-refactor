import cho_han
import coin_flip
import higher_card
import roulette

def play_games_of_chance():
  """Play the games of chance imported from modules above.
  """
  running_total = 100
  running_total += coin_flip.play("Heads", 10)
  running_total += higher_card.play(5)
  running_total += cho_han.play("Even", 2)
  running_total += roulette.play("Even", 10)
  running_total += roulette.play(3, 1)
  print(f"Your total amount of money is {running_total}")

play_games_of_chance()