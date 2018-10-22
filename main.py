"""
File Name: Main.py
Author: zdeniz
Year: 2018
#TODO: Oyun arayüzü için metod ve/veya class oluşturulacak.
#TODO: Oyuncu ve dağıtıcı bahis ve para hesapları yapan ve bu değerleri tutan class ve/veya metodlar oluşturulacak.
"""
import cards

deck = cards.Deck()

print(deck)
deck.shuffle_deck()
print(deck)
print(cards.card_ranks['King'])
bb = cards.SetTable()
print(deck)

abc = cards.DealersHand(True)
