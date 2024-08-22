import pytest
import random


def get_suit(n):
    suit = ""
    if n==1:
       suit = "Heart"
    elif n==2:
        suit = "Diamond"
    elif n==3:
        suit = "Spade"
    elif n==4:
        suit = "Club"
    return suit

def create_deck():
    deck=[]
    for c in range(1,14):
        for s in range(1,5):
            if c==1:
                deck.append("A " + str(get_suit(s)))
            elif c==11:
                deck.append("J " + str(get_suit(s)))
            elif c==12:
                deck.append("Q " + str(get_suit(s)))
            elif c==13:
                deck.append("K " + str(get_suit(s)))
            else:
                deck.append(str(c) + " " + str(get_suit(s)))
    return deck

if __name__ == '__main__':
    print("Hello from PyTest...")
    assert func(3) == 3

    deck = []
    #for d in range(0, 1):

    print("New Deck...")
    new_deck = create_deck()
    deck.append(new_deck)

    for d in range(0,len(deck)):
        print(deck[d])
    random.shuffle(deck[0])

    print("Shuffled Deck....")
    print(str(deck[0]))
