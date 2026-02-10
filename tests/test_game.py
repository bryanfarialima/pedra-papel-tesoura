import unittest

from Pedra_Papel_Tesoura import jogo_pedra_papel_tesoura as game


class TestDetermineWinner(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(game.determine_winner("pedra", "pedra"), "tie")

    def test_player_wins(self):
        self.assertEqual(game.determine_winner("pedra", "tesoura"), "player")
        self.assertEqual(game.determine_winner("tesoura", "papel"), "player")
        self.assertEqual(game.determine_winner("papel", "pedra"), "player")

    def test_computer_wins(self):
        self.assertEqual(game.determine_winner("tesoura", "pedra"), "computer")
        self.assertEqual(game.determine_winner("papel", "tesoura"), "computer")
        self.assertEqual(game.determine_winner("pedra", "papel"), "computer")


if __name__ == "__main__":
    unittest.main()
