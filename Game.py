from Player import Player
from Deck import Deck
from Dealer import Dealer
class Game:
# Game class has attributes:


    def __init__(self, num_players, num_decks, blackjack):
        self.blackjack = blackjack; #Pay outs for getting blackjack vary by the casino, default is 2 some do 1.2
        self.num_players = num_players;
        self.deck = Deck(num_decks);
        self.players = [Player(input("Enter player name:"),1000)];
        if num_players == 2:
            self.players.append(Player(input("Enter player name:"),1000));

        #Draw phase
        #***set and print dealer hand***
        for p in self.players:
            p.hit(self.deck);
            p.hit(self.deck);
            print(p.name,':');
            p.printHand();
            
        #Play phase
        for p in self.players:
            
            if p.getHandValue() != 'Blackjack':
                in_play = True;
                while in_play:
                    print(p.name,':');
                    play = input("'hit','stand','surrender','split'?:");
                    if (play == 'stand'):
                        in_play = False;
                    elif (play == 'hit'):
                        p.hit(self.deck);
                        p.printHand();
                        v = p.getHandValue();
                        if v == 'Bust' or v == 21:
                            in_play = False;
        
            


                
            
            
