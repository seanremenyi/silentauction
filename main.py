import art
import os

print(art.logo)
bids = {}

while True:
    name = input("What is your name\n")
    bid = int(input("What is your bid? \n$"))
    bids[name]=bid
    next_bidder = input("Is there another bidder?\n")
    os.system('clear')
    if next_bidder != "yes":
        break

highest_bid = ["",0]
for bidders in bids:
    if bids[bidders] > highest_bid[1]:
        highest_bid = [bidders, bids[bidders]]

print(f"The highest bid goes to {highest_bid[0]} with ${highest_bid[1]}")