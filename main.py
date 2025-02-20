import tkinter as tk
import random

def initialize_deck():
    return [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

def draw_card(deck):
    if not deck:
        deck.extend(initialize_deck())
        random.shuffle(deck)
    return deck.pop(random.randint(0, len(deck) - 1))

def adjust_for_aces(score, cards):
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)
    return score

def hit():
    global player_score, player_cards, deck
    new_card = draw_card(deck)
    player_cards.append(new_card)
    player_score = adjust_for_aces(sum(player_cards), player_cards)
    player_label.config(text=f"Player: {player_cards} (Score: {player_score})")
    if player_score > 21:
        result_label.config(text="You busted! Dealer wins.")
        hit_button.config(state=tk.DISABLED)
        stand_button.config(state=tk.DISABLED)

def stand():
    global dealer_score, dealer_cards, deck
    hit_button.config(state=tk.DISABLED)
    stand_button.config(state=tk.DISABLED)
    dealer_score = sum(dealer_cards)
    dealer_label.config(text=f"Dealer: {dealer_cards} (Score: {dealer_score})")
    while dealer_score < 17:
        new_card = draw_card(deck)
        dealer_cards.append(new_card)
        dealer_score = adjust_for_aces(sum(dealer_cards), dealer_cards)
        dealer_label.config(text=f"Dealer: {dealer_cards} (Score: {dealer_score})")
        root.update()
    determine_winner()

def determine_winner():
    if dealer_score > 21 or player_score > dealer_score:
        result_label.config(text="You won!")
    elif dealer_score == player_score:
        result_label.config(text="It's a tie!")
    else:
        result_label.config(text="Dealer wins!")

def reset_game():
    global player_cards, dealer_cards, player_score, dealer_score, deck
    deck = initialize_deck()
    player_cards = [draw_card(deck), draw_card(deck)]
    dealer_cards = [draw_card(deck), draw_card(deck)]
    player_score = sum(player_cards)
    dealer_score = dealer_cards[0]
    player_label.config(text=f"Player: {player_cards} (Score: {player_score})")
    dealer_label.config(text=f"Dealer: [{dealer_cards[0]}, ?] (Hidden)")
    result_label.config(text="")
    hit_button.config(state=tk.NORMAL)
    stand_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Blackjack Game")

deck = initialize_deck()
player_cards = [draw_card(deck), draw_card(deck)]
dealer_cards = [draw_card(deck), draw_card(deck)]
player_score = sum(player_cards)
dealer_score = dealer_cards[0]

player_label = tk.Label(root, text=f"Player: {player_cards} (Score: {player_score})")
dealer_label = tk.Label(root, text=f"Dealer: [{dealer_cards[0]}, ?] (Hidden)")
result_label = tk.Label(root, text="")

hit_button = tk.Button(root, text="Hit", command=hit)
stand_button = tk.Button(root, text="Stand", command=stand)
reset_button = tk.Button(root, text="Reset Game", command=reset_game)

player_label.pack()
dealer_label.pack()
result_label.pack()
hit_button.pack()
stand_button.pack()
reset_button.pack()

root.mainloop()
