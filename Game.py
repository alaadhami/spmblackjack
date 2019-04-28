from Player import Player
from Deck import Deck
from Dealer import Dealer
class Game:
# Game class has attributes:


    def __init__(self, num_players, num_decks, blackjack):
        self.blackjack = blackjack; #Pay outs for getting blackjack vary by the casino, default is 2 some do 1.2
        self.num_players = num_players;
        self.deck = Deck(num_decks);
        self.players = [Player(input("Enter player name:"),1000.00)];
        self.dealer = Dealer();
        self.shoeSize = len(self.deck.cardList); #a shoe is what casinos call the card dispenser
        self.num_decks = num_decks;

    def setup(self):
        if self.num_players == 2:
            self.players.append(Player(input("Enter player name:"),1000.00));
            
        #Bet phase
    def betPhase(self):
        for p in self.players:
            p.bet = float(input(p.name+' bet:'));
            
        #Draw phase
    def drawPhase(self):
        self.dealer.hit(self.deck);
        print('Dealer:');
        self.dealer.printHand();
        for p in self.players:
            p.hit(self.deck);
            p.hit(self.deck);
            print(p.name,':');
            p.printHand();
            
        #Play phase
    def playerPlayPhase(self):
        for p in self.players:
            if p.getHandValue() != 'Blackjack':
                in_play = True;
                double = True;
                while in_play:
                    print(p.name,':');
                    play = input("'hit','stand','surrender','split','double'?:");
                    if (play == 'stand'):
                        in_play = False;
                    elif (play == 'hit'):
                        double = False;
                        p.hit(self.deck);
                        p.printHand();
                        v = p.getHandValue();
                        if v == 'Bust' or v == 21:
                            in_play = False;
                    elif (play == 'double' and double):
                        p.bet = p.bet*2;
                        p.hit(self.deck);
                        p.printHand();
                        in_play = False;
                    elif (play == 'surrender' and double):
                        p.balance -= p.bet/2;
                        p.bet = 0;

        #Dealer play phase
    def dealerPlayPhase(self):
        in_play = self.dealer.playoutTick(self.deck);
        while(in_play):
            in_play = self.dealer.playoutTick(self.deck);
        print('Dealer Hand:');
        self.dealer.printHand();
        
        #Payout phase
    def payoutPhase(self):
        dValue, soft = self.dealer.getHandValue();
        self.dealer.discardHand();
        for p in self.players:
            pValue = p.getHandValue();
            p.discardHand();
            if pValue == 'Bust':
                p.balance -= p.bet;
                print(p.name, 'Lose.');
            elif dValue == 'Bust':#dealer bust
                p.balance += p.bet;
                print(p.name, 'Win.');
            elif pValue == 'Blackjack' and dValue != 'Blackjack':#player bj dealer no bj
                p.balance += p.bet*self.blackjack;
                print(p.name, 'BlackJack.');
            elif dValue == 'Blackjack' and pValue != 'Blackjack':
                p.balance -= p.bet;
                print(p.name, 'Lose.');
            elif pValue == dValue:
                print(p.name, 'Push.');
            elif pValue > dValue:
                p.balance += p.bet;
                print(p.name, 'Win.');
            else:
                p.balance -= p.bet;
                print(p.name, 'Lose.');
            print(p.name, 'Balance:', p.balance);

    def replay(self):
        if len(self.deck.cardList) < self.shoeSize/3:
            del self.deck;
            self.deck = Deck(self.num_decks);
            print('Refreshing Deck');
        self.betPhase();
        self.drawPhase();
        self.playerPlayPhase();
        self.dealerPlayPhase();
        self.payoutPhase();
                
            


                
            
            
