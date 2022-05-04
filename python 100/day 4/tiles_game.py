row1 = ["✉️", "✉️", "✉️", "✉️", "✉️"]
row2 = ["✉️", "✉️", "✉️", "✉️", "✉️"]
row3 = ["✉️", "✉️", "✉️", "✉️", "✉️"]
row4 = ["✉️", "✉️", "✉️", "✉️", "✉️"]
row5 = ["✉️", "✉️", "✉️", "✉️", "✉️"]


map = [row1, row2, row3, row4,row5]
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")
print("Write a two digit number. Each digit should be less than 5. The first number will represent the column and the second will represent the row")
position = int(input("Where do you want to put the treasure\n"))

column = int(position / 10) # column = int(position[0])
row = int(position % 10)    # row = int(position[1])

map[column][row] = "X"

print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")
