import random

word_list = ["ardvark", "baboon", "camel"]
# choose  a random word
chosen_word = random.choice(word_list)

lives = 6

# create a list 
display = []
word_lenght = len(chosen_word)
for _ in range(word_lenght):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #  check if user already guessed the letter
    if guess in display:
        print(f"You've already guessed {guess}")

    # check if letter chosen belongs to the word
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        # check if user made a wrong guess
        print(f"You guessed {guess}, thats not in word. You lose a live. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")


