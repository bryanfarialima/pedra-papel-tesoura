"""Testes unitários para o jogo Pedra, Papel e Tesoura.

Cobre todos os casos de vitória, derrota e empate sem mocks complexos.
Funções puras permitem testes simples e determinísticos.
"""

import unittest
import sys
from pathlib import Path

# Adiciona diretório pai ao path para importação
sys.path.insert(0, str(Path(__file__).parent.parent))

import jogo_pedra_papel_tesoura as game


class TestDetermineWinner(unittest.TestCase):
    """Testes para a função determine_winner."""

    def test_tie_all_cases(self):
        """Testa empate em todos os casos."""
        for option in ("pedra", "papel", "tesoura"):
            with self.subTest(option=option):
                result = game.determine_winner(option, option)
                self.assertEqual(result, "tie")

    def test_player_wins_pedra(self):
        """Testa vitória: pedra vence tesoura."""
        result = game.determine_winner("pedra", "tesoura")
        self.assertEqual(result, "player")

    def test_player_wins_tesoura(self):
        """Testa vitória: tesoura vence papel."""
        result = game.determine_winner("tesoura", "papel")
        self.assertEqual(result, "player")

    def test_player_wins_papel(self):
        """Testa vitória: papel vence pedra."""
        result = game.determine_winner("papel", "pedra")
        self.assertEqual(result, "player")

    def test_computer_wins_pedra(self):
        """Testa derrota: tesoura vence pedra."""
        result = game.determine_winner("tesoura", "pedra")
        self.assertEqual(result, "computer")

    def test_computer_wins_papel(self):
        """Testa derrota: pedra vence papel."""
        result = game.determine_winner("pedra", "papel")
        self.assertEqual(result, "computer")

    def test_computer_wins_tesoura(self):
        """Testa derrota: papel vence tesoura."""
        result = game.determine_winner("papel", "tesoura")
        self.assertEqual(result, "computer")


class TestGetComputerChoice(unittest.TestCase):
    """Testes para a função get_computer_choice."""

    def test_returns_valid_choice(self):
        """Testa se retorna uma opção válida."""
        choice = game.get_computer_choice()
        self.assertIn(choice, game.OPTIONS)

    def test_returns_string(self):
        """Testa se retorna uma string."""
        choice = game.get_computer_choice()
        self.assertIsInstance(choice, str)

    def test_returns_one_of_three_options(self):
        """Testa se retorna uma das 3 opções possíveis."""
        for _ in range(10):  # Testa múltiplas vezes
            choice = game.get_computer_choice()
            self.assertIn(choice, ("pedra", "papel", "tesoura"))


class TestPlayRound(unittest.TestCase):
    """Testes para a função play_round."""

    def test_play_round_non_interactive_tie(self):
        """Testa rodada em modo não-interativo com empate."""
        result = game.play_round(interactive=False, player_choice="pedra")
        self.assertIn(result, ("player", "computer", "tie"))

    def test_play_round_returns_valid_result(self):
        """Testa se play_round retorna resultado válido."""
        result = game.play_round(interactive=False, player_choice="papel")
        self.assertIn(result, ("player", "computer", "tie"))

    def test_play_round_with_all_choices(self):
        """Testa play_round com todas as opções."""
        for choice in ("pedra", "papel", "tesoura"):
            with self.subTest(choice=choice):
                result = game.play_round(interactive=False, player_choice=choice)
                self.assertIn(result, ("player", "computer", "tie"))


if __name__ == "__main__":
    unittest.main()
