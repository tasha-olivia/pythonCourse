    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")