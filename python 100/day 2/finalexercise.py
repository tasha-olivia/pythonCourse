# tip calculator
print("Welcome to the tip calculator!")
bill = input("What was your total bill? $")
tip = input("What percent tip would you give? 10, 12 and 15? ")
people = input("How many people to split the bill? ")

rtip = int(tip)
rbill =float (bill)
rpeople = int(people)


percent_tip = rtip / 100
sum_tip = percent_tip + 1

split = rbill * sum_tip / rpeople
finalAmount = round(split, 2)

print(f"each person should pay ${finalAmount} ")