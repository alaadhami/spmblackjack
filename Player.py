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

    def getHandValue(self):
        aces = 0;
        value = 0;
        for c in self.hand:
            value += c.value;
            if c.face == 'a':
                aces+=1;
        while (aces > 0):
            aces -=1;
            if (value+10 <= 21):
                value += 10;
        if (value > 21):
            return 'Bust';
        if (len(self.hand) == 2 and value == 21):
            return 'Blackjack';
            #This is a special case where the player gets 21 for the initial 2 card draw
            #It pays differently than a simple win 2:1 as apposed to 1:1
        return value;

    def discardHand(self):
        del self.hand;
        self.hand = [];
        
        
        
