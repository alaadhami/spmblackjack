import tkinter as tk
from tkinter import *
from cards import *
from gameplay import *
from player import *
import random

TITLE_FONT = ("Arial", 30, "bold")

class BlackJackUI(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.minsize(self, 400, 400)

        self.title("EngiMavs BlackJack App")
        self.geometry("800x600")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (WelcomeUIPage, MenuPage):
            page_name = F.__name__
            frame = F(self.container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomeUIPage")

    def gridContainerInit(self, *args, **kwargs):
        self.container.pack_forget()
        self.container.grid_rowconfigure(10, weight=1)
        self.container.grid_columnconfigure(10, weight=1)
        self.container.grid()

    # Show a frame for the given page name
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def closeApp(self):
        self.destroy()

    def okButton(self, controller, name, var, totalCashIn):
        self.name = str(name.get())
        self.option = str(var.get())
        getTotalCashIn = totalCashIn.get()
        param, splitTotalCashIn = getTotalCashIn.split("$", 1)
        self.userMoney = int(splitTotalCashIn.strip())
        self.gridContainerInit(controller)
        self.once = "1"
        self.showBetButtons = True
        self.showGamePlayButtons = False

        userName = self.name
        option = self.option
        self.game = gameplay()
        game = self.game

        # Add players to the game - depending on "Select Players" input
        game.addPlayer("Dealer", "D")
        self.dealer = game.playerDict["Dealer"]
        self.dealer.money = random.randrange(400, 1000, 50)

        if option == "2":
            game.addPlayer("Player2")
            self.p2 = game.playerDict["Player2"]
            self.p2.money = random.randrange(300, 500, 50)
        elif option == "3":
            game.addPlayer("Player2")
            game.addPlayer("Player3")
            self.p2 = game.playerDict["Player2"]
            self.p3 = game.playerDict["Player3"]
            self.p2.money = random.randrange(300, 500, 50)
            self.p3.money = random.randrange(300, 500, 50)

        game.addPlayer(userName, "NULL", True)
        self.user = game.playerDict[userName]
        self.user.money = controller.userMoney

        self.refrehGamePage(controller)

    def betButton(self, controller, bet):
        self.user.bet += bet
        self.refrehGamePage(controller)

    def dealButton(self, controller):
        self.showGamePlayButtons = True
        self.showBetButtons = False

        for i in controller.game.totalPlayers:
            if (i.dealer != "dealer" and i.userRight == False):
                i.bet = random.randrange(5, 200, 5)

        self.refrehGamePage(controller)

    def replayGame(self, controller):
        controller.once = "1"
        self.showBetButtons = True
        self.showGamePlayButtons = False
        self.user.bet = 0
        controller.game.totalPlayersBet = 0
        for i in controller.game.totalPlayers:
            i.winner = "NULL"

        self.refrehGamePage(controller)


    def settingsGame(self, controller):
        self.show_frame("MenuPage")

    def hitMeButton(self, controller):
        self.user.drawCard(controller.deck)
        self.refrehGamePage(controller)

    def doneButton(self, controller):
        controller.game.checkMatch(controller.deck)

        self.showCard = True
        self.showBetButtons = False
        self.showGamePlayButtons = True
        self.refrehGamePage(controller)

    def refrehGamePage(self, controller):
        page_name = MainGamePage.__name__
        frame = MainGamePage(self.container, controller)
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        controller.show_frame("MainGamePage")

    def passVal2controller(self, controller, deck, host):
        self.deck = deck
        self.host = host

class WelcomeUIPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='orange2')
        self.controller = controller
        label = tk.Label(self, text="Welcome to EngiMavs BlackJack", font=TITLE_FONT, fg='blue2')
        label.pack(side="top", fill="x", pady=30)


        button1 = tk.Button(self, text="Start Game", bg="green3", fg='snow',
                            command=lambda: controller.show_frame("MenuPage"))
        button2 = tk.Button(self, text="Quit", bg='red2', fg='snow',
                            command=lambda: controller.closeApp())
        button1.pack(ipadx=50, ipady=40)
        button2.pack(pady=30)

        button1.config(font=('copper black', 20, 'bold'))

class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='green3')
        self.controller = controller
        nameLabel = tk.Label(self, text="Enter your name", font=TITLE_FONT, fg='blue2')
        name = tk.Entry(self, bd =5)
        var1 = IntVar()

        nameLabel.pack(side="top", fill="x", pady=10)
        name.pack(ipadx=10, pady=5)

        label = tk.Label(self, text="How many players will be playing?", font=TITLE_FONT, fg='blue2')

        var = tk.StringVar()
        var.set("1") # initial value

        option = tk.OptionMenu(self, var, "1", "2", "3")

        label.pack(fill="x", pady=15)
        option.pack()

        totalCashLabel = tk.Label(self, text="Enter how much money you're\nbringing into the game:")
        totalCashIn = tk.Entry(self, bd =5)
        totalCashIn.insert(END, '$ ' + '500')

        totalCashLabel.pack()
        totalCashIn.pack()

        button = tk.Button(self, text="OK",
                           command=lambda: controller.okButton(controller, name, var, totalCashIn))
        button.pack(pady=40)

class MainGamePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='green3')
        self.controller = controller
        # 'controller.once' determines if it's the first init.
        # If it is (="1"), add players + generate card decks + draw cards,
        # or else continue with the game with existing players and cards
        if controller.once == "1":
            self.gameInit(controller)
        self.guiInit(controller)

### ====== Generate Cards, shuffle, and start game for the first init ====== ###
    def gameInit(self, controller):
        controller.once = "0"
        controller.showCard = False
        controller.user.bet = 0

        # Get a deck of cards, shuffle them!
        host = cards()
        deck = host.generateDeck()
        host.shuffleDeck(deck)

        # game.startGame makes joined players draw 2 cards to begin with, including dealer
        controller.game.startGame(deck)

        controller.passVal2controller(controller, deck, host)

### ====== GUI display settings ====== ###

    def guiInit(self, controller):
        userName = controller.name
        option = controller.option

        game = controller.game
        totalBet = abs(game.totalPlayersBet)
        deck = controller.deck

        dealer = controller.dealer
        dealerName = dealer.name
        dealerOnHand = dealer.onHand
        dealerMoney = str(dealer.money)

        user = controller.user
        userOnHand = user.onHand
        userMoney = str(user.money)

        if option == "2":
            p2 = controller.p2
            p2name = p2.name
            p2OnHand = p2.onHand
            p2Money = str(p2.money)
            p2Bet = p2.bet

        elif option == "3":
            p2 = controller.p2
            p2name = p2.name
            p2OnHand = p2.onHand
            p2Money = str(p2.money)
            p2Bet = p2.bet

            p3 = controller.p3
            p3name = p3.name
            p3OnHand = p3.onHand
            p3Money = str(p3.money)
            p3Bet = p3.bet

        # Default display - Dealer and User display
        # ===== Dealer Display ===== #
        if dealer.winner == False:
            dealerLabel = tk.Label(self, text=dealerName, font=TITLE_FONT, fg="red")
        elif dealer.winner == True:
            dealerLabel = tk.Label(self, text=dealerName, font=TITLE_FONT, fg="green")
        else:
            dealerLabel = tk.Label(self, text=dealerName, font=TITLE_FONT)

        dealerLabel.grid(row=2, column=0)

        for i in range (0, len(dealerOnHand)):
            if controller.showCard == True:
                dealerCards = tk.Label(self, text=dealerOnHand[i], bg="black", fg="white")
            else:
                dealerCards = tk.Label(self, text=dealerOnHand[i], bg="black", fg="black")
            dealerCards.grid(row=3, column=1+i, padx=(0,5), ipadx=5, ipady=15)

        dealerMoneyLabel = tk.Label(self, text="Total: $" + dealerMoney)
        dealerMoneyLabel.grid(row=3,  column=0)

        if controller.showBetButtons == False:
            if controller.dealer.winner == False:
                totalBetLabel = tk.Label(self, text="-$" + str(totalBet), fg="red")
            elif controller.dealer.winner == True:
                totalBetLabel = tk.Label(self, text="+$" + str(totalBet), fg="green")
            else:
                totalBetLabel = tk.Label(self, text="$" + str(totalBet))

            totalBetLabel.grid(row=2,  column=3, columnspan=4)

        # If user choose 2 players - add 1 more players (including himself)
        if option == "2":
            if p2.winner == False:
                p2 = tk.Label(self, text=p2name, font=TITLE_FONT, fg="red")
            elif p2.winner == True:
                p2 = tk.Label(self, text=p2name, font=TITLE_FONT, fg="green")
            else:
                p2 = tk.Label(self, text=p2name, font=TITLE_FONT)

            p2.grid(row=5, column=0)

            for i in range (0, len(p2OnHand)):
                if controller.showCard == True:
                    p2Cards = tk.Label(self, text=p2OnHand[i], bg="black", fg="white")
                else:
                    p2Cards = tk.Label(self, text=p2OnHand[i], bg="black", fg="black")
                p2Cards.grid(row=6, column=1+i, padx=(0,5), ipadx=5, ipady=15)

            p2MoneyLabel = tk.Label(self, text="Total: $" + p2Money)
            p2MoneyLabel.grid(row=6,  column=0)

            if controller.showBetButtons == False:
                if controller.p2.winner == False:
                    p2BetLabel = tk.Label(self, text="Bet: -$" + str(p2Bet), fg="red")
                elif controller.p2.winner == True:
                    p2BetLabel = tk.Label(self, text="Bet: +$" + str(p2Bet), fg="green")
                else:
                    p2BetLabel = tk.Label(self, text="Bet: $" + str(p2Bet))

                p2BetLabel.grid(row=5,  column=3, columnspan=4)

        # If user choose 3 players - add 2 more players (including himself)
        elif option == "3":
            # ===== Player 2 Display ===== #
            if p2.winner == False:
                p2 = tk.Label(self, text=p2name, font=TITLE_FONT, fg="red")
            elif p2.winner == True:
                p2 = tk.Label(self, text=p2name, font=TITLE_FONT, fg="green")
            else:
                p2 = tk.Label(self, text=p2name, font=TITLE_FONT)
            p2.grid(row=5, column=0)

            for i in range (0, len(p2OnHand)):
                if controller.showCard == True:
                    p2Cards = tk.Label(self, text=p2OnHand[i], bg="black", fg="white")
                else:
                    p2Cards = tk.Label(self, text=p2OnHand[i], bg="black", fg="black")
                p2Cards.grid(row=6, column=1+i, padx=(0,5), ipadx=5, ipady=15)

            p2MoneyLabel = tk.Label(self, text="Total: $" + p2Money)
            p2MoneyLabel.grid(row=6,  column=0)

            if controller.showBetButtons == False:
                if controller.p2.winner == False:
                    p2BetLabel = tk.Label(self, text="Bet: -$" + str(p2Bet), fg="red")
                elif controller.p2.winner == True:
                    p2BetLabel = tk.Label(self, text="Bet: +$" + str(p2Bet), fg="green")
                else:
                    p2BetLabel = tk.Label(self, text="Bet: $" + str(p2Bet))
                p2BetLabel.grid(row=5,  column=3, columnspan=4)


            # ===== Player 3 Display ===== #
            if p3.winner == False:
                p3 = tk.Label(self, text=p3name, font=TITLE_FONT, fg="red")
            elif p3.winner == True:
                p3 = tk.Label(self, text=p3name, font=TITLE_FONT, fg="green")
            else:
                p3 = tk.Label(self, text=p3name, font=TITLE_FONT)

            p3.grid(row=7, column=0)

            for i in range (0, len(p3OnHand)):
                if controller.showCard == True:
                    p3Cards = tk.Label(self, text=p3OnHand[i], bg="black", fg="white")
                else:
                    p3Cards = tk.Label(self, text=p3OnHand[i], bg="black", fg="black")
                p3Cards.grid(row=8, column=1+i, padx=(0,5), ipadx=5, ipady=15)

            p3MoneyLabel = tk.Label(self, text="Total: $" + p3Money)
            p3MoneyLabel.grid(row=8,  column=0)

            if controller.showBetButtons == False:
                if controller.p3.winner == False:
                    p3BetLabel = tk.Label(self, text="Bet: -$" + str(p3Bet), fg="red")
                elif controller.p3.winner == True:
                    p3BetLabel = tk.Label(self, text="Bet: +$" + str(p3Bet), fg="green")
                else:
                    p3BetLabel = tk.Label(self, text="Bet: $" + str(p3Bet))
                p3BetLabel.grid(row=7,  column=3, columnspan=4)

        # ===== Line ===== #

        line = tk.Label(self, text="_______________________________", font=TITLE_FONT)
        line.grid(row=19, column=0, pady=(5), columnspan=10)

        # ===== User Display ===== #
        if user.winner == False:
            userLabel = tk.Label(self, text=userName, font=TITLE_FONT, fg="red")
            userBetLabel = tk.Label(self, text="Bet: -$" + str(controller.user.bet), fg="red")
        elif user.winner == True:
            userLabel = tk.Label(self, text=userName, font=TITLE_FONT, fg="green")
            userBetLabel = tk.Label(self, text="Bet: +$" + str(controller.user.bet), fg="green")
        else:
            userLabel = tk.Label(self, text=userName, font=TITLE_FONT)
            userBetLabel = tk.Label(self, text="Bet: $" + str(controller.user.bet))

        userLabel.grid(row=20, column=0)
        userBetLabel.grid(row=20,  column=3, columnspan=4)

        for i in range (0, len(userOnHand)):
            if (controller.showGamePlayButtons == True):
                userCards = tk.Label(self, text=userOnHand[i], bg="black", fg="white")
            else:
                userCards = tk.Label(self, text=userOnHand[i], bg="black", fg="black")
            userCards.grid(row=21, column=1+i, padx=(0,5), ipadx=5, ipady=15)

        if (controller.showBetButtons == True):
            betButton5 = tk.Button(self, text="$5",
                              command=lambda: controller.betButton(controller, 5))
            betButton10 = tk.Button(self, text="$10",
                              command=lambda: controller.betButton(controller, 10))
            betButton25 = tk.Button(self, text="$25",
                              command=lambda: controller.betButton(controller, 25))
            betButton50 = tk.Button(self, text="$50",
                              command=lambda: controller.betButton(controller, 50))
            dealButton = tk.Button(self, text="Deal Cards",
                              command=lambda: controller.dealButton(controller))

            betButton5.grid(row=21, column=3, pady=(5, 0))
            betButton10.grid(row=21, column=4, pady=(5, 0))
            betButton25.grid(row=21, column=5, pady=(5,0))
            betButton50.grid(row=21, column=6, pady=(5,0))
            dealButton.grid(row=22, column=3, columnspan=4, pady=(5,0))

        userMoneyLabel = tk.Label(self, text="Total: $" + userMoney)
        userMoneyLabel.grid(row=21,  column=0)

        # ===== Buttons Display ===== #
        if (controller.showGamePlayButtons == True):
            hitMe = tk.Button(self, text="Hit Me",
                              command=lambda: controller.hitMeButton(controller))
            done = tk.Button(self, text="Stay",
                              command=lambda: controller.doneButton(controller))
            replayButton = tk.Button(self, text="Replay?",
                                command=lambda: controller.replayGame(controller))
            settingsButton = tk.Button(self, text="Settings",
                                command=lambda: controller.settingsGame(controller))
            closeButton = tk.Button(self, text="Quit",
                                command=lambda: controller.closeApp())

            hitMe.grid(row=22, column=1, pady=(25, 0))
            done.grid(row=22, column=2, pady=(25, 0))
            replayButton.grid(row=23, column=1, pady=(3,0))
            settingsButton.grid(row=23, column=2, pady=(3,0))
            closeButton.grid(row=24, column=1, columnspan=2, pady=(5,0))
            
        
if __name__ == "__main__":
    app = BlackJackUI()
    app.mainloop()
