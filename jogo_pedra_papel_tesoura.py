"""Jogo Pedra, Papel e Tesoura - versão refatorada.

Módulo com funções testáveis e interface interativa simples.
"""

from __future__ import annotations

import random
from typing import Literal

OPTIONS: tuple[str, ...] = ("pedra", "papel", "tesoura")
Choice = Literal["pedra", "papel", "tesoura"]


def get_computer_choice() -> Choice:
    """Retorna uma escolha aleatória do computador."""
    return random.choice(OPTIONS)  # type: ignore[return-value]


def get_player_choice(prompt: str = "Escolha pedra, papel ou tesoura: ") -> Choice:
    """Solicita a escolha do jogador até receber uma resposta válida."""
    while True:
        resposta = input(prompt).strip().lower()
        if resposta in OPTIONS:
            return resposta  # type: ignore[return-value]
        print("Opção inválida. Digite: pedra, papel ou tesoura.")


def determine_winner(jogador: str, computador: str) -> Literal["player", "computer", "tie"]:
    """Determina o vencedor de uma rodada.

    Retorna 'player' se o jogador vence, 'computer' se o computador vence
    e 'tie' em caso de empate.
    """
    if jogador == computador:
        return "tie"

    wins = {
        "pedra": "tesoura",
        "tesoura": "papel",
        "papel": "pedra",
    }

    if wins.get(jogador) == computador:
        return "player"
    return "computer"


def play_round(interactive: bool = True, player_choice: str | None = None) -> Literal["player", "computer", "tie"]:
    """Executa uma rodada. Em modo não interativo, passe `player_choice` para testar."""
    player = player_choice if player_choice is not None else get_player_choice()
    computer = get_computer_choice()
    result = determine_winner(player, computer)
    if interactive:
        print(f"Você escolheu {player}")
        print(f"Computador escolheu {computer}")
        if result == "tie":
            print("Empate!")
        elif result == "player":
            print("Você venceu!")
        else:
            print("Computador venceu!")
    return result


def main() -> None:
    """Loop principal interativo do jogo."""
    try:
        while True:
            play_round(interactive=True)
            repetir = input("Jogar novamente? (s/n): ").strip().lower()
            while repetir not in ("s", "n"):
                repetir = input("Digite apenas 's' para sim ou 'n' para não: ").strip().lower()
            if repetir != "s":
                print("Obrigado por jogar!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nEncerrando o jogo. Obrigado por jogar!")


if __name__ == "__main__":
    main()