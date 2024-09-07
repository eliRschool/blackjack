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

#DEBUGGING print all the cards in the deck
'''
for i in range(0, 52):
    print(str(dealing_shoe[i].value), str(dealing_shoe[i].suit))
'''

#declare global variables
player_1_dealer_hand = []
player_2_hand = []
game_ongoing = True

#deal a random card from the shoe to each player's hand, and print the entire contents of the hands
def draw_stage():
    player_1_dealer_hand.append(dealing_shoe.pop(random.randint(0, len(dealing_shoe))))
    player_2_hand.append(dealing_shoe.pop(random.randint(0, len(dealing_shoe))))

    print("Player 1 (Dealer)'s hand is: ")
    for i in range(0, len(player_1_dealer_hand)):
        time.sleep(1) #make it feel old
        print(str(player_1_dealer_hand[i].value), "of", str(player_1_dealer_hand[i].suit))
    print("Player 2's hand is: ")
    for i in range(0, len(player_2_hand)):
        time.sleep(1)
        print(str(player_2_hand[i].value), "of", str(player_2_hand[i].suit))


#tally the amount of points in a player's hand
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


#initial draw so that each player gets two cards at the start of the game
player_1_dealer_hand.append(dealing_shoe.pop(random.randint(0, len(dealing_shoe))))
player_2_hand.append(dealing_shoe.pop(random.randint(0, len(dealing_shoe))))

player_1_dealer_points = 0
player_2_points = 0
#this conditional loop contains the main game
while game_ongoing:
    draw_stage()
    time.sleep(3)
    print("Tallying Player 1 (Dealer) 's points...")
    time.sleep(3)
    player_1_dealer_points = print(tally_points(player_1_dealer_hand))
    print("Player 1 (Dealer)'s hand is worth", str(player_1_dealer_points), "points.")
    time.sleep(3)
    player_2_points = print(tally_points(player_2_hand))
    print("Player 2's hand is worth", str(player_1_dealer_points), "points.")
    input("debug")

    









