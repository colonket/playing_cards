#!/usr/bin/env python3
"""
playing_cards
-------------
A module to emulate the usage of playing cards
Author: Eric Iniguez @colonket
"""
import random

class Card:
    """
    A playing card
    """
    def __init__(self,suit,rank):
        self.suit = str(suit).upper()
        self.rank = str(rank).upper()

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.suit}','{self.rank}')"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return (self.suit, self.rank) == (other.suit, other.rank)
        else:
            return False

class Deck:
    """
    A deck of 52 playing cards
    """
    def __init__(self,cards=None):
        self.suits = ["Spades","Diamonds","Hearts","Clubs"] 
        self.ranks = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
        if cards:
            self.cards = cards
        else:
            self.cards = [ Card(s,r) for s in self.suits for r in self.ranks ]

    def __str__(self):
        return f"\N{package} {len(self.cards)} cards, "+str([ f"{card.rank} of {card.suit}" for card in self.cards ])

    def __repr__(self):
        return f"Deck({self.cards})"

    def shuffle(self, times=1):
        """
        Randomizes the order of the playing cards in the deck
        """
        for _ in range(times):
            random.shuffle(self.cards)

    def deal(self, num):
        """
        Pops playing cards out of the deck, typically used to deal cards to a hand
        """
        stack = []
        for _ in range(num):
            try:
                stack += [self.cards.pop()]
            except IndexError:
                break
        return stack

class Hand:
    """
    A hand to draw and store playing cards
    """
    def __init__(self):
        self.cards = []

    def __str__(self):
        return f"\N{raised hand} {len(self.cards)} cards, "+str([ f"{card.rank} of {card.suit}" for card in self.cards ])

    def __repr__(self):
        return f"Hand({self.cards})"

    def draw(self, deck, num=1):
        """ Draws 'num' cards from 'deck' """
        self.cards += deck.deal(num)

    def discard(self, num=1):
        """ Discards 'num' cards from hand """
        stack = []
        for _ in range(num):
            stack += [self.cards.pop()]
        return stack

    def send(self, other_hand, suit=None, rank=None):
        """ Send cards with matching suit and/or rank to 'otherHand' """

        card = Card(suit,rank)

        def get_cards(type):
            matching = []
            for c in self.cards:
                if type =='rank':
                    if card.rank == c.rank:
                        matching += self.cards.pop(self.cards.index(c))
                elif type == 'suit':
                    if card.suit == c.suit:
                        matching += self.cards.pop(self.cards.index(c))
                else:
                    print("Error, suit or rank not specified")
            return matching

        if (not suit) and (not rank):
            print("Error: No suit or rank given")
            return False

        if not suit:
            # If no suit given, check hand for cards matching 'rank'
            other_hand.cards += get_cards('rank')

        if not rank:
            # If no rank given, check hand for cards matching 'suit'
            other_hand.cards += get_cards('suit')
        
        # Rank and Suit given, send card from hand
        other_hand.cards += self.cards.pop(self.cards.index(card))

    def check_for(self, suit=None, rank=None):
        """ Return true if 'card' found in hand"""
        card = Card(suit,rank)

        if (not suit) and (not rank):
            print("Error: No suit or rank given")
            return False

        if not suit:
            # If no suit given, check hand for cards matching 'rank'
            rank_in_hand = False
            for c in self.cards:
                if card.rank == c.rank:
                    rank_in_hand = True
            return rank_in_hand

        if not rank:
            # If no rank given, check hand for cards matching 'suit'
            suit_in_hand = False
            for c in self.cards:
                if card.suit == c.suit:
                    suit_in_hand = True
            return suit_in_hand
        
        # Rank and Suit given, check hand for card
        return card in self.cards