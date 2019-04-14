class Game:
# Game class has attributes:

'''
    def __init__(self, aaa, bbb):
        self.aaa = aaa;
        self.bbb = bbb;
'''        
        
    dealerHand = deal(deck)
    playerHand = deal(deck)
        
    def score(dealerHand, playerHand):
        if total(playerHand) == 21:
            print ("The dealer has a " + str(dealerHand) + " for a total of " + str(total(dealerHand)) )
            print ("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)) )
            print ("Congratulations! You win!\n")
        elif total(dealerHand) == 21:
            print ("The dealer has a " + str(dealerHand) + " for a total of " + str(total(dealerHand)) )
            print ("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)) )		
            print "You lose.\n"
        elif total(playerHand) > 21:
            print ("The dealer has a " + str(dealerHand) + " for a total of " + str(total(dealerHand)) )
            print ("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)) )
            print "You went over 21. You lose.\n"
        elif total(dealerHand) > 21:
            print ("The dealer has a " + str(dealerHand) + " for a total of " + str(total(dealerHand)) )
            print ("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)) )			   
            print "Dealer went over 21. You win!\n"
        elif total(playerHand) < total(dealerHand):
            print ("The dealer has a " + str(dealerHand) + " for a total of " + str(total(dealerHand)) )
            print ("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)) )
            print "Dealer's score is higher than yours. You lose.\n"
        elif total(playerHand) > total(dealerHand):
            print ("The dealer has a " + str(dealerHand) + " for a total of " + str(total(dealerHand)) )
            print ("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)) )		   
            print "Congratulations. You win! Your score is higher than the dealer's.\n"	
            
            
