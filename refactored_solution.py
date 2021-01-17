import random
import cho_han
import coin_flip
import higher_card

total = 100

def roulette(guess, bet):
    #Makes sure your bet was above 0
    

total += coin_flip.play("Heads", 10)
total += higher_card.play(5)
total += cho_han.play("Even", 2)
total += roulette("Even", 10)
total += roulette(3, 1)
total += roulette("Odd", total)
print("Your total amount of money is " + str(total))
