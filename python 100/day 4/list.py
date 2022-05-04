regions_in_cameroon = [ "NW", "SW", "north", "far_north"]

print(regions_in_cameroon[0])

# starts printing items from the end of the list
print(regions_in_cameroon[-1])

# change an item at a particular index
regions_in_cameroon[1] = "South_West"

# Add item to the end of the list
regions_in_cameroon.append("Litoral")

# print entire list
print(regions_in_cameroon)


fruits = ['strawberry', 'nectarines', 'apples', 'grapes', 'peaches', 'cherries', 'pears', ]
vegetables = ['spinach', 'kale','tomatoes', 'celery', 'potatoes']
dirty_dozen = [fruits, vegetables]

dirty_dozen[1][0] = "mango" 

print(f"{fruits}\n {vegetables}")
