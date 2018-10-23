"""
File Name: Main.py
Author: zdeniz
Year: 2018
#TODO: Oyun arayüzü için metod ve/veya class oluşturulacak.                             %0
"""
import cards

deck = cards.Deck()

print(deck)
deck.shuffle_deck()
print(deck)
print(cards.card_ranks['King'])
bb = cards.Player()
print(deck)

abc = cards.DealersHand(True)
