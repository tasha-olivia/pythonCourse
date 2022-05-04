import random

scissor = '''
    _ _ _ _
---'    _ _) _ _ _
         _ _ _ _ _)
        _ _ _ _ _ _)
       (_ _ )
---._ _(_ _ )

'''

paper = '''
    _ _ _ _
---'     _ _) _ _
        _ _ _ _ _)
         _ _ _ _ _)
        _ _ _ _ _)
---._ _ _ _ _ _)

'''

rock = '''
     _ _ _ _ _
----'    _ _ _)
        (_ _ _ )
        (_ _ _ _)
        (_ _ _ )
----._ _(_ _ _)

'''

player = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
computer = random.randint(0, 2)

game_list = [rock, paper, scissor]

print(f"You choose\n{game_list[player]} ")
print(f" The computer choose\n{game_list[computer]} ")

if player == 2  and computer == 1:
    print("You win")
elif player == 1 and computer == 0:
    print("You win")
elif player == 0 and computer == 2:
    print("You win")
elif player == computer:
    print("You draw")
else:
    print("You loose")