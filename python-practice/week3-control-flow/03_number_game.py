# Week 3: Mini Project - Number Guessing Game
# Run: python3 week3-control-flow/03_number_game.py

# Simple version - the secret number is 7
secret_number = 7

print("I'm thinking of a number between 1 and 10")
guess = int(input("What's your guess? "))

if guess == secret_number:
    print("Correct! You win!")
elif guess == secret_number-1 or guess == secret_number+1:
    print("Close!")
elif guess < secret_number:
    print("Too low! The answer was", secret_number)
else:
    print("Too high! The answer was", secret_number)


# TODO: Add a message if the guess is within 1 of the answer (close!)
# TODO: Give the user 3 guesses instead of 1 (we'll learn loops next week!)
