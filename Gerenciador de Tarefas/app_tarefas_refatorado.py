"""
Gerenciador de Tarefas - Versão Otimizada para Vaga Junior
Demonstra boas práticas de Python moderno
"""

from pathlib import Path
from datetime import datetime, timedelta
import json
import os
from typing import List, Dict, Optional
import logging

# ============================================================================
# CONFIGURAÇÃO DE LOGGING
# ============================================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================================
# CONSTANTES
# ============================================================================

PRIORIDADES = {
    "1": "Baixa",
    "2": "Média",
    "3": "Alta"
}

ORDEM_PRIORIDADE = {
    "Alta": 3,
    "Média": 2,
    "Baixa": 1
}

CATEGORIA_PADRAO = "Pessoal"
PRAZO_PADRAO_DIAS = 7
ENCODING = "utf-8"


# ============================================================================
# CLASSE PRINCIPAL
# ============================================================================

class GerenciadorTarefas:
    """
    Sistema de gerenciamento de tarefas com persistência em JSON.
    
    Funcionalidades:
    - Adicionar, listar, editar, remover tarefas
    - Marcar como concluída
    - Filtrar por categoria ou status
    - Buscar por termo
    - Estatísticas
    
    Atributos:
        pasta: Caminho da pasta de dados
        arquivo: Caminho do arquivo JSON
        tarefas: Lista de tarefas carregadas
    """

    def __init__(self) -> None:
        """Inicializa o gerenciador e carrega tarefas existentes."""
        self.pasta = Path.home() / "tarefas_app"
        self.pasta.mkdir(exist_ok=True)
        self.arquivo = self.pasta / "tarefas.json"
        self.tarefas: List[Dict] = self._carregar()
        logger.info(f"Gerenciador iniciado com {len(self.tarefas)} tarefas")

    # ========================================================================
    # PERSISTÊNCIA
    # ========================================================================

    def _carregar(self) -> List[Dict]:
        """
        Carrega tarefas do arquivo JSON.
        
        Returns:
            List[Dict]: Lista de tarefas ou lista vazia se arquivo não existe
        """
        if not self.arquivo.exists():
            logger.info("Arquivo não existe, iniciando com lista vazia")
            return []

        try:
            with self.arquivo.open("r", encoding=ENCODING) as f:
                tarefas = json.load(f)
                logger.info(f"✅ {len(tarefas)} tarefas carregadas")
                return tarefas
        except json.JSONDecodeError:
            logger.error(f"❌ JSON inválido em {self.arquivo}")
            return []
        except IOError as e:
            logger.error(f"❌ Erro ao ler arquivo: {e}")
            return []

    def _salvar(self) -> None:
        """Salva tarefas no arquivo JSON."""
        try:
            with self.arquivo.open("w", encoding=ENCODING) as f:
                json.dump(self.tarefas, f, ensure_ascii=False, indent=2)
                logger.info(f"✅ {len(self.tarefas)} tarefas salvas")
        except IOError as e:
            logger.error(f"❌ Erro ao salvar arquivo: {e}")
            print("❌ Erro ao salvar tarefas. Tente novamente.")

    # ========================================================================
    # UTILITÁRIOS
    # ========================================================================

    def _gerar_id(self) -> int:
        """
        Gera ID único (nunca repete mesmo após remoções).
        
        Returns:
            int: Próximo ID disponível
        """
        return max((t["id"] for t in self.tarefas), default=0) + 1

    def _encontrar_tarefa(self, tarefa_id: int) -> Optional[Dict]:
        """
        Encontra uma tarefa pelo ID.
        
        Args:
            tarefa_id: ID da tarefa
            
        Returns:
            Dict ou None: Tarefa encontrada ou None
        """
        return next((t for t in self.tarefas if t["id"] == tarefa_id), None)

    def _validar_data(self, entrada: str) -> Optional[str]:
        """
        Valida e converte data para ISO format.
        
        Args:
            entrada: String de data (DD/MM/YYYY)
            
        Returns:
            str: Data em ISO format ou None se inválida
        """
        if not entrada.strip():
            return None

        try:
            return datetime.strptime(entrada.strip(), "%d/%m/%Y").isoformat()
        except ValueError:
            print("⚠️ Data inválida (use DD/MM/YYYY)")
            return None

    def _exibir_tarefa(self, tarefa: Dict) -> None:
        """
        Exibe uma tarefa formatada.
        
        Args:
            tarefa: Dicionário da tarefa
        """
        status = "✔" if tarefa["concluida"] else "•"
        venc = tarefa["vencimento"][:10] if tarefa["vencimento"] else "Sem prazo"

        print(f"\n[{tarefa['id']}] {status} {tarefa['titulo']}")
        print(f"  {tarefa['categoria']} | {tarefa['prioridade']} | {venc}")
        
        if tarefa["descricao"]:
            print(f"  Descrição: {tarefa['descricao']}")

    @staticmethod
    def _limpar_tela() -> None:
        """Limpa a tela do terminal."""
        os.system("clear" if os.name == "posix" else "cls")

    # ========================================================================
    # CRUD
    # ========================================================================

    def adicionar(self) -> None:
        """Adiciona uma nova tarefa interativamente."""
        print("\n" + "="*50)
        print("➕ ADICIONAR TAREFA")
        print("="*50)

        titulo = input("Título: ").strip()
        if not titulo:
            print("❌ Título obrigatório")
            return

        descricao = input("Descrição: ").strip()
        categoria = input("Categoria: ").strip() or CATEGORIA_PADRAO

        print("Prioridade: 1-Baixa 2-Média 3-Alta")
        prioridade = PRIORIDADES.get(
            input("Prioridade: ").strip(),
            "Média"
        )

        vencimento = self._validar_data(input("Prazo (DD/MM/YYYY): ").strip())
        if input("\nDeseja prazos em 7 dias? (s/n): ").lower() == "s" and not vencimento:
            vencimento = (datetime.now() + timedelta(days=PRAZO_PADRAO_DIAS)).isoformat()

        tarefa = {
            "id": self._gerar_id(),
            "titulo": titulo,
            "descricao": descricao,
            "categoria": categoria,
            "prioridade": prioridade,
            "concluida": False,
            "criado_em": datetime.now().isoformat(),
            "vencimento": vencimento,
        }

        self.tarefas.append(tarefa)
        self._salvar()
        print(f"\n✅ Tarefa '{titulo}' adicionada")

    def listar(self, apenas_pendentes: bool = False) -> None:
        """
        Lista tarefas com opção de filtro.
        
        Args:
            apenas_pendentes: Se True, mostra apenas tarefas não concluídas
        """
        tarefas = self.tarefas

        if apenas_pendentes:
            tarefas = [t for t in tarefas if not t["concluida"]]

        if not tarefas:
            print("\n ❌ Sem tarefas" + (" pendentes" if apenas_pendentes else ""))
            return

        # Ordenar por prioridade (Alta primeiro) e depois por data
        tarefas_ordenadas = sorted(
            tarefas,
            key=lambda t: (
                -ORDEM_PRIORIDADE.get(t["prioridade"], 0),
                t["vencimento"] or "9999"
            )
        )

        print("\n" + "="*50)
        print("📋 TAREFAS" + (" PENDENTES" if apenas_pendentes else ""))
        print("="*50)

        for tarefa in tarefas_ordenadas:
            self._exibir_tarefa(tarefa)

        print()

    def concluir(self) -> None:
        """Marca uma tarefa como concluída."""
        self.listar(apenas_pendentes=True)

        try:
            tarefa_id = int(input("ID para concluir: ").strip())
        except ValueError:
            print("❌ ID inválido")
            return

        tarefa = self._encontrar_tarefa(tarefa_id)

        if not tarefa:
            print(f"❌ Tarefa #{tarefa_id} não encontrada")
            return

        if tarefa["concluida"]:
            print("⚠️ Tarefa já estava concluída")
            return

        tarefa["concluida"] = True
        self._salvar()
        print(f"✅ Tarefa '{tarefa['titulo']}' concluída!")

    def editar(self) -> None:
        """Edita uma tarefa existente."""
        self.listar()

        try:
            tarefa_id = int(input("ID para editar: ").strip())
        except ValueError:
            print("❌ ID inválido")
            return

        tarefa = self._encontrar_tarefa(tarefa_id)

        if not tarefa:
            print(f"❌ Tarefa #{tarefa_id} não encontrada")
            return

        print(f"\nEditando: {tarefa['titulo']}")
        print("(deixe em branco para manter)\n")

        novo_titulo = input(f"Novo título: ").strip()
        if novo_titulo:
            tarefa["titulo"] = novo_titulo

        nova_descricao = input(f"Nova descrição: ").strip()
        if nova_descricao:
            tarefa["descricao"] = nova_descricao

        nova_categoria = input(f"Nova categoria: ").strip()
        if nova_categoria:
            tarefa["categoria"] = nova_categoria

        self._salvar()
        print("✅ Tarefa atualizada")

    def remover(self) -> None:
        """Remove uma tarefa com confirmação."""
        self.listar()

        try:
            tarefa_id = int(input("ID para remover: ").strip())
        except ValueError:
            print("❌ ID inválido")
            return

        tarefa = self._encontrar_tarefa(tarefa_id)

        if not tarefa:
            print(f"❌ Tarefa #{tarefa_id} não encontrada")
            return

        confirmacao = input(f"Remover '{tarefa['titulo']}'? (s/n): ").lower()
        if confirmacao != "s":
            print("❌ Cancelado")
            return

        self.tarefas = [t for t in self.tarefas if t["id"] != tarefa_id]
        self._salvar()
        print("✅ Tarefa removida")

    def buscar(self) -> None:
        """Busca tarefas por termo."""
        termo = input("Buscar por: ").lower().strip()

        if not termo:
            print("❌ Digite algo para buscar")
            return

        encontradas = [
            t for t in self.tarefas
            if termo in t["titulo"].lower() or termo in t["categoria"].lower()
        ]

        if not encontradas:
            print(f"❌ Nenhuma tarefa encontrada com '{termo}'")
            return

        print(f"\n🔍 {len(encontradas)} resultado(s)\n")
        for tarefa in encontradas:
            self._exibir_tarefa(tarefa)

    def filtrar_categoria(self) -> None:
        """Filtra tarefas por categoria."""
        categorias = sorted(set(t["categoria"] for t in self.tarefas))

        if not categorias:
            print("❌ Sem categorias cadastradas")
            return

        print("\nCategorias:")
        for i, cat in enumerate(categorias, 1):
            print(f"{i} - {cat}")

        try:
            escolha = int(input("Escolha: ").strip()) - 1
        except ValueError:
            print("❌ Entrada inválida")
            return

        if not (0 <= escolha < len(categorias)):
            print("❌ Opção inválida")
            return

        categoria = categorias[escolha]
        tarefas_cat = [t for t in self.tarefas if t["categoria"] == categoria]

        print(f"\n📁 {categoria}\n")
        for tarefa in tarefas_cat:
            self._exibir_tarefa(tarefa)

    def estatisticas(self) -> None:
        """Exibe estatísticas das tarefas."""
        if not self.tarefas:
            print("❌ Sem tarefas")
            return

        total = len(self.tarefas)
        concluidas = len([t for t in self.tarefas if t["concluida"]])
        pendentes = total - concluidas

        print("\n" + "="*50)
        print("📊 ESTATÍSTICAS")
        print("="*50)
        print(f"Total: {total}")
        print(f"Concluídas: {concluidas} ({(concluidas/total*100):.0f}%)")
        print(f"Pendentes: {pendentes} ({(pendentes/total*100):.0f}%)")

        print("\nPor prioridade:")
        for prioridade in ["Alta", "Média", "Baixa"]:
            qtd = len([t for t in self.tarefas if t["prioridade"] == prioridade])
            print(f"  {prioridade}: {qtd}")

        print("\nPor categoria:")
        for cat in sorted(set(t["categoria"] for t in self.tarefas)):
            qtd = len([t for t in self.tarefas if t["categoria"] == cat])
            print(f"  {cat}: {qtd}")

        print()

    # ========================================================================
    # MENU
    # ========================================================================

    def menu(self) -> None:
        """Exibe menu e controla a aplicação."""
        # Mapear opções para executar (mais escalável)
        acoes = {
            "1": ("Adicionar", self.adicionar),
            "2": ("Listar", self.listar),
            "3": ("Concluir", self.concluir),
            "4": ("Editar", self.editar),
            "5": ("Remover", self.remover),
            "6": ("Buscar", self.buscar),
            "7": ("Filtrar categoria", self.filtrar_categoria),
            "8": ("Estatísticas", self.estatisticas),
            "9": ("Sair", None),
        }

        while True:
            self._limpar_tela()

            print("="*50)
            print("📱 GERENCIADOR DE TAREFAS")
            print("="*50)

            for chave, (nome, _) in acoes.items():
                print(f"{chave} - {nome}")

            opcao = input("\nEscolha: ").strip()

            if opcao not in acoes:
                print("❌ Opção inválida")
                input("ENTER...")
                continue

            nome, funcao = acoes[opcao]

            if funcao is None:  # Sair
                print("\n👋 Até logo!")
                break

            try:
                funcao()
            except Exception as e:
                logger.error(f"Erro ao executar {nome}: {e}")
                print(f"❌ Erro: {e}")

            input("\nENTER para continuar...")


# ============================================================================
# EXECUÇÃO
# ============================================================================

if __name__ == "__main__":
    try:
        app = GerenciadorTarefas()
        app.menu()
    except KeyboardInterrupt:
        print("\n\n⚠️ Programa interrompido pelo usuário")
    except Exception as e:
        logger.critical(f"Erro crítico: {e}")
        print(f"❌ Erro: {e}")
