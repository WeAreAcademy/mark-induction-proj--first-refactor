import random
import cho_han
import coin_flip
import higher_card
import roulette

total = 100


total += coin_flip.play("Heads", 10)
total += higher_card.play(5)
total += cho_han.play("Even", 2)
total += roulette.play("Even", 10)
total += roulette.play(3, 1)
print(f"Your total amount of money is {total}")
