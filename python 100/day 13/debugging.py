# # describe the problem
# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print("You get it")
# my_function()

# # Reproduce the bug
# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # play computer
# year = int(input("What is your year of birth? "))
# if year >= 1980 and year < 1994:
#     print("You are millenial. ")
# elif year >= 1994:
#     print("You are a Gen Z.")

# # Fix the error
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age} ")


# # print is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("NUmber of pages: "))
# word_per_page = int(input("Number of words per page: "))
# print(f"the number of pages is {pages} ")
# print(f"The words per page is {word_per_page} ")
# total_words = pages * word_per_page
# print(total_words)

# use a debugger 
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
    
mutate([1,2,3,5,8,13])

# take a break
# ask a friend
# run your code after each step
# stack overflow