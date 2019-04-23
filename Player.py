from Deck import Deck
class Player:
    def __init__(self, name, balance):
        self.name = name;
        self.balance = balance;
        self.hand = [];

    def hit(self, deck):
        self.hand.append(deck.cardList.pop());

    def printHand(self):
        for c in self.hand:
            print(c.face, "of", c.suit, "\n");
        
        
