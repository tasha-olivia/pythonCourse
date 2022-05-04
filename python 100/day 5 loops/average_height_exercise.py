heigth = input("input a list of students heights: ").split( )
for n in range(0, len(heigth)):
    heigth[n] = int(heigth[n])
print(heigth)

# sums up all items in a list 
sum(heigth)

item = 0
sum = 0
for hei in heigth:
    item += 1
    sum += hei
    average = round(sum / item)
print(f"The list has {item} items in the list")
print(f"The sum of heights is {sum}")
print(f"The average of heights in the list is {average}")
