class Card:
# Card class has attributes:
#	suit (heart,diamond,spade,clubs);
#	face (2-10, j, q, k, a)
#	value1 (1-11)
# value is derived from face
    def __init__(self, suit, face):
        self.suit = suit;
        self.face = face;
        if face == 'j' or face == 'q' or face == 'k':
                self.value = 10;
        elif face == 'a':
                self.value = 1;
        else:
                self.value = face;
