"""
This module for cards
"""
import random


class Deck:
    """
    Deck class
    """
    card_ranks = {'Ace': [1, 11], 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
                  'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
                  'Joker': 10, 'Queen': 10, 'King': 10}
    card_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self, whole_deck=[]):
        self.whole_deck = whole_deck

        list_of_ranks = list(Deck.card_ranks)
        for i in range(4):
            this_suit = Deck.card_suits[i]
            for j in range(13):
                self.whole_deck.append(this_suit + ' of ' + list_of_ranks[j])

    def __str__(self):
        return str(self.whole_deck)

    def shuffle_deck(self):
        """
        Shuffles deck randomly
        :return: void
        """
        random.shuffle(self.whole_deck)

    def pull_from_dec(self):
        """
        Pull cards from deck
        :return: Pulled card name (str)
        """
        if len(self.whole_deck) == 0:
            print('Deck out off cards!')
            exit()

        print('A card pulled from deck')

        return self.whole_deck.pop()

    def put_cart_to_the_table(self, put_to_where):

        return put_to_where.append(self.pull_from_dec())


class SetTable:
    """

    """
    def __init__(self, number_of_players=1):
        self.number_of_players = number_of_players
        while True:
            try:
                self.number_of_players = int(input('Please Write Player Count'))
            except ValueError:
                print('input must be integer')
                continue
            else:
                print('Players Ready!')
                break

    def distribute_cards(self, deck):
        for i in range(self.number_of_players):
            deck.put_cart_to_the_table('player ' + str(i) + '\'s cards')

        deck.put_cart_to_the_table('Dealer \'s cards')

