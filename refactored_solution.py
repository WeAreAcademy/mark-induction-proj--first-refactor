import random
import coin_flip

total = 100

def higher_card(bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        print_with_divider("Your bet should be above 0.", True)
        return 0

    # Draws two cards between 1 and 10 and prints the result
    print_divider()
    print("Let's play a game of cards!")
    mine = random.randint(1, 10)
    theirs = random.randint(1, 10)
    print("Your card was " + str(mine))
    print("Their card was " + str(theirs))

    #Determines who won and returns either bet, -bet or 0 (in the case of a tie.)
    if mine > theirs:
        print("You won " + str(bet)+" dollars!")
        print_divider()
        return bet
    elif mine < theirs:
        print("You lost " + str(bet)+" dollars!")
        print_divider()
        return -bet
    else:
        print("It was a tie!")
        print_divider()
        return 0

def cho_han(guess, bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        print_divider()
        print("Your bet should be above 0.")
        print_divider()
        return 0

    print_divider()
    print("Let's play Cho-Han!")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("The sum of the two dice is " + str(total))

    if guess == "Even" and total % 2 == 0:
        print("You won " + str(bet)+" dollars!")
        print_divider()
        return bet
    elif guess == "Odd" and total % 2 == 1:
        print("You won " + str(bet)+" dollars!")
        print_divider()
        return bet
    else:
        print("You lost " + str(bet)+" dollars!")
        print_divider()
        return -bet

def roulette(guess, bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        print_divider()
        print("Your bet should be above 0.")
        print_divider()
        return 0

    #A standard roulette wheel has the numbers 0 through 36 as well as 00. We'll use 37 to represent 00.
    print_divider()
    print("Let's play roulette!")
    result = random.randint(0, 37)
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

total += coin_flip.play("Heads", 10)
total += higher_card(5)
total += cho_han("Even", 2)
total += roulette("Even", 10)
total += roulette(3, 1)
total += roulette("Odd", total)
print("Your total amount of money is " + str(total))
