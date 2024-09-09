#this is a simple game of open-hand blackjack intended for two players: a dealer and another player
#Author: Eli Rosenkim, Last Edited: Sep 6 2024
#I consulted w3schools.com for a refresher on python syntax but otherwise all work is original
import random
import time

#define a class for the cards, containing a value and a suit
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

#populate the deck of cards
dealing_shoe = [] #this a list of all cards yet to be dealt
for value_index in range(0, 13):
    values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace")
    suits = ("spades", "hearts", "clubs", "diamonds")
    for suit_index in range(0, 4):
        dealing_shoe.append(Card(values[value_index], suits[suit_index]))

#define a player class
class Player:
    def __init__(self, hand, points):
        self.hand = [] #list of cards in player's hand
        self.points = 0; #points in player's hand
    
    #draw a random card from the shoe
    def draw(self):
        self.hand.append(dealing_shoe.pop(random.randint(0, len(dealing_shoe)-1)))
        time.sleep(0.5)

    #print the contents of the player's hand
    def print_hand(self):
        for i in range(0, len(self.hand)):
            time.sleep(0.5)
            print(str(self.hand[i].value), "of", str(self.hand[i].suit))
        time.sleep(1)
    
    #tally up the points of the player's hand, and update the player's point variable
    def tally(self):
        self.points=0
        for i in range(0, len(self.hand)):
            time.sleep(0.1)
            if self.hand[i].value in {"Jack", "Queen", "King"}:
                self.points += 10
            elif self.hand[i].value == "Ace":
                self.points += int(input("Would you like to count your Ace as 1 or 11 points? Please respond by typing '1' or '11' "))
            else:
                self.points += int(self.hand[i].value)
    

#declare two players
player_1_dealer = Player([], 0)
player_2 = Player([], 0)



#########################MAIN GAME STARTS HERE########################

#initial draw so that each player gets *two* cards at the start of the game
player_1_dealer.draw()
player_1_dealer.draw()
player_2.draw()
player_2.draw()
print("Player 1 (Dealer) 's hand is :")
player_1_dealer.print_hand()
print("Player 2's hand is :")
player_2.print_hand()

#tally points
print("Tallying Player 1 (Dealer) 's points...")
player_1_dealer.tally()
time.sleep(0.5)
print("Player 1 (Dealer)'s hand is worth", str(player_1_dealer.points), "points.")
time.sleep(1)

print("Tallying Player 2's points...")
player_2.tally()
time.sleep(0.5)
print("Player 2's hand is worth", str(player_2.points), "points.")
time.sleep(1)

#test for blackjack and busts
if player_1_dealer.points == 21:
    if player_2.points ==21:
        print("Tie! both players drew blackjack.")
        exit(1)
    else:
        print("Dealer blackjack, Player 1 (Dealer) Wins!")
        exit(1)
if player_2.points == 21:
        print("Player 2 drew blackjack. Player 2 Wins!")
        exit(1)
if int(player_2.points) > 21:
            print("Bust!, Player 2 Loses")
            exit(1)
if player_1_dealer.points > 21:
            print("Bust!, Player 1 (Dealer) Loses")
            exit(1)


#Player's Turn
while True:
    if input("Would you like to hit or stand? Please respond by typing 'hit' or 'stand'") == 'hit':
        time.sleep(1)
        print("Player 2's hand is :")
        player_2.draw()
        player_2.print_hand()
        time.sleep(1)
        print("Tallying Player 2's points...")
        time.sleep(2)
        player_2.tally()
        print("Player 2's hand is worth", str(player_2.points), "points.")
        time.sleep(2)
        if int(player_2.points) > 21:
            print("Bust!, Player 2 Loses")
            exit(1)
    else:
        break

#Dealer's Turn
while player_1_dealer.points < 17:
    player_1_dealer.draw()
    print("Player 1 (Dealer) 's hand is :")
    player_1_dealer.print_hand()
    time.sleep(1)
    print("Tallying Player 1 (Dealer) 's points...")
    time.sleep(2)
    player_1_dealer.tally()
    print("Player 1 (Dealer)'s hand is worth", str(player_1_dealer.points), "points.")
    time.sleep(2)
    if player_1_dealer.points > 21:
            print("Bust!, Player 1 (Dealer) Loses")
            exit(1)

#test for wins if neither player busts
if player_1_dealer.points > player_2.points:
     print("Player 1 Wins!")
     exit(1)
elif player_1_dealer.points < player_2.points:
     print("Player 2 Wins!")
else:
    print("Draw")

    












