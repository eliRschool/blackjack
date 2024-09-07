#this is a simple game of open-hand blackjack intended for two players: a dealer and another player
#Author: Eli Rosenkim, Last Edited: Sep 6 2024
#I consulted w3schools.com for a refresher on python syntax but otherwise all work is original
import random
import time

#declare global variables
player_1_dealer_hand = []
player_2_hand = []
player_1_dealer_points = 0
player_2_points = 0

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

#DEBUGGING print all the cards in the deck
'''
for i in range(0, 52):
    print(str(dealing_shoe[i].value), str(dealing_shoe[i].suit))
'''

#deal a random card to dealer and print dealer hand
def dealer_draw():
    player_1_dealer_hand.append(dealing_shoe.pop(random.randint(0, len(dealing_shoe)-1)))
    print("Player 1 (Dealer)'s hand is: ")
    time.sleep(1)#make it feel old
    for i in range(0, len(player_1_dealer_hand)):
        print(str(player_1_dealer_hand[i].value), "of", str(player_1_dealer_hand[i].suit))
        time.sleep(1.2)

#deal random card to player 2, print player 2 hand
def player_draw():
    player_2_hand.append(dealing_shoe.pop(random.randint(0, len(dealing_shoe)-1)))
    print("Player 2's hand is: ")
    time.sleep(1)
    for i in range(0, len(player_2_hand)):
        print(str(player_2_hand[i].value), "of", str(player_2_hand[i].suit))
        time.sleep(1.2)


#tally the amount of points in a player's hand, given a hand list as argument
def tally_points(player_hand):
    points = 0
    for i in range(0, len(player_hand)):
        if player_hand[i].value in {"Jack", "Queen", "King"}:
            points += 10
        elif player_hand[i].value == "Ace":
            points += int(input('''Would you like to count your Ace as 1 or 11 points? Please respond by typing '1' or '11' '''))
        else:
            points += int(player_hand[i].value)
    return points





#########################MAIN GAME STARTS HERE########################

#initial draw so that each player gets *two* cards at the start of the game
player_1_dealer_hand.append(dealing_shoe.pop(random.randint(0, len(dealing_shoe)-1)))
player_2_hand.append(dealing_shoe.pop(random.randint(0, len(dealing_shoe)-1)))
dealer_draw()
player_draw()

#player_1_dealer_hand.append(Card("King", 0)) #blackjack for debug
#player_1_dealer_hand.append(Card("Ace", 0)) #
#player_2_hand.append(Card("King", 0)) #blackjack for debug
#player_2_hand.append(Card("Ace", 0)) #

#tally points
print("Tallying Player 1 (Dealer) 's points...")
time.sleep(2)
player_1_dealer_points = tally_points(player_1_dealer_hand)
print("Player 1 (Dealer)'s hand is worth", str(player_1_dealer_points), "points.")
time.sleep(2)

print("Tallying Player 2's points...")
time.sleep(2)
player_2_points = tally_points(player_2_hand)
print("Player 2's hand is worth", str(player_2_points), "points.")
time.sleep(2)

#test for blackjack and busts
if player_1_dealer_points == 21:
    if player_2_points ==21:
        print("Tie! both players drew blackjack.")
        exit(1)
    else:
        print("Dealer blackjack, Player 1 (Dealer) Wins!")
        exit(1)
if player_2_points == 21:
        print("Player 2 drew blackjack. Player 2 Wins!")
        exit(1)
if int(player_2_points) > 21:
            print("Bust!, Player 2 Loses")
            exit(1)
if player_1_dealer_points > 21:
            print("Bust!, Player 1 (Dealer) Loses")
            exit(1)


#Player's Turn
while True:
    if input("Would you like to hit or stand? Please respond by typing 'hit' or 'stand'") == 'hit':
        time.sleep(1)
        player_draw()
        time.sleep(1)
        print("Tallying Player 2's points...")
        time.sleep(2)
        player_2_points = tally_points(player_2_hand)
        print("Player 2's hand is worth", str(player_2_points), "points.")
        time.sleep(2)
        if int(player_2_points) > 21:
            print("Bust!, Player 2 Loses")
            exit(1)
    else:
        break

#Dealer's Turn
while player_1_dealer_points < 17:
    dealer_draw()
    time.sleep(1)
    print("Tallying Player 1 (Dealer) 's points...")
    time.sleep(2)
    player_1_dealer_points = tally_points(player_1_dealer_hand)
    print("Player 1 (Dealer)'s hand is worth", str(player_1_dealer_points), "points.")
    time.sleep(2)
    if player_1_dealer_points > 21:
            print("Bust!, Player 1 (Dealer) Loses")
            exit(1)

#test for wins if neither player busts
if player_1_dealer_points > player_2_points:
     print("Player 1 Wins!")
     exit(1)
elif player_1_dealer_points < player_2_points:
     print("Player 2 Wins!")
else:
    print("Draw")

    


    









