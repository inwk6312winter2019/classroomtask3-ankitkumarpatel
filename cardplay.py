# my code for card play game

import random
import math
import string

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

   def add_card(self, card):
       self.cards.append(card)
   
   def remove_card(self, card):
       self.cards.remove(card)

   def pop_card(self, i=-1):        
       return self.cards.pop(i)

   def shuffle(self):        
       random.shuffle(self.cards)

   def sort(self):       
       self.cards.sort()

   def move_cards(self, hand, num):
       for i in range(num):
           hand.add_card(self.pop_card())
class Hand(Deck):

    """ This represents hand of Player """
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label

def main():
    deck = Deck()
    deck.shuffle()
    hand1 = Hand()
    deck.move_cards(hand1,5)
    hand1.sort()
    print("Player 1 Cards:")
    print(hand1)
    hand2 = Hand()
    deck.move_cards(hand2,5)
    hand2.sort()
    print("\nPlayer 2 Cards:")
    print(hand2)
    hand3 = Hand()
    deck.move_cards(hand3,5)
    hand3.sort()
    print("\nPlayer 3 Cards:")
    print(hand3)
    hand4 = Hand()
    deck.move_cards(hand4,5)
    hand4.sort()
    print("\nPlayer 4 Cards:")
    print(hand4)


if __name__ == '__main__':
    main()
    
























