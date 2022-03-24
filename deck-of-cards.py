import random

# Python implementation of a deck of 52 cards.
# Allows for deck shuffling and drawing 1 or more cards

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Returns the card name, for example "Ace of Spades"
    def show(self):
        nameSub = {
            1:"Ace",
            11:"Jack",
            12:"Queen",
            13:"King"
        }
        if self.rank in nameSub:
            self.rank = nameSub[self.rank]
        return (f"{self.rank} of {self.suit}")

    def __repr__(self):
        return self.show()

    def __str__(self):
        return self.show()

class Deck:
    def __init__(self):
        self.cards = []

    # Creates a fresh 52 card deck
    def build(self):
        suits = ["Spades","Clubs","Hearts","Diamonds"]
        ranks = range(1,13+1)

        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s,r))

    # Print each card in the deck
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self,quantity=1):
        if quantity == 1:
            return self.cards.pop()
        else:
            return [ self.cards.pop() for i in range(quantity) ]

if __name__ == '__main__':
    # Build a deck of 52 cards
    deck = Deck()
    deck.build()

    # Shuffle the deck
    deck.shuffle()

    # Draw the top 7 cards
    print(deck.draw(7))
