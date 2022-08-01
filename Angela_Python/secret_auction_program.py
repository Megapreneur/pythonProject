#
# each_bid = {}
#
# bid = True
#
#
# name_of_bidder = input("What is your name? ")
# bidding_amount = float(input("How much will you like to bid? "))
#
# while bid:
#     each_bid = {name_of_bidder: bidding_amount}
#
#     ask_for_more_bidders = input("Any more person willing to bid? yes or no")
#     if ask_for_more_bidders.lower() == "yes":
#         bid = True
#     elif ask_for_more_bidders.lower() == "no":
#         bid = False
#     else:
#         print("Wrong input")
#
#
#

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner =""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ₦{highest_bid}")

while not bidding_finished:
    name = input("What is your name? ")
    price = float(input("What is your bid? ₦"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        print("Next")
