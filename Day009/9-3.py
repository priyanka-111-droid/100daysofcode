from art import logo
print(logo)
print("Welcome to the secret auction")
terminate=False
auction={}
def max_bidding(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while not terminate:
    name=input("Enter your name :")
    bid_price=float(input("Enter your bid price :"))
    auction[name]=bid_price
    answer=input("Do any other people want to bid?yes or no.\n")
    if(answer=="no"):
        max_bidding(auction)
        terminate =True



