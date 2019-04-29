class Card:
# Card class has attributes:
#	suit (heart,diamond,spade,clubs);
#	face (2-10, j, q, k, a)
#	value1 (1-11)
# value is derived from face
    def __init__(self, suit, face):
        self.suit = suit;
        self.face = face;
        if face == 'J' or face == 'Q' or face == 'K':  #if it's a face card value is 10
                self.value = 10;
        elif face == 'A': #aces initialy set to 1, when calculating hand value will add 10 if it can (aces are 1 or 11)
                self.value = 1; 
        else:
                self.value = face;
