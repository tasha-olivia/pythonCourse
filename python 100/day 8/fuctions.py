def greet():
    print("Welcome to the python class")
    print("I am a student too just like you")
    print("I know we will help each other out along this course.  ")
print("hi")
greet()

# name is a parameter
# function with one parameter
def greet_with_name(name):
    print(f"Hello {name} ")
    print(f"How do you do {name}")

# olivia is an arguement
greet_with_name("OLivia")

# function with two parameters
# positional arguements- position of arguementdd is very important 
def salut(name, location):
    print(f"Hello {name}")
    print(f'I hear you live in {location}')
salut("olivia", "bamenda")


# keyword arguments- the order in which the arguments are passed doesnt matter
salut( location = "Buea", name = "Wilfred")