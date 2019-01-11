import random


class Deck():
    """
    Will be an array containing 52 cards
    """

    def __init__(self):
        pass
        self.cards = []

    def add_sorted_cards(self):
        names = ['2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['D', 'C', 'H', 'S']
        for name in names:
            for suit in suits:
                card = Card()
                card.name = name
                card.suit = suit
                if name in ['J', 'Q', 'K']:
                    card.val = 10
                elif name == 'A':
                    card.val = 11
                else:
                    card.val = int(name)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def print_cards(self):
        for i, card in enumerate(self.cards):
            print('{}: {} of {}'.format(i+1, card.name, card.suit))


class Card():
    """
    Class used to store card attributes
    """

    def __init__(self):
        self.val = None
        self.name = None
        self.suit = None


# class Dealer():
#     """

#     """

#     def __init__(self):
#         self.name = 'Dealer'


# class Player():
#     """
#     """

#     def __init__(self):
#         pass


# class Blackjack():
#     """
#     Will be an array containing 52 cards
#     Blackjack:

#     """

#     def __init__(self):
#         pass


if __name__ == '__main__':

    deck = Deck()
    deck.add_sorted_cards()
    deck.print_cards()
    deck.shuffle()
    deck.print_cards()
