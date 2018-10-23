"""
This module for cards

#TODO: Kartları sırayla dağıtan metod yazılacak.                                        %0
#TODO: 'Player Actions'lar için class ve/veya metod yazılacak.                          %70
#TODO: Oyuncu ve dağıtıcı para hesapları yapan class ve/veya metodlar oluşturulacak.    %80
"""

import random

card_ranks = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
              'Eight': 8, 'Nine': 9, 'Ten': 10, 'Joker': 10, 'Queen': 10, 'King': 10}
card_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
action_dict = {1: 'Stays', 2: 'Hits', 3: 'Makes Insurance', 4: 'Splits', 5: 'Double Downs'}


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


class Hands:
    """
    Player's cards
    """
    def __int__(self):
        self.deck_in_the_hand = []

    def __str__(self):
        return self.deck_in_the_hand

    def take_the_card(self, the_card):
        """
        Adds the_card in your hand
        :param the_card: (str) the card you want to add in your hand
        :return: void
        """
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
            self.first_round = False
            return self.deck_in_the_hand[0] + '\nClosed card! '

        else:
            return self.deck_in_the_hand


class Money:
    """
    money class
    """
    def __init__(self, start_money='5000', player_name=' '):
        self.total_money = start_money
        self.money_on_the_desk = 0
        self.player_name = player_name

    def money_math_sub(self, sub):
        """

        :param sub:
        :return: (Bool) If player has enough money,
        drops sub from players money and returns "True"
        else returns "False"
        """
        if self.total_money - sub < 0:
            print('Insufficient fund!')
            return False
        else:
            self.total_money -= sub
            return True

    def put_money(self):
        """

        :return: void
        """
        while True:
            try:
                amount = int(input('Write bet amount'))
            except ValueError:
                print('Wrong input!')
                continue
            else:
                if amount < 25:
                    print('Minimum bet amount is 25!')
                    continue
                elif amount > 2500:
                    print('Maximum bet amount is 2500!')
                    continue
                elif Money.money_math_sub(self, amount):
                    print(self.player_name + f' Puts {amount}')
                    self.money_on_the_desk += amount
                    break

    def win_hand(self):
        """

        :return: (int) The money left to desk
        """
        self.total_money += self.money_on_the_desk * 2
        print(self.player_name + f', wins hand {self.money_on_the_desk}')
        dealer = -1 * self.money_on_the_desk
        self.money_on_the_desk = 0
        return dealer

    def win_blackjack(self):
        """

        :return: (int) The money left to desk
        """
        self.total_money += self.money_on_the_desk * 2.5
        print(self.player_name + f', wins Blackjack {self.money_on_the_desk}')
        dealer = -1.5 * self.money_on_the_desk
        self.money_on_the_desk = 0
        return dealer

    def win_insurance(self):
        """

        :return: (int) The money left to desk
        """
        self.total_money += self.money_on_the_desk
        print(self.player_name + f', win insurance {self.money_on_the_desk}')
        self.money_on_the_desk = 0
        return 0

    def refund_money(self):
        """

        :return: (int) The money left to desk
        """
        self.total_money += self.money_on_the_desk
        print(self.player_name + f', refunds back {self.money_on_the_desk}')
        self.money_on_the_desk = 0
        return 0


class Player:
    """
    player class
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

    def turn_and_actions(self, player_x):
        """
        Takes players number who is going to make move.
        :param: (str) Players name
        :return: (int) That players decision 'look for action_dict'
        """
        print(f'Player {player_x}\'s Turn!')
        print('For "Stand"          press 1')
        print('For "Hit"            press 2')
        print('For "Insurance"      press 3')
        print('For "Split"          press 4')
        print('For "Double Down"    press 5')

        while True:
            try:
                action = int(input('\tAnd press enter:'))
            except ValueError:
                print('Wrong input!')
                continue
            else:
                if 0 < action < 6:
                    print(f'Player {player_x} {action_dict[action]}!')
                    break
                else:
                    print('Wrong input!\n\tTry Again.')
                    continue

        return action
