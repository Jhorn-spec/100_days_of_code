import random


# Our Blackjack House Rules

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# Hints

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.

def deal_card():
    """
    Returns a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
is_game_over = False

for _ in range(0, 2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f" Your cards: {user_cards}, current score: {user_score}")
print(f" Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 0:
    is_game_over = True
else:
    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_should_deal == "y":
        user_cards.append(deal_card())
    else:
        is_game_over = True




# Hint 10: If the game has not ended, ask the user if they want to draw another card.
# If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn
# and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play.
# The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0),
# then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21,
# then the user loses. If the computer_score is over 21, then the computer loses. If none of the above,
# then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game.
# If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
