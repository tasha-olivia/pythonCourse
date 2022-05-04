# local scope

def drink_portion():
    portion_strenght = 3
    print(portion_strenght)

drink_portion()

# namespace -Anything you give a name to
# global scope
player_health = 10
def drink_portion():
    portion_strenght = 3
    print(portion_strenght)
    print(player_health)

drink_portion()

# modyfying global variable -aviod it
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside function {enemies} ")

increase_enemies()
print(f"Enemies outside function {enemies} ")

PI = 3.14159