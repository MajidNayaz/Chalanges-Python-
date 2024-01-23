#this program can take every bid from the particepents secretly and in the final show the winner

from replit import clear


auctions_bid = {}
higher_bid = 0
winner = ""
bedding_fnished = False
while not bedding_fnished:
    name = input("Enter your name!")
    bid = int(input("Enter your bid!"))

    auctions_bid[name] = bid

    should_continue = input("Is there any other bidder? Print 'yes' or 'no'")
    if should_continue == "yes":
        clear()
    elif should_continue == "no":
        bedding_fnished = True
    else :
        bedding_fnished = True
        print("it is an ambiguos cammand")

for bidder in auctions_bid:
    price = auctions_bid[bidder]
    if price > higher_bid:
        higher_bid = auctions_bid[bidder]
        winner = bidder

print(f"{winner} is the winner and his bid is {higher_bid}")
    

