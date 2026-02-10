"""
Gerenciador de Tarefas - Versão Profissional (Portfólio Júnior)

Sistema de gerenciamento de tarefas com persistência em JSON.

Demonstra:
✔ POO com Dataclasses
✔ Type Hints Completos
✔ Logging Profissional
✔ Persistência de Dados
✔ Clean Code
✔ Tratamento de Erros

Author: Bryan Faria Lima
License: MIT
"""

from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from typing import List, Optional
import json
import logging
import os


# =============================================================================
# CONFIGURAÇÃO DE LOGGING
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# =============================================================================
# MODELO DE DADOS
# =============================================================================

@dataclass
class Tarefa:
    """
    Representa uma tarefa com todas suas propriedades.
    
    Atributos:
        id: Identificador único da tarefa
        titulo: Título/nome da tarefa
        descricao: Descrição detalhada
        categoria: Categoria (Trabalho, Pessoal, Estudos, etc)
        prioridade: Nível de prioridade (Baixa, Média, Alta)
        concluida: Status de conclusão
        criado_em: Data/hora de criação (ISO format)
        vencimento: Data de vencimento opcional (ISO format)
    """
    id: int
    titulo: str
    descricao: str
    categoria: str
    prioridade: str
    concluida: bool
    criado_em: str
    vencimento: Optional[str]

    def to_dict(self) -> dict:
        """
        Converte objeto Tarefa para dicionário.
        
        Returns:
            dict: Dicionário com dados da tarefa
        """
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Tarefa":
        """
        Cria objeto Tarefa a partir de dicionário.
        
        Args:
            data: Dicionário com dados da tarefa
            
        Returns:
            Tarefa: Nova instância de Tarefa
        """
        return Tarefa(**data)

    def __repr__(self) -> str:
        """Representação legível da tarefa para debugging."""
        status = "✔" if self.concluida else "•"
        return f"{status} [{self.id}] {self.titulo} ({self.prioridade})"


# =============================================================================
# CONSTANTES
# =============================================================================

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
ENCODING = "utf-8"


# =============================================================================
# GERENCIADOR DE TAREFAS
# =============================================================================

class GerenciadorTarefas:
    """
    Gerenciador profissional de tarefas com persistência em JSON.
    
    Funcionalidades:
    - Adicionar, listar, editar, remover tarefas
    - Marcar tarefas como concluídas
    - Buscar e filtrar tarefas
    - Visualizar estatísticas
    - Persistência automática em JSON
    
    Atributos:
        pasta: Caminho da pasta de dados
        arquivo: Caminho do arquivo JSON com tarefas
        tarefas: Lista de tarefas carregadas em memória
    """

    def __init__(self) -> None:
        """Inicializa o gerenciador e carrega tarefas existentes."""
        self.pasta = Path.home() / "tarefas_app"
        self.pasta.mkdir(exist_ok=True)

        self.arquivo = self.pasta / "tarefas.json"
        self.tarefas: List[Tarefa] = self._carregar()
        
        logger.info(f"Gerenciador iniciado com {len(self.tarefas)} tarefas")

    # =========================================================================
    # PERSISTÊNCIA
    # =========================================================================

    def _carregar(self) -> List[Tarefa]:
        """
        Carrega tarefas do arquivo JSON.
        
        Returns:
            List[Tarefa]: Lista de tarefas ou lista vazia se arquivo não existe
        """
        if not self.arquivo.exists():
            logger.info("Arquivo não existe, iniciando com lista vazia")
            return []

        try:
            with self.arquivo.open("r", encoding=ENCODING) as f:
                dados = json.load(f)
                tarefas = [Tarefa.from_dict(t) for t in dados]
                logger.info(f"✅ {len(tarefas)} tarefas carregadas com sucesso")
                return tarefas
        except json.JSONDecodeError as e:
            logger.error(f"❌ JSON inválido em {self.arquivo}: {e}")
            return []
        except IOError as e:
            logger.error(f"❌ Erro ao ler arquivo: {e}")
            return []

    def _salvar(self) -> None:
        """
        Salva tarefas no arquivo JSON.
        
        Raises:
            IOError: Se houver erro ao salvar arquivo
        """
        try:
            with self.arquivo.open("w", encoding=ENCODING) as f:
                json.dump(
                    [t.to_dict() for t in self.tarefas],
                    f,
                    indent=2,
                    ensure_ascii=False
                )
            logger.info(f"✅ {len(self.tarefas)} tarefas salvas com sucesso")
        except IOError as e:
            logger.error(f"❌ Erro ao salvar arquivo: {e}")
            print("❌ Erro ao salvar tarefas. Tente novamente.")

    # =========================================================================
    # UTILITÁRIOS
    # =========================================================================

    def _gerar_id(self) -> int:
        """
        Gera ID único (nunca repete mesmo após remoções).
        
        Returns:
            int: Próximo ID disponível
        """
        return max((t.id for t in self.tarefas), default=0) + 1

    def _buscar(self, tarefa_id: int) -> Optional[Tarefa]:
        """
        Busca uma tarefa pelo ID.
        
        Args:
            tarefa_id: ID da tarefa a buscar
            
        Returns:
            Tarefa ou None: Tarefa encontrada ou None
        """
        return next((t for t in self.tarefas if t.id == tarefa_id), None)

    def _validar_data(self, entrada: str) -> Optional[str]:
        """
        Valida e converte data para ISO format.
        
        Args:
            entrada: String de data no formato DD/MM/YYYY
            
        Returns:
            str ou None: Data em ISO format ou None se inválida
        """
        if not entrada.strip():
            return None

        try:
            return datetime.strptime(entrada.strip(), "%d/%m/%Y").isoformat()
        except ValueError:
            print("⚠️ Data inválida (use DD/MM/YYYY)")
            logger.warning(f"Entrada de data inválida: {entrada}")
            return None

    def _exibir_tarefa(self, tarefa: Tarefa) -> None:
        """
        Exibe uma tarefa formatada no terminal.
        
        Args:
            tarefa: Tarefa a exibir
        """
        status = "✔" if tarefa.concluida else "•"
        venc = tarefa.vencimento[:10] if tarefa.vencimento else "Sem prazo"

        print(f"\n[{tarefa.id}] {status} {tarefa.titulo}")
        print(f"  {tarefa.categoria} | {tarefa.prioridade} | {venc}")

        if tarefa.descricao:
            print(f"  Descrição: {tarefa.descricao}")

    @staticmethod
    def _limpar() -> None:
        """Limpa a tela do terminal."""
        os.system("clear" if os.name == "posix" else "cls")

    # =========================================================================
    # CRUD - CREATE
    # =========================================================================

    def adicionar(self) -> None:
        """Adiciona uma nova tarefa interativamente."""
        print("\n" + "=" * 50)
        print("➕ ADICIONAR NOVA TAREFA")
        print("=" * 50)

        titulo = input("Título: ").strip()
        if not titulo:
            print("❌ Título obrigatório")
            logger.warning("Tentativa de adicionar tarefa sem título")
            return

        descricao = input("Descrição: ").strip()
        categoria = input("Categoria: ").strip() or CATEGORIA_PADRAO

        print("\nPrioridade: 1-Baixa  2-Média  3-Alta")
        prioridade = PRIORIDADES.get(
            input("Escolha: ").strip(),
            "Média"
        )

        prazo = input("Prazo (DD/MM/YYYY ou vazio): ").strip()
        vencimento = self._validar_data(prazo) if prazo else None

        tarefa = Tarefa(
            id=self._gerar_id(),
            titulo=titulo,
            descricao=descricao,
            categoria=categoria,
            prioridade=prioridade,
            concluida=False,
            criado_em=datetime.now().isoformat(),
            vencimento=vencimento
        )

        self.tarefas.append(tarefa)
        self._salvar()
        logger.info(f"Tarefa criada: {tarefa}")
        print(f"\n✅ Tarefa '{titulo}' adicionada com sucesso!")

    # =========================================================================
    # CRUD - READ
    # =========================================================================

    def listar(self, apenas_pendentes: bool = False) -> None:
        """
        Lista tarefas com opção de filtro.
        
        Args:
            apenas_pendentes: Se True, mostra apenas tarefas não concluídas
        """
        tarefas = self.tarefas

        if apenas_pendentes:
            tarefas = [t for t in tarefas if not t.concluida]

        if not tarefas:
            print(f"\n❌ Sem tarefas{' pendentes' if apenas_pendentes else ''}")
            return

        # Ordenar por prioridade (Alta primeiro) e depois por vencimento
        tarefas_ordenadas = sorted(
            tarefas,
            key=lambda t: (
                -ORDEM_PRIORIDADE.get(t.prioridade, 0),
                t.vencimento or "9999"
            )
        )

        print("\n" + "=" * 50)
        print("📋 TAREFAS" + (" PENDENTES" if apenas_pendentes else ""))
        print("=" * 50)

        for tarefa in tarefas_ordenadas:
            self._exibir_tarefa(tarefa)

        print()

    # =========================================================================
    # CRUD - UPDATE
    # =========================================================================

    def concluir(self) -> None:
        """Marca uma tarefa como concluída."""
        self.listar(apenas_pendentes=True)

        try:
            tarefa_id = int(input("ID para concluir: ").strip())
        except ValueError:
            print("❌ ID inválido")
            logger.warning("Entrada de ID inválida em concluir()")
            return

        tarefa = self._buscar(tarefa_id)

        if not tarefa:
            print(f"❌ Tarefa #{tarefa_id} não encontrada")
            return

        if tarefa.concluida:
            print("⚠️ Tarefa já estava concluída")
            return

        tarefa.concluida = True
        self._salvar()
        logger.info(f"Tarefa concluída: {tarefa}")
        print(f"✅ Tarefa '{tarefa.titulo}' marcada como concluída!")

    def editar(self) -> None:
        """Edita uma tarefa existente."""
        self.listar()

        try:
            tarefa_id = int(input("ID para editar: ").strip())
        except ValueError:
            print("❌ ID inválido")
            logger.warning("Entrada de ID inválida em editar()")
            return

        tarefa = self._buscar(tarefa_id)

        if not tarefa:
            print(f"❌ Tarefa #{tarefa_id} não encontrada")
            return

        print(f"\nEditando: {tarefa.titulo}")
        print("(deixe em branco para manter valor anterior)\n")

        novo_titulo = input("Novo título: ").strip()
        if novo_titulo:
            tarefa.titulo = novo_titulo

        nova_descricao = input("Nova descrição: ").strip()
        if nova_descricao:
            tarefa.descricao = nova_descricao

        nova_categoria = input("Nova categoria: ").strip()
        if nova_categoria:
            tarefa.categoria = nova_categoria

        self._salvar()
        logger.info(f"Tarefa editada: {tarefa}")
        print("✅ Tarefa atualizada com sucesso!")

    # =========================================================================
    # CRUD - DELETE
    # =========================================================================

    def remover(self) -> None:
        """Remove uma tarefa com confirmação."""
        self.listar()

        try:
            tarefa_id = int(input("ID para remover: ").strip())
        except ValueError:
            print("❌ ID inválido")
            logger.warning("Entrada de ID inválida em remover()")
            return

        tarefa = self._buscar(tarefa_id)

        if not tarefa:
            print(f"❌ Tarefa #{tarefa_id} não encontrada")
            return

        # Pedir confirmação antes de deletar
        confirmacao = input(f"\nTemcerteza? Remover '{tarefa.titulo}'? (s/n): ").lower()
        if confirmacao != "s":
            print("❌ Operação cancelada")
            return

        self.tarefas.remove(tarefa)
        self._salvar()
        logger.info(f"Tarefa removida: {tarefa}")
        print("✅ Tarefa removida com sucesso!")

    # =========================================================================
    # FUNCIONALIDADES EXTRAS
    # =========================================================================

    def buscar(self) -> None:
        """Busca tarefas por termo."""
        termo = input("Buscar por: ").lower().strip()

        if not termo:
            print("❌ Digite algo para buscar")
            return

        encontradas = [
            t for t in self.tarefas
            if termo in t.titulo.lower() or termo in t.categoria.lower()
        ]

        if not encontradas:
            print(f"❌ Nenhuma tarefa encontrada com '{termo}'")
            logger.info(f"Busca sem resultados: {termo}")
            return

        print(f"\n🔍 {len(encontradas)} resultado(s)")
        for tarefa in encontradas:
            self._exibir_tarefa(tarefa)

    def filtrar_categoria(self) -> None:
        """Filtra tarefas por categoria."""
        categorias = sorted(set(t.categoria for t in self.tarefas))

        if not categorias:
            print("❌ Sem categorias cadastradas")
            return

        print("\nCategorias disponíveis:")
        for i, cat in enumerate(categorias, 1):
            print(f"{i} - {cat}")

        try:
            escolha = int(input("Escolha: ").strip()) - 1
        except ValueError:
            print("❌ Entrada inválida")
            logger.warning("Entrada inválida em filtrar_categoria()")
            return

        if not (0 <= escolha < len(categorias)):
            print("❌ Opção inválida")
            return

        categoria = categorias[escolha]
        tarefas_cat = [t for t in self.tarefas if t.categoria == categoria]

        print(f"\n📁 Tarefas de '{categoria}'")
        for tarefa in tarefas_cat:
            self._exibir_tarefa(tarefa)

    def estatisticas(self) -> None:
        """Exibe estatísticas das tarefas."""
        if not self.tarefas:
            print("❌ Sem tarefas para exibir estatísticas")
            return

        total = len(self.tarefas)
        concluidas = len([t for t in self.tarefas if t.concluida])
        pendentes = total - concluidas

        print("\n" + "=" * 50)
        print("📊 ESTATÍSTICAS")
        print("=" * 50)
        print(f"Total: {total}")
        print(f"Concluídas: {concluidas} ({(concluidas/total*100):.0f}%)")
        print(f"Pendentes: {pendentes} ({(pendentes/total*100):.0f}%)")

        print("\nPor prioridade:")
        for prioridade in ["Alta", "Média", "Baixa"]:
            qtd = len([t for t in self.tarefas if t.prioridade == prioridade])
            print(f"  {prioridade}: {qtd}")

        print("\nPor categoria:")
        for cat in sorted(set(t.categoria for t in self.tarefas)):
            qtd = len([t for t in self.tarefas if t.categoria == cat])
            print(f"  {cat}: {qtd}")

        print()

    # =========================================================================
    # MENU PRINCIPAL
    # =========================================================================

    def menu(self) -> None:
        """Exibe menu interativo e controla a aplicação."""
        # Mapear opções para executar (escalável)
        acoes = {
            "1": ("Adicionar", self.adicionar),
            "2": ("Listar", self.listar),
            "3": ("Concluir", self.concluir),
            "4": ("Editar", self.editar),
            "5": ("Remover", self.remover),
            "6": ("Buscar", self.buscar),
            "7": ("Filtrar por categoria", self.filtrar_categoria),
            "8": ("Estatísticas", self.estatisticas),
            "9": ("Sair", None),
        }

        while True:
            self._limpar()

            print("=" * 50)
            print("📱 GERENCIADOR DE TAREFAS")
            print("=" * 50)

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
                logger.info("Aplicação encerrada pelo usuário")
                break

            try:
                funcao()
            except Exception as e:
                logger.error(f"Erro ao executar {nome}: {e}", exc_info=True)
                print(f"❌ Erro: {e}")

            input("\nENTER para continuar...")


# =============================================================================
# EXECUÇÃO
# =============================================================================

if __name__ == "__main__":
    try:
        app = GerenciadorTarefas()
        app.menu()
    except KeyboardInterrupt:
        print("\n\n⚠️ Programa interrompido pelo usuário")
        logger.info("Aplicação interrompida por KeyboardInterrupt")
    except Exception as e:
        logger.critical(f"Erro crítico na aplicação: {e}", exc_info=True)
        print(f"❌ Erro crítico: {e}")
