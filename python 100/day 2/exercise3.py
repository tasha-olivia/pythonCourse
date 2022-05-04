#  calculate the number of days weeks and months left if you live 90years
age = input("what is your current age: ")

years = 90 - int(age)
months = years * 12
weeks = years * 52
days = years * 365
print( years)
print(f"you have {days} days, {weeks} weeks and {months} months left.")