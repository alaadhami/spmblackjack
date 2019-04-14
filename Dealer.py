import random

class Dealer:
# Dealer class has attributes:
    hand = []
    def __init__(self, aaa, bbb):
        self.aaa = aaa;
        self.bbb = bbb;
    

    
    def deal(deck):

        for i in range(2):
            random.shuffle(deck)
            card = deck.pop()
            if card == 11:card = "J"
            if card == 12:card = "Q"
            if card == 13:card = "K"
            if card == 14:card = "A"
            hand.append(card)
            return hand



    def hit(hand):
        card = deck.pop()
        if card == 11: card = "J"
        if card == 12: card = "Q"
        if card == 13: card = "K"
        if card == 14: card = "A"
        hand.append(card)
        return hand
