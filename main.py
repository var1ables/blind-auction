from replit import clear
from art import logo
print(logo)

bids = {}
more_bids = True

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")


while more_bids == True:
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n"))
  bids[name] = bid
  accept_more = input("Are there any other bidders? yes or no\n").lower()
  clear()
  if accept_more == "no":
    more_bids = False
    highest_bidder(bids)
