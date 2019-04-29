from Deck import Deck
class Dealer:
# Dealer class has attributes:
    def __init__(self):
        self.hand = [];
    
    def hit(self, deck):
        self.hand.append(deck.cardList.pop());

    def getHandValue(self):
        aces = 0;
        value = 0;
        soft = False;
        for c in self.hand:   #for each card in hand add up values and count aces
            value += c.value;
            if c.face == 'a':
                aces+=1;
        while (aces > 0):   #for each ace if adding 10 doesn't exceed 21 it does add 10, this gets highest value still playable
            aces -=1;
            if (value+10 <= 21):
                value += 10;
                soft = True; # soft rule: we can fall back on that ace being a 1 instead of an 11 if we draw high value cards that put us over 21
        if (value > 21):  # exceeding 21 means you lose (called busting out)
            return 'Bust', False;
        if (len(self.hand) == 2 and value == 21): 
            return 'Blackjack', False;
            #This is a special case where the player gets 21 for the initial 2 card draw
            #It pays differently than a simple win 2:1 as apposed to 1:1
        return value, soft;
    
    def printHand(self):
        for c in self.hand:
            print(c.face, "of", c.suit);
        value, soft = self.getHandValue();
        if soft:
            print ('( soft',value,')');
        else:
            print('( hard',value,')');

    def discardHand(self):
        del self.hand;
        self.hand = [];

    def playoutTick(self, deck): #This fuction should be called untill it returns False as per blackjack rules.
        #this function represents one turn for the dealer. the dealer keeps taking turns until
        value, soft = self.getHandValue();
        if value == 'Blackjack' or value == 'Bust':
            return False;
        if value < 17 or (value == 17 and soft == True): #soft 17 rule, dealer only stands on hard 17, (all aces counted as 1)
            self.hit(deck);
            return True;
        return False;
