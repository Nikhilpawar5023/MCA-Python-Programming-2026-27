# P21 Guessing Game
import random
secret = random.randint(1, 100)
print("Guess number between 1 to 100")
while True:
    guess = int(input("Enter your guess: "))
    if guess == secret:
        print("Correct! You guessed it")
        break
    elif guess < secret:
        print("Too Low")
    else:
        print("Too High")
