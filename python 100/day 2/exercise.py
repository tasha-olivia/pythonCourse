# sum digits of a number
a = input("Enter a two digit number: ")

b = int(a)
c = b % 10
d = b / 10
d = int(d)
# print(c)
# print(d)
sum = d + c
sum = int(sum)
print(sum) 

# teachers method
num = input("enter a two digit number")
firstDigit = num[0]
secondDigit = num[1]

sum = int(firstDigit) + int(secondDigit)
print(sum)

14 // 3 # flow division  
#  f-strings: Insted of doing type casting, use this
score = 0
height = 1.8
isWinnig = True
print(f"your score is {score}, your height is {height},you are winning is {isWinnig} ") 
