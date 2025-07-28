import random

def guess_number():
    low = 1
    high = 100
    attempts = 0
    while True:
        guess = random.choice(range(low, high))
        attempts += 1
        answer = input(f'computer guessed {guess}, is it correct, low or high (c / l / h)? :').lower()
        if answer == 'c':
            break
        elif answer == 'l':
            low = guess
        elif answer == 'h':
            high = guess
    return attempts

attempts = guess_number()
print(f'Congratulations! You have guessed it at {attempts} attempts.')