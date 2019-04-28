from Deck import Deck
class Player:
    def __init__(self, name, balance):
        self.name = name;
        self.balance = balance;
        self.bet = 0;
        self.hand = [];
        self.split = False;
        self.splitBet = 0;
        self.splitHand = [];


    def hit(self, deck):
        self.hand.append(deck.cardList.pop());

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
    
    def printHand(self):
        for c in self.hand:
            print(c.face, "of", c.suit);
        print('(',self.getHandValue(),')');

    def discardHand(self):
        del self.hand;
        self.hand = [];

    def hitSplit(self, deck):
        self.splitHand.append(deck.cardList.pop());

    def getSplitHandValue(self):
        aces = 0;
        value = 0;
        for c in self.splitHand:
            value += c.value;
            if c.face == 'a':
                aces+=1;
        while (aces > 0):
            aces -=1;
            if (value+10 <= 21):
                value += 10;
        if (value > 21):
            return 'Bust';
        if (len(self.splitHand) == 2 and value == 21):
            return 'Blackjack';
            #This is a special case where the player gets 21 for the initial 2 card draw
            #It pays differently than a simple win 2:1 as apposed to 1:1
        return value;
    
    def printSplitHand(self):
        for c in self.splitHand:
            print(c.face, "of", c.suit);
        print('(',self.getSplitHandValue(),')');

    def discardSplitHand(self):
        del self.splitHand;
        self.splitHand = [];
        
        
        
