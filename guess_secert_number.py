# generate random numbers
import random
# creates a random 3-digit number (between 100 and 999) and converts it to a string.
secret_number = str(random.randint(100, 999))
# welcome message to the player
print("Welcome to the Guessing Game!\n")
# This loop allows the player up to 10 attempts to guess the secret number.
for attempt in range(10):
    while True:
        guess = input("Guess a 3-digit number: ").strip()
        if len(guess) == 3 and guess.isdigit():
            break
        print("Invalid input. Please enter a 3-digit number.")
    
    if guess == secret_number:
        print("👌👌👌 Correct! You've guessed the secret number!")
        break
    
    secret_digits = list(secret_number)
    guess_digits = list(guess)
    feedback = []
    secret_used = [False] * 3
    guess_used = [False] * 3
    
    # Check for Correct digits
    for i in range(3):
        if secret_digits[i] == guess_digits[i]:
            feedback.append("👌")
            secret_used[i] = True
            guess_used[i] = True
        else:
            feedback.append("")
    
    # Check for Ok digits
    for i in range(3):
        if not guess_used[i]:
            for j in range(3):
                if not secret_used[j] and guess_digits[i] == secret_digits[j]:
                    feedback[i] = "👍"
                    secret_used[j] = True
                    guess_used[i] = True
                    break
    
    # Remaining digits are Wrong
    for i in range(3):
        if feedback[i] == "":
            feedback[i] = "❌"
    
    print("".join(feedback))
else:
    print(f"\nGame over! The secret number was {secret_number}.")