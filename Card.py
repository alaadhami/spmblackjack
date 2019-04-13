class Card:
# Card class has attributes:
#	suit (heart,diamond,spade,clubs);
#	face (2-10, j, q, k, a)
#	value1 (1-11)
#	value2 (1-11)
# Both values are derived from face
	def __init__(self, suit, face):
		self.suit = suit;
		self.face = face;
		if face == 'j' or face == 'q' or face == 'k':
			self.value1 = 10;
			self.value2 = 10;
		else if face == 'a':
			self.value1 = 1;
			self.value2 = 11;
		else:
			self.value1 = face;
			self.value2 = face;
