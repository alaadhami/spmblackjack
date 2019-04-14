from Card import Card

class Deck:
# Deck class has attributes:
    def __init__(self, copies):
        suit = ["hearts","diamonds","spades","clubs"];
        face = [2,3,4,5,6,7,8,9,10,'a','k','q','j'];
        d = [];
        for x in range(copies):
            for s in suit:
                for f in face:
                    d.append(Card(s,f));
        self.cardList = d;
        
    def printDeck(self):
        for c in self.cardList:
            print(c.face, "of", c.suit, "\n");
