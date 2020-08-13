import unittest

from src.card import Card
from src.card_game import CardGame


class CardGameTest(unittest.TestCase):
    def setUp(self):
        self.game = CardGame()

    def test_check_for_ace_true(self):
        expected = True
        card = Card("Hearts", 1)
        actual = self.game.checkforAce(card)
        self.assertEqual(expected, actual)

    def test_check_for_ace_false(self):
        expected = False
        card = Card("Clubs", 4)
        actual = self.game.checkforAce(card)
        self.assertEqual(expected, actual)

    def test_highest_card_is_card1(self):
        card1 = Card("Clubs", 8)
        card2 = Card("Spades", 3)
        expected = card1
        actual = self.game.highest_card(card1, card2)
        self.assertEqual(expected, actual)

    def test_highest_card_is_card_2(self):
        card1 = Card("Hearts", 4)
        card2 = Card("Diamonds", 7)
        expected = card2
        actual = self.game.highest_card(card1, card2)
        self.assertEqual(expected, actual)

    def test_highest_card__equal_card_values(self):
        card1 = Card("Hearts", 9)
        card2 = Card("Clubs", 9)
        expected = card2
        actual = self.game.highest_card(card1, card2)
        self.assertEqual(expected, actual)

    def test_cards_total(self):
        card1 = Card("Spades", 7)
        card2 = Card("Clubs", 3)
        cards = [card1, card2]
        expected = "You have a total of 10"
        actual = self.game.cards_total(cards)
        self.assertEqual(expected, actual)

    def test_cards_total_many(self):
        card1 = Card("Spades", 7)
        card2 = Card("Clubs", 3)
        card3 = Card("Hearts", 8)
        card4 = Card("Diamonds", 10)
        cards = [card1, card2, card3, card4]
        expected = "You have a total of 28"
        actual = self.game.cards_total(cards)
        self.assertEqual(expected, actual)
