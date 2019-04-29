from Card import Card
import random

class Deck:
# Deck class has attributes:
    def __init__(self, copies):
        suit = ["Hearts","Diamonds","Spades","Clubs"];
        face = [2,3,4,5,6,7,8,9,10,'A','K','Q','J'];
        cl = [];
        for x in range(copies):
            for s in suit:
                for f in face:
                    cl.append(Card(s,f));
        random.shuffle(cl);
        random.shuffle(cl);
        random.shuffle(cl);
        self.cardList = cl;
        
    def printDeck(self):
        for c in self.cardList:
            print(c.face, "of", c.suit, "\n");
