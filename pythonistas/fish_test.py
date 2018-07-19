
import unittest
import random
from functools import reduce


class Game(object):

    UNSHUFFLED_DECK = list(range(1,14)) * 4
    SHUFFLED_DECK = list(UNSHUFFLED_DECK)
    random.shuffle(SHUFFLED_DECK)

    PLAYER_1_HAND = SHUFFLED_DECK[:7] 
    PLAYER_2_HAND = SHUFFLED_DECK[7:14]
    SHUFFLED_DECK = SHUFFLED_DECK[14:]

def has_card_in_hand(hand, card):
    return card in hand

def transfer_card(hand_from, hand_to, card):
    cards_to_remove = hand_from.count(card)
    hand_to += [card] * cards_to_remove
    while (card in hand_from):
        hand_from.remove(card)
    return True

class TestFish(unittest.TestCase):

    def set_up_test(self):
        return Game()

    def test_length_of_card_deck(self): 
        new_game = self.set_up_test()
        self.assertEqual(len(new_game.UNSHUFFLED_DECK),52, "Deck needs to be 52 cards")

    def test_is_deck_random(self):
        new_game = self.set_up_test()
        self.assertNotEqual(new_game.UNSHUFFLED_DECK, new_game.SHUFFLED_DECK, "Deck hasn't been shuffled correctly")

    def test_each_player_has_correct_starting_hand(self):
        new_game = self.set_up_test()
        self.assertEqual (len(new_game.PLAYER_1_HAND),7,"Player 1 doesn't have 7 cards initially")
        self.assertEqual (len(new_game.PLAYER_2_HAND),7,"Player 2 doesn't have 7 cards initially")
    
    def test_remaining_cards_after_initial_deal(self):
        new_game = self.set_up_test()
        self.assertEqual (len(new_game.SHUFFLED_DECK),38,"Deck after initial deal doesn't have 38 cards")

    def test_player1_is_asking_a_number_they_have(self):
        new_game = self.set_up_test()
        card_choice = random.choice(list(range(1,14)))
        self.assertEqual (has_card_in_hand(new_game.PLAYER_1_HAND,card_choice),
            (card_choice in new_game.PLAYER_1_HAND),
            "Incorrect result from function has_card_in_hand")

    def test_card_transfer(self):
        new_game = self.set_up_test()
        initial_length_player_1 = len(new_game.PLAYER_1_HAND)
        initial_length_player_2 = len(new_game.PLAYER_2_HAND)
        card_value = random.choice(new_game.PLAYER_2_HAND)
        transfer_card(new_game.PLAYER_2_HAND, new_game.PLAYER_1_HAND, card_value)

        self.assertEqual(len(new_game.PLAYER_1_HAND + new_game.PLAYER_2_HAND),
            initial_length_player_1 + initial_length_player_2,
            "Number of cards in both hands incorrectly changed after transfer")

        self.assertTrue(card_value in new_game.PLAYER_1_HAND)
        self.assertTrue(card_value not in new_game.PLAYER_2_HAND)



if __name__ == '__main__':
    unittest.main()