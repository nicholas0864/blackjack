import time
import random

def initialize_deck():
    return [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

def draw_card(deck):
    if not deck:  # Reshuffle if deck is empty
        deck.extend(initialize_deck())
        random.shuffle(deck)
    return deck.pop(random.randint(0, len(deck) - 1))

def adjust_for_aces(score, cards):
    """ Convert Aces from 11 to 1 if needed. """
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1  # Change one Ace from 11 to 1
        score = sum(cards)
    return score

def blackjack():
    deck = initialize_deck()
    
    player_cards = [draw_card(deck), draw_card(deck)]
    dealer_cards = [draw_card(deck), draw_card(deck)]
    
    player_score = sum(player_cards)
    dealer_score = dealer_cards[0]  # Only show one dealer card at first
    
    print(f"Dealer's visible card: {dealer_score}")
    print(f"Your cards: {player_cards}, total score: {player_score}")
    
    while True:
        choice = input("Do you want to hit or stand? (hit/stand): ").strip().lower()

        if choice == "hit":
            new_card = draw_card(deck)
            player_cards.append(new_card)
            player_score = adjust_for_aces(sum(player_cards), player_cards)
            print(f"You drew {new_card}, total score: {player_score}")
            
            if player_score > 21:
                print("You busted! The dealer wins.")
                return
            elif player_score == 21:
                print("You got Blackjack!")
                break  # Move to dealer's turn

        elif choice == "stand":
            break

    print(f"The dealer's hidden card was {dealer_cards[1]}!")
    dealer_score = sum(dealer_cards)
    
    # Dealer's turn
    while dealer_score < 17:
        new_card = draw_card(deck)
        dealer_cards.append(new_card)
        dealer_score = adjust_for_aces(sum(dealer_cards), dealer_cards)
        print(f"Dealer drew {new_card}, total score: {dealer_score}")
        time.sleep(1)
    
    # Final results
    print(f"Final Scores - You: {player_score}, Dealer: {dealer_score}")
    if dealer_score > 21 or player_score > dealer_score:
        print("You won!")
    elif dealer_score == player_score:
        print("It's a tie!")
    else:
        print("The dealer won!")

if __name__ == "__main__":
    blackjack()
