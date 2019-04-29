import random

class cards:

    numbersRep = {'2' : 2,
                  '3' : 3,
                  '4' : 4,
                  '5' : 5,
                  '6' : 6,
                  '7' : 7,
                  '8' : 8,
                  '9' : 9,
                  '10': 10,
                  'J' : 10,
                  'Q' : 10,
                  'K' : 10,
                  'A' : 11}

    def __init__(self):
        self.deck = []
        self.suits = ['Diamond', 'Clubs', 'Hearts', 'Spades']
        self.suits_symbols = ['♦', '♣', '♥', '♠']
        self.numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

    def generateDeck(self,copies):
        self.deck = []
        for i in range(copies)
            for i in self.numbers:
                for j in self.suits_symbols:
                    insertCard = []
                    insertCard.append(i)
                    insertCard.append(j)
                    self.deck.append(insertCard)
        return self.deck

    def shuffleDeck(self, deck):
        random.shuffle(deck)
        self.deck = deck
        return self.deck
