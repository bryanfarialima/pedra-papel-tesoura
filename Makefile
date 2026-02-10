.PHONY: help install test lint format coverage clean dev-setup check

help:
	@echo "📚 Comandos disponíveis:"
	@echo ""
	@echo "  make install      - Instala dependências"
	@echo "  make dev-setup    - Setup completo para desenvolvimento"
	@echo "  make test         - Executa testes (pytest)"
	@echo "  make unittest     - Executa testes (unittest)"
	@echo "  make lint         - Verifica com flake8"
	@echo "  make black-check  - Verifica formatação Black"
	@echo "  make format       - Formata código com Black"
	@echo "  make coverage     - Gera relatório de cobertura"
	@echo "  make check        - Executa lint + test + coverage"
	@echo "  make play         - Inicia o jogo"
	@echo "  make clean        - Remove arquivos gerados"

install:
	pip install -e .

dev-setup:
	pip install -e ".[dev]"
	@echo "✅ Ambinte de desenvolvimento pronto!"

test:
	pytest Pedra_Papel_Tesoura/tests/ -v

unittest:
	python3 -m unittest discover -s Pedra_Papel_Tesoura/tests -p "test_*.py" -v

lint:
	flake8 Pedra_Papel_Tesoura/ --count --statistics

black-check:
	black --check --diff Pedra_Papel_Tesoura/

format:
	black Pedra_Papel_Tesoura/
	isort Pedra_Papel_Tesoura/

coverage:
	pytest Pedra_Papel_Tesoura/tests/ --cov=Pedra_Papel_Tesoura --cov-report=term-missing --cov-report=html
	@echo "📊 Relatório em htmlcov/index.html"

check: lint test coverage
	@echo "✅ Todas as verificações passaram!"

play:
	python3 Pedra_Papel_Tesoura/jogo_pedra_papel_tesoura.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov *.egg-info dist build .mypy_cache
	@echo "🧹 Limpeza concluída!"
