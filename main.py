#!/usr/bin/env python3
"""
The main method / driver script to demo use of the
playing_cards module
"""
import playing_cards

def main():
    """Main Method"""
    #demo_check_for()
    demo_str_vs_repr()

def demo_str_vs_repr():
    """
    Demonstrates printing of string format versus representation format
    string Form: pretty, human friendly format
    repr Form: literal Python Objects format, debug friendly
    """
    deck = playing_cards.Deck()
    alondra = playing_cards.Hand()

    deck.shuffle()
    alondra.draw(deck,7)

    print("Deck STRING FORM")
    print(str(deck))
    print()
    print("Deck REPR FORM")
    print(repr(deck))
    print()
    print("Alondra STRING FORM")
    print(str(alondra))
    print()
    print("Alondra REPR FORM")
    print(repr(alondra))


def demo_check_for():
    """Demonstrates the Hand class's check_for method"""
    deck = playing_cards.Deck()
    alondra = playing_cards.Hand()

    deck.shuffle()
    alondra.draw(deck,7)

    print("Deck:",deck)
    print("Alondra's Hand:",alondra)
    print("Has Clubs?",alondra.check_for(suit="Clubs"))
    print("Has King?",alondra.check_for(rank="King"))
    print("Has King of Clubs?",alondra.check_for(suit="Clubs",rank="King"))

if __name__ == '__main__':
    main()
