"""Jogo Pedra, Papel e Tesoura - implementação profissional.

Módulo com funções testáveis e interface interativa. Demonstra boas práticas:
- Separação de responsabilidades (I/O vs lógica)
- Type hints completos (Literal type alias)
- Docstrings em padrão Google
- Funções puras (testáveis)

Exemplo de uso:
    >>> determine_winner("pedra", "tesoura")
    'player'
    >>> determine_winner("papel", "papel")
    'tie'

Para jogar interativo:
    >>> python3 jogo_pedra_papel_tesoura.py
"""

from __future__ import annotations

import random
from typing import Literal

# Constantes
OPTIONS: tuple[str, ...] = ("pedra", "papel", "tesoura")

# Type alias para melhor legibilidade
Choice = Literal["pedra", "papel", "tesoura"]


def get_computer_choice() -> Choice:
    """Retorna uma escolha aleatória do computador.
    
    Returns:
        Choice: Uma das opções ('pedra', 'papel', 'tesoura') escolhida aleatoriamente.
    
    Example:
        >>> choice = get_computer_choice()
        >>> choice in OPTIONS
        True
    """
    return random.choice(OPTIONS)  # type: ignore[return-value]


def get_player_choice(prompt: str = "Escolha pedra, papel ou tesoura: ") -> Choice:
    """Solicita a escolha do jogador até receber uma resposta válida.
    
    Valida a entrada do usuário em um loop até receber uma opção válida.
    Input é convertido para minúsculas e removido espaços em branco.
    
    Args:
        prompt: Mensagem para exibir ao solicitar entrada (default padrão).
    
    Returns:
        Choice: A escolha válida do jogador.
    
    Example:
        >>> # Interativo no terminal
        >>> player = get_player_choice()
        Escolha pedra, papel ou tesoura: pedra
        # Retorna: 'pedra'
    """
    while True:
        resposta = input(prompt).strip().lower()
        if resposta in OPTIONS:
            return resposta  # type: ignore[return-value]
        print("Opção inválida. Digite: pedra, papel ou tesoura.")


def determine_winner(jogador: str, computador: str) -> Literal["player", "computer", "tie"]:
    """Determina o vencedor de uma rodada. Função pura (sem I/O).
    
    Implementa as regras clássicas:
    - Pedra vence Tesoura
    - Tesoura vence Papel
    - Papel vence Pedra
    
    Args:
        jogador: Escolha do jogador ('pedra', 'papel' ou 'tesoura').
        computador: Escolha do computador ('pedra', 'papel' ou 'tesoura').
    
    Returns:
        Literal["player", "computer", "tie"]: Resultado da rodada.
            - 'player': jogador ganhou
            - 'computer': computador ganhou
            - 'tie': empate
    
    Raises:
        Nenhuma exceção é levantada. Função pura sem efeitos colaterais.
    
    Example:
        >>> determine_winner("pedra", "tesoura")
        'player'
        >>> determine_winner("papel", "papel")
        'tie'
        >>> determine_winner("tesoura", "pedra")
        'computer'
    """
    if jogador == computador:
        return "tie"

    # Dicionário de vitórias: chave vence valor
    wins = {
        "pedra": "tesoura",
        "tesoura": "papel",
        "papel": "pedra",
    }

    if wins.get(jogador) == computador:
        return "player"
    return "computer"


def play_round(interactive: bool = True, player_choice: str | None = None) -> Literal["player", "computer", "tie"]:
    """Executa uma rodada do jogo. Combina lógica com exibição.
    
    Esta função orquestra uma rodada: obtém as escolhas, determina o vencedor
    e opcionalmente exibe o resultado. Pode ser usada em modo interativo ou
    teste (passando player_choice para bypass do input).
    
    Args:
        interactive: Se True, exibe escolhas e resultado no console.
                    Se False, apenas retorna o resultado (útil para testes).
        player_choice: Opcional. Se fornecido, usa esta escolha em vez de 
                       chamar get_player_choice(). Útil para testes automatizados.
    
    Returns:
        Literal["player", "computer", "tie"]: Resultado da rodada.
    
    Example:
        >>> result = play_round(interactive=False, player_choice="pedra")
        >>> result in ["player", "computer", "tie"]
        True
    """
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
    """Loop principal interativo do jogo.
    
    Executa rodadas do jogo em loop até o usuário escolher sair.
    Trata exceções para encerramento gracioso (Ctrl+C, EOF).
    
    Fluxo:
        1. Executa uma rodada com play_round()
        2. Pergunta se quer jogar novamente
        3. Valida resposta (s/n)
        4. Repete ou encerra
    
    Exceções tratadas:
        - KeyboardInterrupt: Usuário pressiona Ctrl+C
        - EOFError: Fim da entrada (p.ex., EOF em stdin)
    
    Example:
        >>> # Executar jogo interativo
        >>> main()
        Escolha pedra, papel ou tesoura: pedra
        ...
    """
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