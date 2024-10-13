import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    max_attempts = 5
    
    print("Welcome to the 'Guess the Number' game!")
    print("I have selected a number between 1 and 10.")
    print(f"You have {max_attempts} attempts to guess the number.")
    
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ")
        
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
    
    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry! You've used all {max_attempts} attempts. The number was {number_to_guess}.")

guess_number()
