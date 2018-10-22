from cards import Deck, SetTable

deck = Deck()


print(deck)
deck.shuffle_deck()
print(deck)
print(deck.card_ranks['King'])
bb = SetTable()
bb.distribute_cards(deck)
print(deck)

print('fkeljnfdsbjfbds')