"""
This module for cards

#TODO: Kartları sırayla dağıtan metod yazılacak.
#TODO: 'Player Actions'lar için class ve/veya metod yazılacak.
"""

import random

card_ranks = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,'Six': 6, 'Seven': 7,
              'Eight': 8, 'Nine': 9, 'Ten': 10, 'Joker': 10, 'Queen': 10, 'King': 10}
card_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']


class Deck:
    """
    Deck class
    """

    def __init__(self, whole_deck=[]):
        self.whole_deck = whole_deck

        list_of_ranks = list(card_ranks)
        for i in range(4):
            this_suit = card_suits[i]
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

    def pull_from_deck(self):
        """
        Pull cards from deck
        :return: Pulled card name (str)
        """
        if len(self.whole_deck) == 0:
            print('Deck out off cards!')
            exit()

        print('A card pulled from deck')

        return self.whole_deck.pop()


class SetTable:
    """

    """
    def __init__(self, number_of_players=1):
        self.number_of_players = number_of_players
        while True:
            try:
                self.number_of_players = int(input('Please Write Player Count: '))
            except ValueError:
                print('Input must be integer!')
                continue
            else:
                if self.number_of_players > 6:
                    print('Maximum player count is 6!')
                    continue
                elif self.number_of_players < 1:
                    print('Minimum player count is 1!')
                    continue
                else:
                    print('Players Ready!')
                    break


class Hands:
    """
    Player's cards
    """
    def __int__(self):
        self.deck_in_the_hand = []

    def __str__(self):
        return self.deck_in_the_hand

    def take_the_card(self, the_card):
        self.deck_in_the_hand.append(the_card)

    def calculate_the_hand(self):
        """
        Calculates the card ranks and add all up ace functions included
        :return: value of the hand (int)
        """
        soft_hand = 0
        rank_of_hand = 0
        for i in self.deck_in_the_hand:
            card_name = i.split(' ')
            if card_name[-1] == 'Ace':
                soft_hand += 1
            else:
                rank_of_hand += card_ranks[card_name[-1]]

        if soft_hand >= 1:
            if (21 - rank_of_hand - soft_hand + 1) >= 11:
                rank_of_hand += (10 + soft_hand)
            else:
                rank_of_hand += soft_hand

        return rank_of_hand


class DealersHand(Hands):
    """
    Dealer's cards
    """
    def __init__(self, first_round=True):
        Hands.__init__(self)
        self.first_round = first_round

    def __str__(self):
        if self.first_round:
            return self.deck_in_the_hand[0] + '\nClosed card! '
        else:
            return self.deck_in_the_hand

