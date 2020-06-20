# EPIC Lab 1: Python Blackjack

#Last name,Student Number
#_________, _________
#_________, _________
#_________, _________
#_________, _________
#Please also rename this file with your last names

# START OF HELPER CODE: ------------------------------------------------------------------------------------------------------------------------

### NOTE
### The following helper code does not need to be edited. It contains some important functions we've imported from the built-in random
### and time Python libraries, and a Card class we will be using in our game.

from random import sample   # Imports JUST the sample function from the random library so that we can use it
from time import sleep      # Imports the sleep function from the time library. The input is the number of seconds to pause the program for.

# Possible values for value: 2,3,4,5,6,7,8,9,T,J,Q,K,A 
# Possible values for suit: "C" = clubs♣, "D" = diamonds♦, "H" = hearts♥, "S" = spades♠

class Card:
    def __init__(self,value,suit):
        if value == 'T':            # Check if the value is T so we can properly change the value to the number 10
            self.value = "10"
        else:
            self.value = str(value) # Convert the given value into a string, just in case we forgot to input a string for the value
        suit_dict = {'C': 1, 'D': 2, 'H': 3, 'S': 4}    # This dictionary maps a given suit to a number that we can use as a list index
        self.suit = '♣♦♥♠'[suit_dict[str(suit)]-1]      # 1,2,3,4 = ♣♦♥♠, here we are indexing the string: ♣ = index 1, ♦ = index 2, and so on

    def card_front(self):                   # This class method returns a list of strings that represents the "front" of the card, with suit and
        return[                             # the proper value. The f in front of some of the strings is a formatting character. We basically
                '┌───────┐',                # lay out some mandatory instructions for how the string should look when printed.
                "|{:<2}     |".format(self.value) , 
                '|       |',
                "|   {:^2}  |".format(self.suit) ,
                '|       |',
                "|     {:>2}|".format(self.value) ,
                '└───────┘'
                ]
    def card_back(self):                    # This returns a list of strings for the "back" of the card so we can't see what cards the dealer has
        """creates back of card as a list of strings, used mainly for dealer"""
        return[
                '┌───────┐',
                '│░░░░░░░│', 
                '│░░░░░░░│',
                '│░░░░░░░│',
                '│░░░░░░░│',
                '│░░░░░░░│',
                '└───────┘'
                ]
    def get_value(self):                            # This method lets us quickly check the numerical value of a card, according to the rules
        """Returns the card's numerical value"""    # of blackjack. This will be useful later, where we need to calculate the value of a 
        if self.value in ['T', 'J', 'Q', 'K']:      # given hand of cards.
            card_value = 10
        elif self.value == "A":                     # Note that Aces in blackjack have two possible values, so the ace is the only value to return
            card_value = [1,11]                     # a list of two values, instead of a single value. Useful later in the code.
        else:
            card_value = int(self.value)
        return card_value
### END OF HELPER CODE --------------------------------------------------------------------------------------------------------------------------

# Start of Step 1 -------------------------------------------------------------------------------------------------------------------------------        
def create_deck():
    """ Generates a full deck of 52 cards using the Card class. The deck is
    returned as a list of Card objects, and is shuffled."""
    
    suits = ["C", "D", "H", "S"]
    values = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    deck = []           # We set up an empty list for the deck. Setting up an empty list is required in order to add items to the list later
    for suit in suits:
        for value in values:
            myCard = Card(value, suit)
            deck.append(myCard)   # add the new card to the deck here using append(item)
    deck = sample(deck, 52)   # shuffle the deck we just created (you may want to read about sample command on page 2 of lab instruction)
    return deck         # return designates the output of a function. Here, we say this function should give us the list stored in deck
# End of Step 1 ---------------------------------------------------------------------------------------------------------------------------------

# Start of Step 2 -------------------------------------------------------------------------------------------------------------------------------
def start_of_game_deal(deck):
    """Used at the start of a game, deals the player and the dealer two 
    cards each"""
    dealer_hand = []
    player_hand = []
    # implement a for loop to deal two cards to both the player and the dealer
    for i in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
    return player_hand, dealer_hand
# End of Step 2 ---------------------------------------------------------------------------------------------------------------------------------

# Start of Step 3 -------------------------------------------------------------------------------------------------------------------------------
def check_hand_value(hand):
    """Checks the numerical value of the cards in the given hand. A hand is a
    list of card objects"""
    hand_value = 0
    num_aces = 0
    # Sum up all non-Ace card values first (HINT: use card.get_value() here)
    for card in hand:
        card_value = card.get_value()  # get the card's value here
        if type(card_value) == list: # Only Ace cards return a list for their value
            card_value = 0
            num_aces += 1   # set the ace card's value to 0 and add 1 to the number of aces
        hand_value += card_value # add the value of the card to the hand
        
    # Now check if the value of an Ace should be 1 or 11 in the given hand
    if num_aces == 0:          # First check if we have 0 aces, in which case we do nothing
        return hand_value
    elif (hand_value + 11) > 21: # Check if counting the first ace as 11 and all other aces as 1 puts the hand value over 21 (means all aces should be 1)
        hand_value += int(num_aces) # Add the value of the aces to the hand, in this case they all have a value of 1
        return hand_value
    else:               # The else runs if the first ace has a value of 11 and the rest of the aces have a value of 1 without going over 21
        hand_value = hand_value + 11 + (int(num_aces) - 1) # Add the value of the aces to the hand, the first ace counts as 11 and the rest are 1
        return hand_value
# End of Step 3 ---------------------------------------------------------------------------------------------------------------------------------

# Start of Step 4 -------------------------------------------------------------------------------------------------------------------------------
def show_hand_unhidden_cards(hand):
    """Prints the cards for the given hand to the shell, with no hidden cards."""
    hand_graphics_unhidden = []
    # Implement a for loop to create a list of lists of strings, containing all of the card graphics we want to print
    # HINT: A hand is a list of card objects, and you can use card.card_front() to return the list of strings used to print the card
    # for loop goes here
    for card in hand:
       hand_graphics_unhidden.append(card.card_front())              # append to the list of card graphics here
        
    # Each card has seven lines to print
    for i in range(7):
        card_str = ""           # initialize an empty string to add card graphics to
        for j in range(len(hand)):    # The second loop should run for however many cards we have in the hand
            card_str += hand_graphics_unhidden[j][i] + " " # fill in the indexes HINT: use i or j here
        print(card_str)         # prints all of the cards in the hand when complete
        
def show_hand_hidden_cards(hand):
    """Prints the cards for the given hand to the shell, with all cards except the first hidden."""
    hand_graphics_hidden = [hand[0].card_front()] # The first value in this list should be the list of strings for the front of the first card
    for i in range(1,len(hand)):                      # This loop should skip the first card in the hand but cover the rest of the cards
        hand_graphics_hidden.append(hand[i].card_back())         # Add the back of the cards to our list here
        
    # Again, each card has 7 lines to print. Implement the for loop to print the cards here. HINT: it should be extremely similar to the
    # nested for loop from the previous function.
    for i in range(7):
        card_str = ""    # initialize an empty string to add card graphics to
        for j in range(len(hand)): # The second loop should run for however many cards we have in the hand
            card_str += hand_graphics_hidden[j][i] + " " # fill in the indexes HINT: use i or j here
        print(card_str)
# End of Step 4 ---------------------------------------------------------------------------------------------------------------------------------

# Start of Step 5 -------------------------------------------------------------------------------------------------------------------------------

def hit(deck, hand):
    """Allows a player to hit and draw one more card"""
    hand.append(deck.pop())                  # Add a card from the deck to the hand here. HINT: remember pop() and append()
    return hand

def dealer_turn(deck, hand):
    dealer_stands_on = 17   # This defines the minimum value the dealer's hand must reach before it is allowed to stop drawing cards
    print("Now it's the dealer's turn! The dealer stands on %s." % dealer_stands_on )
    print("Dealer's hand:")
    show_hand_hidden_cards(hand) # On this line, show the dealer's unhidden hand using the function from step 4
    while check_hand_value(hand) < 17: # Keep looping for as long as the value of the hand is less than what the dealer stands on
        print("The dealer draws a card.")
        hand.append(deck.pop())   # add a card to the hand using the hit function above
        show_hand_hidden_cards(hand)   # Show the unhidden hand of the dealer
        sleep(5)   # Pause to allow the player to process what the dealer draws. HINT: sleep function from intro
    if check_hand_value(hand) > 21: # Check if the dealer's hand has a value over 21, which means they bust (lose)
        print("The dealer busts!")
        return 0
    else:        # Here, the dealer hit between 17 and 21 and now we can resolve the hand to see who won in the main game loop.
        print("The dealer is finished drawing cards.")
        print("Dealer's final hand:")
        show_hand_hidden_cards(hand)    # Show the unhidden hand of the dealer
        sleep(5)    # Pause for readability
        return check_hand_value(hand) # return the final value of the hand


# End of Step 5 ---------------------------------------------------------------------------------------------------------------------------------

# Start of Game Loop ----------------------------------------------------------------------------------------------------------------------------
## define the main game loop function
def game_loop():
    player_chips = 500
    print("Welcome to Python Blackjack! You start with %s chips." % (player_chips))
    print("The dealer's hand is shown first, followed by your hand.")
    while player_chips > 0:
        print("New hand!")
        print("You currently have %s chips." % player_chips)
        bet = int(input("What is your initial bet? "))
        while bet > player_chips or bet < 0:
            bet = int(input("That was an invalid bet. Make sure you aren't betting more than you have! Please enter a bet: "))
        deck = create_deck()#step 1
        player_hand, dealer_hand = start_of_game_deal(deck)#step 2
        print("Dealer's hand:")
        show_hand_hidden_cards(dealer_hand)
        print("Player's hand:")
        show_hand_unhidden_cards(player_hand)
        player_answer = "N/A"
        if check_hand_value(player_hand) == 21:
            print("You had a natural 21! Let's see what the dealer had:")
            show_hand_unhidden_cards(dealer_hand)
            sleep(2.5)
            if check_hand_value(dealer_hand) == 21:
                print("The dealer also had 21, so you tie. End of hand.")
            else:
                print("You win! Since you had a natural 21, you get your 1.5 times your bet back. Nice!")
                player_chips += int(bet*1.5)
        else: 
            player_turn = True
            while player_turn:
                print("The current value of the cards in your hand is %s. What would you like to do?"% (check_hand_value(player_hand)))
                player_answer = input("Type hit, stand, double down. Enter something else to quit the game: " )
                if player_answer == "hit":#step 5, hit function
                    player_hand = hit(deck, player_hand)
                    print("Dealer's hand:")
                    show_hand_hidden_cards(dealer_hand)
                    print("Player's hand:")
                    show_hand_unhidden_cards(player_hand)
                    if check_hand_value(player_hand) > 21:
                        player_turn = False
                elif player_answer == "double down":#step 5, hit function
                    hit(deck, player_hand)
                    print("Dealer's hand:")
                    show_hand_hidden_cards(dealer_hand)
                    print("Player's hand:")
                    show_hand_unhidden_cards(player_hand)
                    player_turn = False
                elif player_answer == "stand":
                    player_turn = False
                else:
                    print("GAME OVER")
                    print("You finished with %s chips." % player_chips)
                    player_turn = False
                    return None
            player_final_value = check_hand_value(player_hand)
            if player_final_value > 21:
                print("Dealer's final hand:")
                show_hand_unhidden_cards(dealer_hand)
                print("Player's final hand:")
                show_hand_unhidden_cards(player_hand)
                if player_answer == "double down":
                    bet = 2*bet
                    print("Oh no! You drew too many cards and busted. You lose this hand and %s chips." % bet)
                    player_chips -= bet
                else:
                    print("Oh no! You drew too many cards and busted. You lose this hand and %s chips." % bet)
                    player_chips -= bet
            else:
                dealer_final_value = dealer_turn(deck, dealer_hand)#step 5, dealer_turn
                print("Player's final hand:")
                show_hand_unhidden_cards(player_hand)
                if dealer_final_value > 21:
                    print("The dealer busted. You win this hand! You received %s chips." % bet)
                    player_chips += bet
                else:
                   if player_final_value > dealer_final_value:
                       if player_answer == "double down":
                           bet = bet*2
                           print("You won this hand! Since you doubled down, you received %s chips." % bet)
                           player_chips += bet
                       else:
                           print("You won this hand! You received %s chips." % bet)
                           player_chips += int(bet)
                   elif player_final_value == dealer_final_value:
                       print("You tied with the dealer. You don't gain or lose any chips.")
                   else:
                       if player_answer == "double down":
                           bet = bet*2
                           print("The dealer had the better hand, you lose this hand and %s chips." % bet)
                           player_chips -= bet
                       else:
                           print("The dealer had the better hand, you lose this hand and %s chips." % bet)
                           player_chips -= bet
        if player_chips <= 0:                   
            print("You ran out of chips! Game over.")
        sleep(2.5)           
# End of Game Loop ------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    game_loop()
