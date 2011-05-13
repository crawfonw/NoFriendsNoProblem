import unittest

from DiscardPileObjects import DiscardPile

from UnoCardObjects import UnoCard
from UnoAIPlayerObjects import AIUnoPlayer

class TestUnoHumanPlayer(unittest.TestCase):

    def setUp(self):
        self.player = AIUnoPlayer()
        self.other = AIUnoPlayer()
        self.discard = DiscardPile()
        self.other.hand = [UnoCard(-1, 'Wild', 'Black'), UnoCard(-1, 'Wild', 'Black'), UnoCard(-1, 'Wild', 'Black'), UnoCard(-1, 'Wild', 'Black'), UnoCard(-1, 'Wild', 'Black'), UnoCard(-1, 'Wild', 'Black'), UnoCard(-1, 'Wild', 'Black')]

    def test_choose_color(self):
        self.discard.cards = [UnoCard(1, 'Number', 'Red')]
        self.player.hand = [UnoCard(7, 'Number', 'Red'), UnoCard(4, 'Number', 'Red'), UnoCard(-1, 'Reverse', 'Red'), UnoCard(3, 'Number', 'Blue'), UnoCard(4, 'Number', 'Blue'), UnoCard(0, 'Number', 'Yellow'), UnoCard(10, 'Number', 'Green')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertTrue('Red' in move and 'Skip' not in move)

    def test_choose_color_2(self):
        self.discard.cards = [UnoCard(1, 'Number', 'Green')]
        self.player.hand = [UnoCard(7, 'Number', 'Red'), UnoCard(4, 'Number', 'Red'), UnoCard(3, 'Number', 'Blue'), UnoCard(4, 'Number', 'Blue'), UnoCard(0, 'Number', 'Yellow'), UnoCard(10, 'Number', 'Green')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertTrue('Green' in move)

    def test_choose_color_3(self):
        self.discard.cards = [UnoCard(1, 'Number', 'Green')]
        self.player.hand = [UnoCard(7, 'Number', 'Red'), UnoCard(4, 'Number', 'Red'), UnoCard(3, 'Number', 'Blue'), UnoCard(4, 'Number', 'Blue')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertTrue('Draw' in move)

    def test_number_choice(self):
        self.discard.cards = [UnoCard(1, 'Number', 'Green')]
        self.player.hand = [UnoCard(1, 'Number', 'Red'), UnoCard(4, 'Number', 'Red'), UnoCard(3, 'Number', 'Red'), UnoCard(1, 'Number', 'Blue')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Red 1', move)

    def test_number_choice_2(self):
        self.discard.cards = [UnoCard(2, 'Number', 'Green')]
        self.player.hand = [UnoCard(1, 'Number', 'Red'), UnoCard(4, 'Number', 'Red'), UnoCard(3, 'Number', 'Red'), UnoCard(2, 'Number', 'Blue')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Blue 2', move)

    def test_do_not_pick_wild_card(self):
        self.discard.cards = [UnoCard(2, 'Number', 'Red')]
        self.player.hand = [UnoCard(-1, 'Wild', 'Black'), UnoCard(4, 'Number', 'Red'), UnoCard(3, 'Number', 'Red'), UnoCard(2, 'Number', 'Blue')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertTrue('Red' in move)

    def test_pick_wild_and_change_to_yellow(self):
        self.discard.cards = [UnoCard(0, 'Number', 'Red')]
        self.player.hand = [UnoCard(-1, 'Wild', 'Black'), UnoCard(4, 'Number', 'Blue'), UnoCard(3, 'Number', 'Yellow'), UnoCard(2, 'Number', 'Yellow')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Yellow Wild', move)

    def test_pick_reverse_only_choice(self):
        self.discard.cards = [UnoCard(0, 'Number', 'Yellow')]
        self.player.hand = [UnoCard(-1, 'Skip', 'Red'), UnoCard(4, 'Number', 'Blue'), UnoCard(-1, 'Reverse', 'Yellow')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Yellow Reverse', move)

    def test_pick_reverse_only_choice_2(self):
        self.discard.cards = [UnoCard(-1, 'Reverse', 'Blue')]
        self.player.hand = [UnoCard(-1, 'Skip', 'Red'), UnoCard(4, 'Number', 'Green'), UnoCard(-1, 'Reverse', 'Yellow')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Yellow Reverse', move)

    def test_pick_reverse_due_to_player(self):
        self.discard.cards = [UnoCard(0, 'Number', 'Yellow')]
        self.player.hand = [UnoCard(1, 'Number', 'Yellow'), UnoCard(4, 'Number', 'Yellow'), UnoCard(-1, 'Reverse', 'Yellow')]
        self.other.hand = [UnoCard(-1, 'Wild', 'Black')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Yellow Reverse', move)

    def test_pick_skip_only_choice(self):
        self.discard.cards = [UnoCard(0, 'Number', 'Red')]
        self.player.hand = [UnoCard(-1, 'Skip', 'Red'), UnoCard(4, 'Number', 'Blue'), UnoCard(-1, 'Reverse', 'Yellow')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Red Skip', move)

    def test_pick_skip_only_choice_2(self):
        self.discard.cards = [UnoCard(-1, 'Skip', 'Green')]
        self.player.hand = [UnoCard(-1, 'Skip', 'Red'), UnoCard(4, 'Number', 'Blue'), UnoCard(-1, 'Reverse', 'Yellow')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Red Skip', move)

    def test_pick_skip_due_to_player(self):
        self.discard.cards = [UnoCard(0, 'Number', 'Yellow')]
        self.player.hand = [UnoCard(1, 'Number', 'Yellow'), UnoCard(4, 'Number', 'Yellow'), UnoCard(-1, 'Skip', 'Yellow')]
        self.other.hand = [UnoCard(-1, 'Wild', 'Black')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Yellow Skip', move)

    def test_pick_draw_two_only_choice(self):
        self.discard.cards = [UnoCard(0, 'Number', 'Red')]
        self.player.hand = [UnoCard(-1, 'Draw Two', 'Red'), UnoCard(4, 'Number', 'Blue'), UnoCard(-1, 'Reverse', 'Yellow')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Red Draw Two', move)

    def test_pick_draw_two_only_choice_2(self):
        self.discard.cards = [UnoCard(-1, 'Draw Two', 'Green')]
        self.player.hand = [UnoCard(-1, 'Skip', 'Red'), UnoCard(4, 'Number', 'Blue'), UnoCard(-1, 'Draw Two', 'Yellow')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Yellow Draw Two', move)

    def test_pick_skip_due_to_player(self):
        self.discard.cards = [UnoCard(0, 'Number', 'Yellow')]
        self.player.hand = [UnoCard(1, 'Number', 'Yellow'), UnoCard(4, 'Number', 'Yellow'), UnoCard(-1, 'Draw Two', 'Yellow')]
        self.other.hand = [UnoCard(-1, 'Wild', 'Black')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Yellow Draw Two', move)

    def test_pick_skip_over_reverse_or_draw_two_or_wild(self):
        self.discard.cards = [UnoCard(0, 'Number', 'Red')]
        self.player.hand = [UnoCard(-1, 'Draw Two', 'Red'), UnoCard(-1, 'Reverse', 'Red'), UnoCard(-1, 'Skip', 'Red'), UnoCard(-1, 'Wild', 'Black')]
        move = self.player.find_best_move(self.other, self.discard)
        self.assertEqual('Red Skip', move)



if __name__ == '__main__':
    unittest.main()
