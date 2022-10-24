#!/usr/bin/env python3
import random

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return str((self.suit,self.rank))

class DeckOfCards:
    def __init__(self):
        self.suits = ["Spades","Diamonds","Hearts","Clubs"] 
        self.ranks = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
        self.cards = [ Card(s,r) for s in self.suits for r in self.ranks ]

    def shuffle(self, times=1):
        for _ in range(times):
            random.shuffle(self.cards)

    def deal(self, num):
        hand = []
        while num > 0:
            hand += [self.cards.pop()]
            num -= 1
        return hand

deck = DeckOfCards()
print(len(deck.cards))
deck.shuffle()
print(deck.deal(7))
print(len(deck.cards))

