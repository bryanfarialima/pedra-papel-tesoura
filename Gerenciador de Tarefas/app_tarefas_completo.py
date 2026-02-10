from pathlib import Path
from datetime import datetime, timedelta
import json
import os

# ============================================================================
# CONFIGURAÇÃO INICIAL
# ============================================================================

class GerenciadorTarefas:
    """
    Classe que gerencia todas as operações com tarefas.
    Organiza o código em métodos bem definidos (boas práticas).
    """
    
    def __init__(self):
        # Criar pasta e arquivo de dados
        self.pasta = Path.home() / "tarefas_app"
        self.pasta.mkdir(exist_ok=True)
        self.arquivo = self.pasta / "tarefas.json"
        
        # Prioridades disponíveis
        self.prioridades = {"1": "Baixa", "2": "Média", "3": "Alta"}
        self.cores = {
            "Baixa": "\033[92m",      # Verde
            "Média": "\033[93m",      # Amarelo
            "Alta": "\033[91m",       # Vermelho
            "reset": "\033[0m"        # Normal
        }
        
        # Carregar tarefas existentes
        self.tarefas = self.carregar_tarefas()
    
    # ========================================================================
    # MÉTODOS DE ARQUIVO (Persistência)
    # ========================================================================
    
    def carregar_tarefas(self):
        """Carrega tarefas do arquivo JSON"""
        if self.arquivo.exists():
            try:
                with open(self.arquivo, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def salvar_tarefas(self):
        """Salva tarefas no arquivo JSON"""
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.tarefas, f, ensure_ascii=False, indent=2)
    
    # ========================================================================
    # MÉTODOS DE OPERAÇÕES (CRUD)
    # ========================================================================
    
    def adicionar_tarefa(self):
        """Adiciona uma nova tarefa com todos os detalhes"""
        print("\n" + "="*60)
        print("📝 ADICIONAR NOVA TAREFA")
        print("="*60)
        
        # Título da tarefa
        titulo = input("Título da tarefa: ").strip()
        if not titulo:
            print("❌ Título não pode ser vazio!")
            return
        
        # Descrição (opcional)
        descricao = input("Descrição (opcional): ").strip()
        
        # Categoria
        print("\nCategorias disponíveis: Trabalho, Pessoal, Estudos, Saúde, Compras")
        categoria = input("Categoria: ").strip() or "Pessoal"
        
        # Prioridade
        print("\nNível de prioridade:")
        for key, value in self.prioridades.items():
            print(f"  {key} - {value}")
        prioridade = self.prioridades.get(input("Escolha (1/2/3): ").strip(), "Média")
        
        # Data de vencimento
        print("\nData de vencimento (formato: DD/MM/YYYY ou deixe em branco)")
        data_input = input("Data: ").strip()
        if data_input:
            try:
                data_vencimento = datetime.strptime(data_input, "%d/%m/%Y").strftime("%d/%m/%Y")
            except ValueError:
                print("⚠️  Data inválida! Usando prazo de 7 dias.")
                data_vencimento = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
        else:
            data_vencimento = None
        
        # Criar tarefa com ID único
        tarefa = {
            "id": len(self.tarefas) + 1,
            "titulo": titulo,
            "descricao": descricao,
            "categoria": categoria,
            "prioridade": prioridade,
            "concluida": False,
            "data_vencimento": data_vencimento,
            "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        
        self.tarefas.append(tarefa)
        self.salvar_tarefas()
        print(f"\n✅ Tarefa '{titulo}' adicionada com sucesso!")
    
    def listar_tarefas(self, filtro=None):
        """
        Lista tarefas com opções de filtro.
        filtro pode ser: 'pendentes', 'concluidas', 'categoria', 'prioridade'
        """
        if not self.tarefas:
            print("\n❌ Nenhuma tarefa cadastrada.")
            return
        
        tarefas_filtradas = self.tarefas.copy()
        
        # Aplicar filtros
        if filtro == "pendentes":
            tarefas_filtradas = [t for t in tarefas_filtradas if not t["concluida"]]
        elif filtro == "concluidas":
            tarefas_filtradas = [t for t in tarefas_filtradas if t["concluida"]]
        
        # Ordenar por prioridade (Alta > Média > Baixa) e depois por ID
        ordem_prioridade = {"Alta": 3, "Média": 2, "Baixa": 1}
        tarefas_filtradas.sort(
            key=lambda x: (-ordem_prioridade.get(x["prioridade"], 0), x["id"])
        )
        
        if not tarefas_filtradas:
            print("\n❌ Nenhuma tarefa encontrada com este filtro.")
            return
        
        print("\n" + "="*80)
        print("📋 TAREFAS")
        print("="*80)
        
        for tarefa in tarefas_filtradas:
            self._exibir_tarefa(tarefa)
    
    def _exibir_tarefa(self, tarefa):
        """Exibe uma tarefa formatada com cores"""
        status = "✅" if tarefa["concluida"] else "⭕"
        cor = self.cores[tarefa["prioridade"]]
        reset = self.cores["reset"]
        
        # Adicional: mostrar alerta se vencida
        alerta = ""
        if tarefa["data_vencimento"] and not tarefa["concluida"]:
            data_venc = datetime.strptime(tarefa["data_vencimento"], "%d/%m/%Y")
            if data_venc < datetime.now():
                alerta = " ⚠️ VENCIDA"
            elif (data_venc - datetime.now()).days <= 3:
                alerta = " ⚠️ PRÓXIMO VENCIMENTO"
        
        print(f"\n{status} [{tarefa['id']}] {tarefa['titulo']}{alerta}")
        print(f"   {cor}Prioridade: {tarefa['prioridade']}{reset} | Categoria: {tarefa['categoria']}")
        
        if tarefa["descricao"]:
            print(f"   Descrição: {tarefa['descricao']}")
        
        if tarefa["data_vencimento"]:
            print(f"   Vencimento: {tarefa['data_vencimento']}")
        
        print(f"   Criada em: {tarefa['data_criacao']}")
    
    def marcar_concluida(self):
        """Marca uma tarefa como concluída"""
        if not self.tarefas:
            print("\n❌ Nenhuma tarefa para marcar.")
            return
        
        self.listar_tarefas("pendentes")
        
        try:
            tarefa_id = int(input("\nID da tarefa a marcar como concluída: "))
            tarefa = next((t for t in self.tarefas if t["id"] == tarefa_id), None)
            
            if tarefa:
                tarefa["concluida"] = True
                self.salvar_tarefas()
                print(f"\n✅ Tarefa '{tarefa['titulo']}' marcada como concluída!")
            else:
                print("\n❌ Tarefa não encontrada.")
        except ValueError:
            print("\n❌ ID inválido!")
    
    def editar_tarefa(self):
        """Edita uma tarefa existente"""
        if not self.tarefas:
            print("\n❌ Nenhuma tarefa para editar.")
            return
        
        self.listar_tarefas()
        
        try:
            tarefa_id = int(input("\nID da tarefa a editar: "))
            tarefa = next((t for t in self.tarefas if t["id"] == tarefa_id), None)
            
            if not tarefa:
                print("\n❌ Tarefa não encontrada.")
                return
            
            print(f"\nEditando: {tarefa['titulo']}")
            print("Deixe em branco para manter o valor atual.\n")
            
            # Editar campo por campo
            novo_titulo = input(f"Novo título ({tarefa['titulo']}): ").strip()
            if novo_titulo:
                tarefa["titulo"] = novo_titulo
            
            nova_descricao = input(f"Nova descrição ({tarefa['descricao'] or 'vazia'}): ").strip()
            if nova_descricao:
                tarefa["descricao"] = nova_descricao
            
            nova_categoria = input(f"Nova categoria ({tarefa['categoria']}): ").strip()
            if nova_categoria:
                tarefa["categoria"] = nova_categoria
            
            print("\nNível de prioridade: 1-Baixa, 2-Média, 3-Alta")
            nova_prioridade = input(f"Nova prioridade ({tarefa['prioridade']}): ").strip()
            if nova_prioridade in self.prioridades:
                tarefa["prioridade"] = self.prioridades[nova_prioridade]
            
            self.salvar_tarefas()
            print(f"\n✅ Tarefa atualizada com sucesso!")
        except ValueError:
            print("\n❌ ID inválido!")
    
    def remover_tarefa(self):
        """Remove uma tarefa"""
        if not self.tarefas:
            print("\n❌ Nenhuma tarefa para remover.")
            return
        
        self.listar_tarefas()
        
        try:
            tarefa_id = int(input("\nID da tarefa a remover: "))
            tarefa = next((t for t in self.tarefas if t["id"] == tarefa_id), None)
            
            if tarefa:
                confirmacao = input(f"Tem certeza que quer remover '{tarefa['titulo']}'? (s/n): ")
                if confirmacao.lower() == "s":
                    self.tarefas.remove(tarefa)
                    self.salvar_tarefas()
                    print(f"\n✅ Tarefa removida!")
                else:
                    print("\n❌ Operação cancelada.")
            else:
                print("\n❌ Tarefa não encontrada.")
        except ValueError:
            print("\n❌ ID inválido!")
    
    def limpar_concluidas(self):
        """Remove todas as tarefas concluídas"""
        concluidas = [t for t in self.tarefas if t["concluida"]]
        
        if not concluidas:
            print("\n✅ Nenhuma tarefa concluída para limpar.")
            return
        
        print(f"\n🧹 Encontradas {len(concluidas)} tarefa(s) concluída(s).")
        confirmacao = input("Deseja remover todas? (s/n): ")
        
        if confirmacao.lower() == "s":
            self.tarefas = [t for t in self.tarefas if not t["concluida"]]
            self.salvar_tarefas()
            print(f"\n✅ {len(concluidas)} tarefa(s) removida(s)!")
        else:
            print("\n❌ Operação cancelada.")
    
    def buscar_tarefas(self):
        """Busca tarefas por palavra-chave"""
        if not self.tarefas:
            print("\n❌ Nenhuma tarefa para buscar.")
            return
        
        termo = input("\nBuscar por (título ou categoria): ").lower().strip()
        
        encontradas = [
            t for t in self.tarefas
            if termo in t["titulo"].lower() or termo in t["categoria"].lower()
        ]
        
        if not encontradas:
            print(f"\n❌ Nenhuma tarefa encontrada com '{termo}'.")
            return
        
        print(f"\n🔍 {len(encontradas)} tarefa(s) encontrada(s):")
        for tarefa in encontradas:
            self._exibir_tarefa(tarefa)
    
    def filtrar_por_categoria(self):
        """Filtra tarefas por categoria"""
        if not self.tarefas:
            print("\n❌ Nenhuma tarefa para filtrar.")
            return
        
        # Obter categorias únicas
        categorias = sorted(set(t["categoria"] for t in self.tarefas))
        
        print("\nCategorias disponíveis:")
        for i, cat in enumerate(categorias, 1):
            print(f"  {i} - {cat}")
        
        try:
            escolha = int(input("Escolha uma categoria: ")) - 1
            if 0 <= escolha < len(categorias):
                categoria = categorias[escolha]
                tarefas_cat = [t for t in self.tarefas if t["categoria"] == categoria]
                
                print(f"\n📁 Tarefas da categoria '{categoria}':")
                for tarefa in tarefas_cat:
                    self._exibir_tarefa(tarefa)
            else:
                print("\n❌ Opção inválida!")
        except ValueError:
            print("\n❌ Entrada inválida!")
    
    def estatisticas(self):
        """Exibe estatísticas das tarefas"""
        if not self.tarefas:
            print("\n❌ Nenhuma tarefa cadastrada.")
            return
        
        total = len(self.tarefas)
        concluidas = len([t for t in self.tarefas if t["concluida"]])
        pendentes = total - concluidas
        
        print("\n" + "="*60)
        print("📊 ESTATÍSTICAS")
        print("="*60)
        print(f"Total de tarefas: {total}")
        print(f"Concluídas: {concluidas} ({(concluidas/total*100):.0f}%)")
        print(f"Pendentes: {pendentes} ({(pendentes/total*100):.0f}%)")
        
        # Por prioridade
        print("\nPor prioridade:")
        for prioridade in ["Alta", "Média", "Baixa"]:
            qtd = len([t for t in self.tarefas if t["prioridade"] == prioridade])
            print(f"  {prioridade}: {qtd}")
        
        # Por categoria
        print("\nPor categoria:")
        categorias = set(t["categoria"] for t in self.tarefas)
        for categoria in sorted(categorias):
            qtd = len([t for t in self.tarefas if t["categoria"] == categoria])
            print(f"  {categoria}: {qtd}")
    
    # ========================================================================
    # MENU PRINCIPAL
    # ========================================================================
    
    def menu_principal(self):
        """Exibe o menu principal e aguarda entrada do usuário"""
        while True:
            self._limpar_tela()
            print("\n" + "="*60)
            print("📱 GERENCIADOR DE TAREFAS - VERSÃO COMPLETA")
            print("="*60)
            print("\n1  - ➕ Adicionar tarefa")
            print("2  - 📋 Listar todas as tarefas")
            print("3  - ✅ Marcar tarefa como concluída")
            print("4  - ✏️  Editar tarefa")
            print("5  - ❌ Remover tarefa")
            print("6  - 🔍 Buscar tarefa")
            print("7  - 📁 Filtrar por categoria")
            print("8  - 🧹 Limpar tarefas concluídas")
            print("9  - 📊 Ver estatísticas")
            print("10 - 🚪 Sair")
            print("\n" + "="*60)
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.adicionar_tarefa()
            elif opcao == "2":
                self.listar_tarefas()
            elif opcao == "3":
                self.marcar_concluida()
            elif opcao == "4":
                self.editar_tarefa()
            elif opcao == "5":
                self.remover_tarefa()
            elif opcao == "6":
                self.buscar_tarefas()
            elif opcao == "7":
                self.filtrar_por_categoria()
            elif opcao == "8":
                self.limpar_concluidas()
            elif opcao == "9":
                self.estatisticas()
            elif opcao == "10":
                print("\n👋 Até logo!")
                break
            else:
                print("\n❌ Opção inválida!")
            
            input("\nPressione ENTER para continuar...")
    
    @staticmethod
    def _limpar_tela():
        """Limpa a tela do terminal"""
        os.system("clear" if os.name == "posix" else "cls")


# ============================================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================================

if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()
    gerenciador.menu_principal()
