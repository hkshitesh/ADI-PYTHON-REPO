from collections import namedtuple
card = namedtuple('Card', ['rank', 'suit'])
class DeckOfCards:
    ranks = list(range(2, 11)) + list('JQKA')
    suits = 'clubs diamonds hearts spades'.split()
    def __init__(self):
        self._cards = [card(rank, suit) for suit in self.suits for rank in self.ranks]
    def __str__(self):
        time_to_print = [str(x.rank) + ' of ' + str(x.suit) for x in self._cards]
        return str('\n'.join(time_to_print))
    def __iter__(self):
        return iter(self._cards)
deck = DeckOfCards()
for card in deck:
    print(card)
