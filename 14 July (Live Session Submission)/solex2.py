from collections import namedtuple
card = namedtuple('Card', ['rank', 'suit'])
class DeckOfCards:
    ranks = list(range(2, 11)) + list('JQKA')
    suits = 'clubs diamonds hearts spades'.split()

    def __init__(self):
        self.cards = [card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __iter__(self):
        return iter(self.cards)
deck = DeckOfCards()
for card in deck:
    print(card)
