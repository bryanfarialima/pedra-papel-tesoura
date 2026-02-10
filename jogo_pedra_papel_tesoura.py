"""Jogo Pedra, Papel e Tesoura - Implementação Profissional e Multiplataforma.

Suporta múltiplos modos:
- VS Computador (clássico)
- Multiplayer Local (2 jogadores)
- Variação PPLS (Pedra-Papel-Lagarto-Spock)

Compatível: macOS, Linux, Windows
Requisitos: Python 3.9+

Exemplo de uso:
    >>> python3 jogo_pedra_papel_tesoura.py
"""

from __future__ import annotations

import os
import random
import platform
from typing import Literal
from enum import Enum

# ============================================================================
# TIPOS E CONSTANTES
# ============================================================================

class GameMode(Enum):
    """Modos de jogo disponíveis."""
    VS_COMPUTER = "1"      # Jogar contra computador
    MULTIPLAYER = "2"      # Dois jogadores locais
    PPLS = "3"             # Pedra-Papel-Lagarto-Spock


class GameVariant(Enum):
    """Variações de regras do jogo."""
    CLASSIC = "1"          # Pedra-Papel-Tesoura
    PPLS = "2"             # Pedra-Papel-Lagarto-Spock


# Opções para cada variante
CLASSIC_OPTIONS: tuple[str, ...] = ("pedra", "papel", "tesoura")
PPLS_OPTIONS: tuple[str, ...] = ("pedra", "papel", "tesoura", "lagarto", "spock")

# Type aliases
ClassicChoice = Literal["pedra", "papel", "tesoura"]
PPLSChoice = Literal["pedra", "papel", "tesoura", "lagarto", "spock"]
Result = Literal["player1", "player2", "tie"]


# ============================================================================
# FUNÇÕES UTILITÁRIAS
# ============================================================================

def clear_screen() -> None:
    """Limpa a tela de forma multiplataforma.
    
    Funciona em Windows, macOS e Linux.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def print_divider(char: str = "=", width: int = 60) -> None:
    """Imprime uma linha divisória.
    
    Args:
        char: Caractere a usar.
        width: Largura da linha.
    """
    print(char * width)


def print_header(title: str) -> None:
    """Imprime um cabeçalho formatado.
    
    Args:
        title: Título a exibir.
    """
    print_divider()
    print(f"  {title.center(56)}")
    print_divider()


# ============================================================================
# PEDRA-PAPEL-TESOURA CLÁSSICO
# ============================================================================

def determine_winner_classic(player1: str, player2: str) -> Result:
    """Determina o vencedor do modo clássico (Pedra-Papel-Tesoura).
    
    Regras:
    - Pedra vence Tesoura
    - Tesoura vence Papel
    - Papel vence Pedra
    
    Args:
        player1: Escolha do jogador 1.
        player2: Escolha do jogador 2 ou computador.
    
    Returns:
        Result: 'player1' se jogador 1 vence, 'player2' se jogador 2 vence,
                'tie' em empate.
    
    Example:
        >>> determine_winner_classic("pedra", "tesoura")
        'player1'
    """
    if player1 == player2:
        return "tie"
    
    wins = {
        "pedra": "tesoura",
        "tesoura": "papel",
        "papel": "pedra",
    }
    
    return "player1" if wins.get(player1) == player2 else "player2"


# ============================================================================
# PEDRA-PAPEL-LAGARTO-SPOCK
# ============================================================================

def determine_winner_ppls(player1: str, player2: str) -> Result:
    """Determina o vencedor do modo PPLS (Pedra-Papel-Lagarto-Spock).
    
    Regras expandidas:
    - Pedra esmagaca Lagarto e ganha de Tesoura
    - Papel cobre Pedra e ganha de Spock
    - Tesoura corta Papel e ganha de Lagarto
    - Lagarto come Papel e ganha de Spock
    - Spock esmaga Tesoura e ganha de Pedra
    
    Args:
        player1: Escolha do jogador 1.
        player2: Escolha do jogador 2 ou computador.
    
    Returns:
        Result: Resultado da rodada.
    
    Example:
        >>> determine_winner_ppls("pedra", "lagarto")
        'player1'
    """
    if player1 == player2:
        return "tie"
    
    # Cada opção vence dois outros
    wins = {
        "pedra": ("lagarto", "tesoura"),
        "papel": ("pedra", "spock"),
        "tesoura": ("papel", "lagarto"),
        "lagarto": ("papel", "spock"),
        "spock": ("tesoura", "pedra"),
    }
    
    return "player1" if player2 in wins.get(player1, ()) else "player2"


# ============================================================================
# ENTRADA DO JOGADOR
# ============================================================================

def get_player_choice(
    prompt: str = "Sua escolha",
    options: tuple[str, ...] = CLASSIC_OPTIONS
) -> str:
    """Obtém a escolha do jogador com validação.
    
    Args:
        prompt: Mensagem a exibir.
        options: Opções válidas.
    
    Returns:
        str: Escolha validada do jogador.
    """
    options_str = ", ".join(options)
    while True:
        resposta = input(f"{prompt} ({options_str}): ").strip().lower()
        if resposta in options:
            return resposta
        print(f"❌ Opção inválida! Digite uma de: {options_str}")


def get_computer_choice(options: tuple[str, ...] = CLASSIC_OPTIONS) -> str:
    """Retorna uma escolha aleatória do computador.
    
    Args:
        options: Opções disponíveis.
    
    Returns:
        str: Escolha aleatória.
    """
    return random.choice(options)


def get_yes_no(prompt: str = "Deseja continuar") -> bool:
    """Obtém resposta sim/não do usuário.
    
    Args:
        prompt: Pergunta a fazer.
    
    Returns:
        bool: True se sim, False se não.
    """
    while True:
        resposta = input(f"{prompt}? (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        elif resposta in ("n", "nao", "não"):
            return False
        print("❌ Digite 's' para sim ou 'n' para não")


# ============================================================================
# EXIBIÇÃO DE RESULTADOS
# ============================================================================

def display_round_classic(
    player1_name: str, player1_choice: str,
    player2_name: str, player2_choice: str,
    result: Result
) -> None:
    """Exibe resultado de uma rodada do modo clássico.
    
    Args:
        player1_name: Nome do jogador 1 ou "Você".
        player1_choice: Escolha do jogador 1.
        player2_name: Nome do jogador 2, "Computador" ou "Você".
        player2_choice: Escolha do jogador 2.
        result: Resultado da rodada.
    """
    print(f"\n{player1_name} escolheu: {player1_choice}")
    print(f"{player2_name} escolheu: {player2_choice}")
    
    if result == "tie":
        print("🤝 EMPATE!")
    elif result == "player1":
        print(f"🎉 {player1_name} VENCEU!")
    else:
        print(f"🎉 {player2_name} VENCEU!")


def display_ppls_rules() -> None:
    """Exibe as regras do modo PPLS."""
    clear_screen()
    print_header("📜 Regras PPLS")
    print("""
Cada opção vence DUAS outras:

  🪨 PEDRA        vence: Tesoura, Lagarto
  📄 PAPEL        vence: Pedra, Spock
  ✂️  TESOURA     vence: Papel, Lagarto
  🦎 LAGARTO      vence: Papel, Spock
  🖖 SPOCK        vence: Tesoura, Pedra
    """)
    input("Pressione ENTER para continuar...")


# ============================================================================
# MODOS DE JOGO
# ============================================================================

def play_vs_computer_classic() -> None:
    """Joga Pedra-Papel-Tesoura contra computador."""
    print_header("🎮 PEDRA-PAPEL-TESOURA vs COMPUTADOR")
    
    while True:
        player_choice = get_player_choice(
            prompt="Sua escolha",
            options=CLASSIC_OPTIONS
        )
        computer_choice = get_computer_choice(CLASSIC_OPTIONS)
        result = determine_winner_classic(player_choice, computer_choice)
        
        display_round_classic(
            "Você", player_choice,
            "Computador", computer_choice,
            result
        )
        
        if not get_yes_no("\nJogar novamente"):
            break


def play_vs_computer_ppls() -> None:
    """Joga PPLS contra computador."""
    display_ppls_rules()
    clear_screen()
    print_header("🎮 PPLS vs COMPUTADOR")
    
    while True:
        player_choice = get_player_choice(
            prompt="Sua escolha",
            options=PPLS_OPTIONS
        )
        computer_choice = get_computer_choice(PPLS_OPTIONS)
        result = determine_winner_ppls(player_choice, computer_choice)
        
        display_round_classic(
            "Você", player_choice,
            "Computador", computer_choice,
            result
        )
        
        if not get_yes_no("\nJogar novamente"):
            break


def play_multiplayer_classic() -> None:
    """Dois jogadores locais em Pedra-Papel-Tesoura."""
    print_header("🎮 MULTIPLAYER LOCAL - CLÁSSICO")
    
    player1_name = input("Nome do Jogador 1: ").strip() or "Jogador 1"
    player2_name = input("Nome do Jogador 2: ").strip() or "Jogador 2"
    
    score1, score2 = 0, 0
    
    while True:
        clear_screen()
        print_header(f"{player1_name} vs {player2_name}")
        print(f"Placar: {player1_name} {score1} - {score2} {player2_name}\n")
        
        # Jogador 1
        print(f"🎯 {player1_name} - escolha sua opção:")
        player1_choice = get_player_choice(
            prompt="Escolha",
            options=CLASSIC_OPTIONS
        )
        
        # Limpar tela para privacidade
        clear_screen()
        print(f"✅ {player1_name} fez sua escolha!\n")
        
        # Jogador 2
        print(f"🎯 {player2_name} - escolha sua opção:")
        player2_choice = get_player_choice(
            prompt="Escolha",
            options=CLASSIC_OPTIONS
        )
        
        # Resultado
        clear_screen()
        result = determine_winner_classic(player1_choice, player2_choice)
        display_round_classic(
            player1_name, player1_choice,
            player2_name, player2_choice,
            result
        )
        
        # Atualizar placar
        if result == "player1":
            score1 += 1
        elif result == "player2":
            score2 += 1
        
        if not get_yes_no("\nProxima rodada"):
            break
    
    clear_screen()
    print_header("🏁 FIM DO JOGO")
    print(f"Placar final: {player1_name} {score1} - {score2} {player2_name}\n")
    if score1 > score2:
        print(f"🏆 {player1_name} VENCEU! 🏆\n")
    elif score2 > score1:
        print(f"🏆 {player2_name} VENCEU! 🏆\n")
    else:
        print("🤝 EMPATE GERAL! 🤝\n")


def play_multiplayer_ppls() -> None:
    """Dois jogadores locais em PPLS."""
    display_ppls_rules()
    
    clear_screen()
    print_header("🎮 MULTIPLAYER LOCAL - PPLS")
    
    player1_name = input("Nome do Jogador 1: ").strip() or "Jogador 1"
    player2_name = input("Nome do Jogador 2: ").strip() or "Jogador 2"
    
    score1, score2 = 0, 0
    
    while True:
        clear_screen()
        print_header(f"{player1_name} vs {player2_name}")
        print(f"Placar: {player1_name} {score1} - {score2} {player2_name}\n")
        
        print(f"🎯 {player1_name} - escolha sua opção:")
        player1_choice = get_player_choice(
            prompt="Escolha",
            options=PPLS_OPTIONS
        )
        
        clear_screen()
        print(f"✅ {player1_name} fez sua escolha!\n")
        
        print(f"🎯 {player2_name} - escolha sua opção:")
        player2_choice = get_player_choice(
            prompt="Escolha",
            options=PPLS_OPTIONS
        )
        
        clear_screen()
        result = determine_winner_ppls(player1_choice, player2_choice)
        display_round_classic(
            player1_name, player1_choice,
            player2_name, player2_choice,
            result
        )
        
        if result == "player1":
            score1 += 1
        elif result == "player2":
            score2 += 1
        
        if not get_yes_no("\nProxima rodada"):
            break
    
    clear_screen()
    print_header("🏁 FIM DO JOGO")
    print(f"Placar final: {player1_name} {score1} - {score2} {player2_name}\n")
    if score1 > score2:
        print(f"🏆 {player1_name} VENCEU! 🏆\n")
    elif score2 > score1:
        print(f"🏆 {player2_name} VENCEU! 🏆\n")
    else:
        print("🤝 EMPATE GERAL! 🤝\n")


# ============================================================================
# MENU PRINCIPAL
# ============================================================================

def main_menu() -> None:
    """Menu principal interativo."""
    while True:
        clear_screen()
        print_header("🎮 PEDRA-PAPEL-TESOURA")
        print("""
Escolha o modo de jogo:

  1️⃣  VS Computador - Clássico
  2️⃣  Multiplayer Local - Clássico
  3️⃣  VS Computador - PPLS (Pedra-Papel-Lagarto-Spock)
  4️⃣  Multiplayer Local - PPLS
  5️⃣  Informações
  0️⃣  Sair
        """)
        
        choice = input("Escolha uma opção (0-5): ").strip()
        
        try:
            if choice == "1":
                play_vs_computer_classic()
            elif choice == "2":
                play_multiplayer_classic()
            elif choice == "3":
                play_vs_computer_ppls()
            elif choice == "4":
                play_multiplayer_ppls()
            elif choice == "5":
                show_info()
            elif choice == "0":
                print("\nObrigado por jogar! 👋\n")
                break
            else:
                print("❌ Opção inválida!")
                input("Pressione ENTER...")
        except (KeyboardInterrupt, EOFError):
            print("\n\nEncerrando... Até logo! 👋\n")
            break


def show_info() -> None:
    """Exibe informações sobre o jogo."""
    clear_screen()
    print_header("ℹ️ INFORMAÇÕES")
    print("""
🎮 PEDRA-PAPEL-TESOURA & PPLS

Versão: 1.1
Compatível: Windows, macOS, Linux
Python: 3.9+

Modos disponíveis:
  • Versus Computador (IA Random)
  • Multiplayer Local (2 jogadores)

Variações:
  • Clássica (3 opções)
  • PPLS (5 opções)

Autor: Bryan Faria
GitHub: github.com/bryanfarialima/Pedra-Papel-Tesoura

Boas práticas:
  • Type hints completos
  • Unit tests abrangentes
  • Docstrings detalhadas
  • Estrutura modular
    """)
    input("\nPressione ENTER para voltar...")


if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"❌ Erro: {e}")
        raise