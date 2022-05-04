import random

number = random.randint(1, 100)
print("Welcome to the Number Guessing Game. ")
print("I am thinking of a number between 1 and 100")
print(f" fsst random number is {number} ")
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard':  ").lower()

if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

end_of_game = False

def user_guess():
    global number
    global end_of_game
    global guess
    if guess < number:
        print("Too low.")
    elif guess == number:
        print(f"You got it the answer was {guess} ")
        end_of_game = True
    else:
        print("Too high.")


while not end_of_game:
    print(f"You have {lives} left ")
    guess = int(input("Make a guess: "))
    user_guess()
    lives -= 1
    if lives == 0 and (guess != number):
        end_of_game = True
        print("You failed")
    
