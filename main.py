#!/usr/bin/env python3
"""
The main method / driver script to demo use of the
playing_cards module
"""
import playing_cards

def main():
    """Main Method"""
    demo_go_fish()
    #demo_str_vs_repr()
    #demo_check_for()

def demo_go_fish():
    """Demo of Go Fish Mechanics"""
    deck = playing_cards.Deck()
    alondra = playing_cards.Hand()
    benny = playing_cards.Hand()

    deck.shuffle()
    alondra.draw(deck, 14)
    benny.draw(deck, 14)

    # Benny gives Alondra all their 2's
    benny.give_to(alondra,rank=2)

    # Benny gives Alondra all their club's
    benny.give_to(alondra,suit="CLUBS")

    print("A:",alondra)
    print("B:",benny)

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
