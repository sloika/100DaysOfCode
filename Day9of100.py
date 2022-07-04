# Day 9 is about using dictionary. This is a simple demonstration using secret bidding mechanics.

from os import system


def add_if_key_not_exist(dict_obj, new_key_value):
    """ Add new key-value pair to dictionary only if
    key does not exist in dictionary. """
    key, value = new_key_value.split(" ")
    if key not in dict_obj:
        print("Bidder has been successfully added")
        print(f"Name: {key.title()}")
        print(f"Bid: ${value}")
        dict_obj.update({key: value})
    else:
        print("Bidder exist, you cannot cast more than one bid for the current round.")


def secret_auction():
    is_all = False
    d = {}
    print("Welcome to the secret auction code. Please bid accordingly. Tiebreaker is for the earlier bidder")
    while not is_all:
        new_bidder = input("Enter your name and bid separated by a space: \n")
        add_if_key_not_exist(d, new_bidder)
        # print(d)
        another_bidder = input("Is there more people bidding? Type 'yes' or 'no' \n").lower()
        system("clear")

        if another_bidder == "no":
            is_all = True

    winner = max(d, key=d.get)
    print(f"Congrats to : {winner.title()} for having the highest bid.")

    return winner


secret_auction()
