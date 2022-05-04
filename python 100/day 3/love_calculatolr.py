print("Welcome to the love calculator!")
name1 = input("Enter your name. \n")
name2 = input("Enter his/her name. \n")

# concartenate stings
# combine_name = name1 + name2
# combined_string = combine_name.lower()

name1 = name1.lower() 
name2 = name2.lower()

count1 = name1.count("l")
count2 = name2.count("l")
countl = count1 + count2

count3 = name1.count("o")
count4 = name2.count("o")
counto = count3 + count4

count5 = name1.count("v")
count6 = name2.count("v")
countv = count4 + count6

count7 = name1.count("e")
count8 = name2.count("e")
counte = count7 + count8

cont1 = name1.count("t")
cont2 = name2.count("t")
contt = cont1 + cont2

cont3 = name1.count("r")
cont4 = name2.count("r")
contr = cont3 + cont4

cont5 = name1.count("u")
cont6 = name2.count("u")
contu = cont5 + cont6

cont7 = name1.count("e")
cont8 = name2.count("e")
conte = cont7 + cont8

love_sum  = countl + counto + countv + counte
true_sum = contt + contr + contu + conte 

love_percent = int(str(true_sum)  + str(love_sum))

print(f"T occured {contt} times")
print(f"R occured {contr} times")
print(f"U occured {contu} times")
print(f"E occured {conte} times")
print(" ")

print(f"L occured {countl} times")
print(f"O occured {counto} times")
print(f"V occured {countv} times")
print(f"E occured {counte} times")



print(f"Your love percent is {love_percent}% ")

if love_percent <= 10 or love_percent >= 90:
    print(" You go together like coke and mentos")
elif love_percent >= 40 and love_percent <= 50:
    print("You are alright together.") 
 