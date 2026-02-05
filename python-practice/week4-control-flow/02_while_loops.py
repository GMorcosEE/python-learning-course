# Week 4: While Loops - Loop Until Condition is False
# Run: python3 week4-control-flow/02_while_loops.py

# Basic while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Same as: count = count + 1

# While loop with user input
print("\nGuess the password:")
password = ""
while password != "secret":
    password = input("Enter password: ")
    if password != "secret":
        print("Wrong! Try again.")

print("Access granted!")

# Infinite loop prevention - always have a way to exit!
# Be careful with while True - make sure you have a break statement

# TODO: Create a countdown from 10 to 1, then print "Blast off!"
# TODO: Ask the user to enter numbers until they enter 0
# TODO: Add up all the numbers they entered and print the total
