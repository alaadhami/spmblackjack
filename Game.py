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
        print('Dealer Hand:');
        self.dealer.printHand();
        for p in self.players:
            p.hit(self.deck);
            p.hit(self.deck);
            
        #Play phase
    def playerPlayPhase(self):
        for p in self.players:
            if p.hand[0].value == p.hand[1].value:
                split = True;
            
            if p.getHandValue() != 'Blackjack': #players don't play if they get blackjack, they just win, unless dealer gets blackjack too
                in_play = True; #can player still make moves
                first = True;   #is this the players first move
                while in_play:
                    print(p.name,'hand:');
                    p.printHand();
                    if split and not(p.split): #can the players cards be split
                        print ("can 'split'");
                    play = input("'hit','stand','surrender','double'?:");
                    if (play == 'stand'): #players turns are over when they stand
                        in_play = False;
                    elif (play == 'hit'): #player choosed to add cards, check if they busted (>21) or reached 21, can no longer play if they did
                        first = False;
                        p.hit(self.deck);
                        v = p.getHandValue();
                        if v == 'Bust' or v == 21:
                            in_play = False;
                    elif (play == 'double' and first): #player can double their bet on their first move and get delt one card, then their turn is over, no more hitting, you get one 1 card only
                        p.bet = p.bet*2;
                        p.hit(self.deck);
                        p.printHand();
                        in_play = False;
                    elif (play == 'surrender' and first): #player can get half their bet back if they don't like their odds, their turns are over after this, like cutting your loses.
                        p.balance -= p.bet/2;
                        p.bet = 0;
                        in_play = False;
                    elif (play == 'split' and split and not(p.split)): #if split is true (determined on ln 38 of Game.py) both cards have same value, can turn them into two hands.
                        p.split = True; #player attribute set to true to indicate player is playing two hands.
                        p.splitHand.append(p.hand.pop());# pop a card from first hand to the second
                        p.splitBet = p.bet;# second hand has an additional and equal bet to the first bet
                        #
            else:
                print(p.name,'hand:');
                p.printHand();
            
                        
        for p in self.players:#if any player is has a split hand we play it out here with the same rules as before but with no further splitting
            if p.split:
                in_play = True;
                first = True;
                while in_play:
                    print(p.name,' second hand:');
                    p.printSplitHand();
                    play = input("'hit','stand','surrender','double'?:");
                    if (play == 'stand'):
                        in_play = False;
                    elif (play == 'hit'):
                        first = False;
                        p.hitSplit(self.deck);
                        p.printSplitHand();
                        v = p.getSplitHandValue();
                        if v == 'Bust' or v == 21:
                            in_play = False;
                    elif (play == 'double' and first):
                        p.splitBet = p.splitBet*2;
                        p.hitSplit(self.deck);
                        p.printSplitHand();
                        in_play = False;
                    elif (play == 'surrender' and first):
                        p.balance -= p.splitBet/2;
                        p.splitBet = 0;
                        in_play = False;

        #Dealer play phase
    def dealerPlayPhase(self):
        in_play = self.dealer.playoutTick(self.deck); #dealer always takes 1 turn, function returns true if the rules say they need to take more
        while(in_play):#keep playing untill the rules say the dealer stops, dealer has higher than 16 and it's not soft 17 or they busted out.
            in_play = self.dealer.playoutTick(self.deck);
        print('Dealer Hand:');
        self.dealer.printHand();
        
        #Payout phase
    def payoutPhase(self):
        dValue, soft = self.dealer.getHandValue();
        self.dealer.discardHand();                  #gets value of dealers hand
        for p in self.players:
            pValue = p.getHandValue();  #for each player get the value of their hand
            p.discardHand();
            if pValue == 'Bust':    #if player busts player loses, subtract bet from player balance
                p.balance -= p.bet;
                print(p.name, 'Lose.');
            elif dValue == 'Bust':  #if dealer bust and player did not, player wins, add bet to player balance
                p.balance += p.bet;
                print(p.name, 'Win.');
            elif pValue == 'Blackjack' and dValue != 'Blackjack': #player got blackjack dealer did not, add bet * blackjack bonus value to player balance
                p.balance += p.bet*self.blackjack;
                print(p.name, 'BlackJack.');
            elif dValue == 'Blackjack' and pValue != 'Blackjack': #dealer got blackjack player didn't, normal player lose, subtract bet from balance
                p.balance -= p.bet;
                print(p.name, 'Lose.');
            elif pValue == dValue:                      #player and dealer tie, player loses nothing
                print(p.name, 'Push.');
            elif pValue > dValue:                       #player wins by having higher value than dealer, add bet to balance
                p.balance += p.bet;
                print(p.name, 'Win.');
            else:                                       #process of elimination, the dealer has the higher value, player lost, subtract bet from balance
                p.balance -= p.bet;
                print(p.name, 'Lose.');
                
        for p in self.players:                  #same thing again for split hands
            if p.split:
                p.split = False;
                pValue = p.getSplitHandValue();
                p.discardSplitHand();
                if pValue == 'Bust':
                    p.balance -= p.splitBet;
                    print(p.name, 'Lose.');
                elif dValue == 'Bust':#dealer bust
                    p.balance += p.splitBet;
                    print(p.name, 'Win.');
                elif pValue == 'Blackjack' and dValue != 'Blackjack':#player bj dealer no bj
                    p.balance += p.splitBet*self.blackjack;
                    print(p.name, 'BlackJack.');
                elif dValue == 'Blackjack' and pValue != 'Blackjack':
                    p.balance -= p.splitBet;
                    print(p.name, 'Lose.');
                elif pValue == dValue:
                    print(p.name, 'Push.');
                elif pValue > dValue:
                    p.balance += p.splitBet;
                    print(p.name, 'Win.');
                else:
                    p.balance -= p.splitBet;
                    print(p.name, 'Lose.');
                
        for p in self.players:
            print(p.name, 'Balance:', p.balance);

    def replay(self):                                       #replay all phases of game. skip setup. if 2/3rds of deck has been played, refresh deck
        if len(self.deck.cardList) < self.shoeSize/3:       #actually don't know if this is a rule but deck is never suposed to run out of cards
            del self.deck;
            self.deck = Deck(self.num_decks);
            print('Refreshing Deck');
        self.betPhase();
        self.drawPhase();
        self.playerPlayPhase();
        self.dealerPlayPhase();
        self.payoutPhase();
                
            


                
            
            
