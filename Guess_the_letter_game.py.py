#guess the letter game
import random
def set_difficulty(level):
    if level == "easy":
        return 10
    else:
        return 5
def check_answer(guess, letter, attempts):
    if guess < letter:
        print("Your guess is too low.")
        return attempts - 1
    elif guess > letter:
        print("Your guess is too high.")
        return attempts - 1
    else:
        print(f"You Won! The answer was {letter}.")
        return attempts

print("let me think of a letter between a and z")
letter = chr(random.randint(ord('a'), ord('z')))
level=input("choose a level....type easy or hard:").lower()
attempts = set_difficulty(level)
while attempts > 0:
    print(f"you have {attempts} remaining to guess the letter")
    guess_letter = input("guess the letter:").lower()
    attempts=check_answer(guess_letter, letter, attempts)
    if guess_letter == letter:
        break
    if attempts == 0:
        print(f"You've run out of attempts. The answer was {letter}.")
    else:
        print("Guess again.")
print("Thanks for playing!")
# End of the game