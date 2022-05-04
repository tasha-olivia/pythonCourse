programming_dictionary = {
    "Bugs": "An error in a program that prevents the program from running as expected",
    "Functions": "A piece of code that you can easily call over and over and over again",
    "Loop": "The action of doing something over and over again",
}
# to print/access whats in the dictionary using its key
# print(programming_dictionary["Bugs"])

# add entry to the dictionary
programming_dictionary["number"] = "Any imaginary figure that indicates quantity "
# print(programming_dictionary)

# create empty dictionary
empty_dictionary = {}
# wipe an existing dictionary
# programming_dictionary = {}

# edit an item in a dictionary
programming_dictionary["Bugs"] = "A moth in your computer"
# print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
# nesting list in dictionary
travel_logs = {
    "France":{"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 5}, # nested dictionary
    "Germany": ["Berlin", "Hamburg", "Stuttgart"], 
}
# nesting dictionary in list 
travel_log = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 5
    },
    {
      "Country": "Germany",
      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
      "total_visits": 5
    }
]


# for number in range(0,2):
number = 0
experiment = travel_log[number]
for key in experiment:
    print(key)
    print(experiment[key])
    print(travel_log["cities_visited"] )
    