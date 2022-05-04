import random

word_list = ['ardvark', 'baboon', 'camel']
# choose a random number

choosen_word = random.choice(word_list)

# testing code
print(f"psst, the solution is {choosen_word}")

# store lives
lives = 6

#  create blanks as many as are letters of the word
display = []
word_lenght = len(choosen_word)
for _ in range(word_lenght):
    display += "_"
print(display)

# 
end_of_game = False
# ask user to guess a letter
while not end_of_game:
    guess = input("Guess a letter: ").lower()


    # check if letter guess is part of the word
    for position in range(word_lenght):
        letter = choosen_word[position]
        if letter == guess: 
            display[position] = letter
        
        
    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win.")
