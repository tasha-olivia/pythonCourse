import os
import logo
def clearconsole():
    command = 'clear'
    if os.name in ('nt','dos'):
        command ='cls'
    os.system(command)

print(logo.logo)

def find_highest_bidder (bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with  a bid of ${highest_bid} ")



bidding_finished = False
one_bid = {}
while not bidding_finished:
    name = input("Enter your name: ")
    price = int(input("How much do you want to bid: $"))
    one_bid[name] = price
    end = input("Are there any other bidders? Type 'yes' or'no' ").lower
    # clearconsole()
    if end == "no":
        bidding_finished = True
        find_highest_bidder(one_bid)
        print(end)
    elif end == "yes":
        bidding_finished = False
        clearconsole()
        print(end)

