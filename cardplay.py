# my code for card play game



class Card():
   """ This creates a card object"""

    suit_names = ['Clubs','Diamonds','Hearts','Spades']
    rank_names = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    def __init__(self,suit=1,rank=12):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])


    def __eq__(self, other):

        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):

        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    """ This represents a deck of Cards """

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)



ace_of_spade=Card(1,3)
print(ace_of_spade)



