from Deck import Deck
from Player1 import Player
from Game import Game
players = int(input("Number of Players:"))
decks = int(input("Size of Deck (# of copies):"))
bj = float(input("Blackjack Multiplyer:"))
print('-----------------------Game start-----------------------')
game = Game(players,decks,bj);
game.setup();
games = 5;
while games != 0:
    games -= 1;
    game.replay();
input();
