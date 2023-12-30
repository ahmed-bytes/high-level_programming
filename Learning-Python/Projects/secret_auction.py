def high(bid_dict):
    highest_bid = 0
    winner = " "
    for i in bid_dict:
        compare = bid_dict[i]
        if compare > highest_bid:
            highest_bid = compare
            winner = i
    print(f"The winner is {winner} for ${highest_bid}")


from art import auction_art

print(auction_art)

more_bidders = True
result = {}
while more_bidders == True:
    name = input("Enter bidder name: ")
    price = int(input("Enter bid price: "))
    result[name] = price

    check_more_bidders = input("Are there more bidders ('yes' or 'no'): ").lower()
    if check_more_bidders == "no":
        more_bidders = False

high(result)
