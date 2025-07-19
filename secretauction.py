import os

auction = {}

ascii_art = '''
 __   ___  __   __   ___ ___     __     __   __          __  
/__` |__  /  ` |__) |__   |     |__) | |  \ |  \ | |\ | / _` 
.__/ |___ \__, |  \ |___  |     |__) | |__/ |__/ | | \| \__> 

'''


def procedure(bidder, bid):
    auction[bidder] = bid


def highest_bid(auction_dict):
    highest_bid_value = 0
    highest_bidder = ''

    for bidder in auction_dict:
        bid_value = auction_dict[bidder]
        if bid_value > highest_bid_value:
            highest_bid_value = bid_value
            highest_bidder = bidder

    print(f"Highest bidder: {highest_bidder} \nBid: ${highest_bid_value}")


print(ascii_art)

bidder_check = True

while bidder_check:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))

    procedure(name, price)

    bidder_check = input("Are there anyone to bid? Yes or No: ").strip().lower()

    if bidder_check in ["no", "n"]:
        bidder_check = False
    elif bidder_check in ["yes", "y"]:
        bidder_check = True
        os.system("cls")  # or "clear" if on Mac/Linux
        print(ascii_art)
    else:
        print("Sorry, you can't proceed.")

highest_bid(auction)
