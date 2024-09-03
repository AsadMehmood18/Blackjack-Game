from art import logo
from random import choice, shuffle

# Define deck and shuffle once
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(deck):
    """Returns a random card from the deck"""
    return choice(deck)


def calculate_score(hand):
    """Take a list of cards and return the score calculated from the cards"""
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    if score == 21 and len(hand) == 2:
        return 0  # Blackjack
    return score


def print_hand(hand, who="Your"):
    """Prints the hand and score"""
    score = calculate_score(hand)
    print(f"{who} cards: {hand}, current score: {score}")
    return score


def determine_winner(user_score, computer_score):
    """Determine the winner based on scores"""
    if computer_score > 21:
        print("Dealer busts, you win!")
    elif user_score > 21:
        print("You Lose!")
    elif user_score == 0:
        print("Blackjack! You win.")
    elif computer_score == 0:
        print("Opponent wins with Blackjack!")
    elif user_score > computer_score:
        print("You Win!")
    elif user_score == computer_score:
        print("It's a Draw!")
    else:
        print("Dealer wins!")


def game():
    print(logo)
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play != "y":
        return

    # Shuffle and initialize deck
    deck = cards[:]
    shuffle(deck)

    user_hand = [deal_card(deck) for _ in range(2)]
    computer_hand = [deal_card(deck) for _ in range(2)]

    while True:
        user_score = print_hand(user_hand)
        computer_score = print_hand(computer_hand[:1], "Computer's first")

        if user_score > 21:
            print("You Lose!")
            return
        if user_score == 0:
            print("Blackjack! You win.")
            return
        if computer_score == 0:
            print("Opponent wins with Blackjack!")
            return

        more = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if more == 'y':
            user_hand.append(deal_card(deck))
        elif more == 'n':
            break
        else:
            print("Invalid Entry!")

    # Computer's turn
    while computer_score < 17:
        computer_hand.append(deal_card(deck))
        computer_score = calculate_score(computer_hand)

    print_hand(user_hand, "Your final hand")
    print_hand(computer_hand, "Computer's final hand")

    determine_winner(user_score, computer_score)


while True:
    game()
    if input("Play again? Type 'y' or 'n': ").lower() != "y":
        break
