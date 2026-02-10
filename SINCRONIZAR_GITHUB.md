# 🔐 Instruções para Sincronizar com GitHub

## ❌ Problema Encontrado

O Personal Access Token (PAT) atual **não possui o escopo `workflow`** necessário para fazer push de arquivos `.github/workflows/`.

**O que foi sincronizado:**
- ✅ 50+ arquivos já no GitHub
- ✅ Testes expandidos
- ✅ Configuração profissional
- ❌ Workflow GitHub Actions (bloqueado por permissões)

---

## ✅ Solução: Gerar Novo Token com Escopo Workflow

### Passo 1: Criar Novo Personal Access Token

1. Acesse: https://github.com/settings/tokens/new
2. Ou em: Configurações GitHub → Developer settings → Personal access tokens → Tokens (classic)

### Passo 2: Configurar Permissões

**Marque os seguintes escopos:**

```
✅ repo                    (Acesso completo a repositórios)
   ├─ repo:status
   ├─ repo_deployment
   └─ public_repo

✅ workflow                (Criar/atualizar workflows)

✅ admin:repo_hook        (Webhooks)

✅ gist                    (Gerenciar gists)

✅ read:user              (Ler dados de usuário)
```

**IMPORTANTE:** Certifique-se de que `workflow` está marcado! ⚠️

### Passo 3: Copiar Token

- Clique em "Generate token"
- **Copie o token gerado imediatamente** (não será mostrado novamente)

### Passo 4: Configurar Git Credentials

No terminal, execute:

```bash
cd "/Users/bryanfarialima/Documents/Python Projetos"

# Ativar osxkeychain para armazenar credenciais
git config --global credential.helper osxkeychain

# Tentar fazer push (será pedido autenticação)
git push origin main
```

**Will prompt:**
```
Username for 'https://github.com': bryanfarialima
Password for 'https://bryanfarialima@github.com':
```

**Cole o novo token no campo PIN:**
- Não é a senha do GitHub
- É o token que você copiou no Passo 3

### Passo 5: Verificar Push

Se bem-sucedido, verá:

```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 1.18 KiB | 1.18 MiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), reused pack 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/bryanfarialima/pedra-papel-tesoura.git
   f704261..22809dd  main -> main
```

---

## 🔄 Commits Pendentes para Push

Estes commits estão no seu repositório local mas ainda **não foram pushados:**

```
22809dd feat: restore GitHub Actions workflow with proper permissions
```

**O que contém:**
- ✅ Workflow GitHub Actions completo
- ✅ Testes em multi-OS (Linux, macOS, Windows)
- ✅ Testes em multi-Python (3.9, 3.10, 3.11, 3.12)
- ✅ Black + Flake8 + Pytest + Coverage
- ✅ Upload automático para Codecov

---

## 📋 Alternativa: Usar GitHub Web UI (Sem Token)

Se preferir não mexer com tokens, você pode:

1. Acesse seu repositório no GitHub
2. Vá ao diretório `.github/workflows/`
3. Clique em "Add file" → "Create new file"
4. Nomeie: `python-app.yml`
5. Cole o conteúdo do seu arquivo local
6. Faça commit direto pela web

---

## 🆘 Se Ainda Houver Problemas

### Problema: "Invalid username or password"

- Certifique-se de usar o **token** (começando com `ghp_...`), não a senha do GitHub

### Problema: "Token expired"

- Acesse https://github.com/settings/tokens
- Gere um novo token com as mesmas permissões

### Problema: Osxkeychain não encontrado

```bash
# No macOS, reinstale:
brew install git
```

---

## 📊 Status Atual (Local)

| Item | Status | Arquivo |
|------|--------|---------|
| Workflow CI/CD | ✅ Pronto | `.github/workflows/python-app.yml` |
| Testes (46+) | ✅ Pronto | `Pedra_Papel_Tesoura/tests/test_game.py` |
| pyproject.toml | ✅ Pronto | `pyproject.toml` |
| README atualizado | ✅ Pronto | `Pedra_Papel_Tesoura/README.md` |
| Black + Flake8 | ✅ Pronto | `.flake8` |
| Makefile | ✅ Pronto | `Makefile` |
| Quality Check | ✅ Pronto | `quality-check.sh` |
| **Para Push** | ⏳ Aguardando | **Token com escopo workflow** |

---

## 🚀 Próximo Passo

Assim que você:
1. Gerar novo token com `workflow` scope
2. Fazer push no terminal

Toda a configuração profissional estará online e o GitHub Actions começará a rodar automaticamente em cada push! 🎉

**Tempo estimado:** 3 minutos

---

**Data:** 10 de fevereiro de 2026
**Local:** `/Users/bryanfarialima/Documents/Python Projetos`
