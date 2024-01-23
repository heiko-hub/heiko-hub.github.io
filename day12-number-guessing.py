import random

def welcome():
    print("Welcome to the Number Guessing Game!")

def set_attempts():
    HARD_ATTEMPTS = random.randint(1, 5)
    EASY_ATTEMPTS = random.randint(6, 10)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        return HARD_ATTEMPTS
    else:
        return EASY_ATTEMPTS

def set_secret():
    START, END = 1, 100
    print(f"I'm thinking of a number between {START} and {END}.")
    return random.randint(START, END)

def get_guess(user_attempts):
    print(f"You have {user_attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    return user_guess

def check_guess(user_guess, com_secret):
    if user_guess == com_secret:
        is_guess_correct = True
        com_message = f"You got it! The secret number was {com_secret}."
    elif user_guess > com_secret:
        is_guess_correct, com_message = False, "Too high."
    else:
        is_guess_correct, com_message = False, "Too low."
    return is_guess_correct, com_message

def update_progress(user_attempts, can_guess_again=True):
    user_attempts -= 1
    if user_attempts > 0:
        print("Guess again.")
    else:
        print("You've run out of guess, you lose.")
        can_guess_again = False
    return user_attempts, can_guess_again
    
def guessing_game():
    welcome()
    attempts = set_attempts()
    secret = set_secret()
    play = True
    while play:
        guess = get_guess(attempts)
        is_correct, message = check_guess(guess, secret)
        print(message)
        if is_correct:
            play = False
        else:
            attempts, play = update_progress(attempts)

guessing_game()

"""
Old Version:

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "hard":
    attempts = 5
else:
    attempts = 10
answer = random.randint(1, 100)
correct_guess = False
while not correct_guess and attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        correct_guess = True
    else:
        attempts -= 1
        if guess > answer:
            print("Too high.")
        else:
            print("Too low.")
        if attempts > 0:
            print("Guess again.")
        else:
            print("You've run out of guess, you lose.")
"""
