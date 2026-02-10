"""Testes unitários para o jogo Pedra, Papel e Tesoura (completo).

Cobre:
- Modo clássico (3 opções)
- Modo PPLS (5 opções)
- Ventagens cruzadas
- Funções utilitárias multiplataforma
"""

import unittest
import sys
from pathlib import Path

# Adiciona diretório pai ao path para importação
sys.path.insert(0, str(Path(__file__).parent.parent))

import jogo_pedra_papel_tesoura as game


class TestDetermineWinnerClassic(unittest.TestCase):
    """Testes para determine_winner_classic."""

    def test_tie_all_cases(self):
        """Testa empate em todos os casos."""
        for option in game.CLASSIC_OPTIONS:
            with self.subTest(option=option):
                result = game.determine_winner_classic(option, option)
                self.assertEqual(result, "tie")

    def test_player1_wins_pedra(self):
        """Testa vitória: pedra vence tesoura."""
        result = game.determine_winner_classic("pedra", "tesoura")
        self.assertEqual(result, "player1")

    def test_player1_wins_tesoura(self):
        """Testa vitória: tesoura vence papel."""
        result = game.determine_winner_classic("tesoura", "papel")
        self.assertEqual(result, "player1")

    def test_player1_wins_papel(self):
        """Testa vitória: papel vence pedra."""
        result = game.determine_winner_classic("papel", "pedra")
        self.assertEqual(result, "player1")

    def test_player2_wins_pedra(self):
        """Testa derrota: tesoura vence pedra."""
        result = game.determine_winner_classic("tesoura", "pedra")
        self.assertEqual(result, "player2")

    def test_player2_wins_papel(self):
        """Testa derrota: pedra vence papel."""
        result = game.determine_winner_classic("pedra", "papel")
        self.assertEqual(result, "player2")

    def test_player2_wins_tesoura(self):
        """Testa derrota: papel vence tesoura."""
        result = game.determine_winner_classic("papel", "tesoura")
        self.assertEqual(result, "player2")


class TestDetermineWinnerPPLS(unittest.TestCase):
    """Testes para determine_winner_ppls."""

    def test_tie_all_cases(self):
        """Testa empate em todos os casos PPLS."""
        for option in game.PPLS_OPTIONS:
            with self.subTest(option=option):
                result = game.determine_winner_ppls(option, option)
                self.assertEqual(result, "tie")

    def test_pedra_vence(self):
        """Testa pedra vence lagarto e tesoura."""
        self.assertEqual(game.determine_winner_ppls("pedra", "lagarto"), "player1")
        self.assertEqual(game.determine_winner_ppls("pedra", "tesoura"), "player1")

    def test_papel_vence(self):
        """Testa papel vence pedra e spock."""
        self.assertEqual(game.determine_winner_ppls("papel", "pedra"), "player1")
        self.assertEqual(game.determine_winner_ppls("papel", "spock"), "player1")

    def test_tesoura_vence(self):
        """Testa tesoura vence papel e lagarto."""
        self.assertEqual(game.determine_winner_ppls("tesoura", "papel"), "player1")
        self.assertEqual(game.determine_winner_ppls("tesoura", "lagarto"), "player1")

    def test_lagarto_vence(self):
        """Testa lagarto vence papel e spock."""
        self.assertEqual(game.determine_winner_ppls("lagarto", "papel"), "player1")
        self.assertEqual(game.determine_winner_ppls("lagarto", "spock"), "player1")

    def test_spock_vence(self):
        """Testa spock vence tesoura e pedra."""
        self.assertEqual(game.determine_winner_ppls("spock", "tesoura"), "player1")
        self.assertEqual(game.determine_winner_ppls("spock", "pedra"), "player1")

    def test_player2_wins_ppls(self):
        """Testa vitória Player 2 em PPLS."""
        result = game.determine_winner_ppls("tesoura", "pedra")
        self.assertEqual(result, "player2")


class TestGetComputerChoice(unittest.TestCase):
    """Testes para get_computer_choice."""

    def test_returns_valid_classic_choice(self):
        """Testa retorna opção válida no modo clássico."""
        for _ in range(10):
            choice = game.get_computer_choice(game.CLASSIC_OPTIONS)
            self.assertIn(choice, game.CLASSIC_OPTIONS)

    def test_returns_valid_ppls_choice(self):
        """Testa retorna opção válida no modo PPLS."""
        for _ in range(10):
            choice = game.get_computer_choice(game.PPLS_OPTIONS)
            self.assertIn(choice, game.PPLS_OPTIONS)

    def test_returns_string(self):
        """Testa retorna string."""
        choice = game.get_computer_choice()
        self.assertIsInstance(choice, str)


class TestGameVariants(unittest.TestCase):
    """Testes para variantes do jogo."""

    def test_classic_has_three_options(self):
        """Testa modo clássico tem 3 opções."""
        self.assertEqual(len(game.CLASSIC_OPTIONS), 3)
        self.assertIn("pedra", game.CLASSIC_OPTIONS)
        self.assertIn("papel", game.CLASSIC_OPTIONS)
        self.assertIn("tesoura", game.CLASSIC_OPTIONS)

    def test_ppls_has_five_options(self):
        """Testa modo PPLS tem 5 opções."""
        self.assertEqual(len(game.PPLS_OPTIONS), 5)
        self.assertIn("pedra", game.PPLS_OPTIONS)
        self.assertIn("papel", game.PPLS_OPTIONS)
        self.assertIn("tesoura", game.PPLS_OPTIONS)
        self.assertIn("lagarto", game.PPLS_OPTIONS)
        self.assertIn("spock", game.PPLS_OPTIONS)

    def test_ppls_each_option_beats_two(self):
        """Testa que cada opção PPLS vence exatamente 2 outras."""
        for option in game.PPLS_OPTIONS:
            wins_count = 0
            for other_option in game.PPLS_OPTIONS:
                if option != other_option:
                    if game.determine_winner_ppls(option, other_option) == "player1":
                        wins_count += 1
            self.assertEqual(wins_count, 2, f"{option} deveria vencer 2, mas venceu {wins_count}")


class TestGameModes(unittest.TestCase):
    """Testes para estrutura de modos de jogo."""

    def test_game_mode_enum_exists(self):
        """Testa que enum GameMode existe."""
        self.assertTrue(hasattr(game, 'GameMode'))

    def test_game_variant_enum_exists(self):
        """Testa que enum GameVariant existe."""
        self.assertTrue(hasattr(game, 'GameVariant'))

    def test_clear_screen_function_exists(self):
        """Testa que função clear_screen existe."""
        self.assertTrue(callable(game.clear_screen))

    def test_print_functions_exist(self):
        """Testa que funções de print existem."""
        self.assertTrue(callable(game.print_divider))
        self.assertTrue(callable(game.print_header))


class TestComprehensiveBattle(unittest.TestCase):
    """Testes integrados de batalhas."""

    def test_classic_all_matchups(self):
        """Testa todos os confrontos no modo clássico."""
        matchups = [
            ("pedra", "tesoura", "player1"),
            ("tesoura", "papel", "player1"),
            ("papel", "pedra", "player1"),
            ("tesoura", "pedra", "player2"),
            ("papel", "tesoura", "player2"),
            ("pedra", "papel", "player2"),
        ]
        for p1, p2, expected in matchups:
            with self.subTest(p1=p1, p2=p2):
                result = game.determine_winner_classic(p1, p2)
                self.assertEqual(result, expected)

    def test_ppls_balanced_distribution(self):
        """Testa que PPLS tem distribuição balanceada."""
        # Cada opção deve vencer 40% (2/5) dos casos
        for option in game.PPLS_OPTIONS:
            win_rate = 0
            for other in game.PPLS_OPTIONS:
                if option != other and game.determine_winner_ppls(option, other) == "player1":
                    win_rate += 1
            expected_wins = 2
            self.assertEqual(
                win_rate, expected_wins,
                f"{option} deveria vencer {expected_wins} de 4 opções, mas venceu {win_rate}"
            )


if __name__ == "__main__":
    unittest.main()

