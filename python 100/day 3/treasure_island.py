print("Welcome to the treasure island!\nYour mission is to find the treasure")
print("Choose your moves wisely ")
choice = input("You are at a cross road. Do you want to go left or right? \n").lower()

if choice == "left":
    swim_move = input('You\'ve come to a lake. There\'s an island in the middle of the lake. Would you like to "swim" or "wait" for a boat?\n' ).lower()
    print("You've arrived the house on the island. The house has threee(3) doors")

    if swim_move == "wait":
        door = input("What door do you want to go into?\n Red, Blue or Yellow \n").lower()
        
        if door == "yellow":
            print("Good job! You found the treasure")
            print("You Win")
        elif door == "red":
            print("The room is on fire")
            print("Game Over")
        elif door == "blue":
            print("The room is full of spiders")
            print("Game Over")
        else:
            print("Game Over")


    else:
        print("You got swallowed by crocodiles")
        print("Game Over") 

else:
    print("You ran into a trap.")
    print("Game Over.") 