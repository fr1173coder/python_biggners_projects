import random

def guess_number():
    number = random.randint(1, 100)
    low = 1
    high = 100
    attempts = 0
    while True:
        guess = int(input(f'Guess a number between {low} and {high}: '))
        attempts += 1
        if guess == number:
            break
        elif guess < number:
            print("Too low")
            low = guess
        elif guess > number:
            print("Too high")
            high = guess

    return attempts
attempts = guess_number()
print(f'Congratulations! You have {attempts} attempts to guess the number.')