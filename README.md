# 🍎 Donation Manager (Gestor de Doações de Alimentos)

> **Link do Repositório:** [https://github.com/joaowictorr/donations-manager](https://github.com/joaowictorr/donations-manager)

[![Python CI](https://github.com/joaowictorr/donations-manager/actions/workflows/ci.yml/badge.svg)](https://github.com/joaowictorr/donations-manager/actions)
![Version](https://img.shields.io/badge/version-1.0.0-orange)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Descrição do Problema Real
Bancos de alimentos e ONGs enfrentam um desafio logístico crítico: o **desperdício de alimentos por vencimento**. Devido ao alto volume de doações e à gestão muitas vezes manual, itens perecíveis acabam "esquecidos" no fundo do estoque, perdendo a validade antes de chegarem às famílias que precisam.

## 💡 Proposta da Solução
O **Donation Manager** é uma aplicação de linha de comando (CLI) projetada para digitalizar o controle de entrada e saída de mantimentos. A solução foca na **prevenção do desperdício**, utilizando uma lógica de monitoramento que identifica automaticamente produtos próximos ao vencimento e os sinaliza como prioridade máxima para distribuição.

## 👥 Público-alvo
- Gestores de bancos de alimentos e ONGs.
- Voluntários em cozinhas comunitárias.
- Administradores de pequenos centros de distribuição de donativos.

## 🚀 Funcionalidades Principais
- **Registro de Doações:** Cadastro com validação de quantidade mínima e data de validade.
- **Inventário Digital:** Visualização completa e organizada do estoque atual.
- **Sistema de Alerta Prioritário:** Listagem automática de itens que vencem nos próximos 7 dias.
- **Persistência de Dados:** Armazenamento automático em arquivo JSON para garantir que os dados não sejam perdidos ao fechar o programa.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Testes Automatizados:** Pytest (Garantia de integridade das regras de negócio).
- **Análise Estática (Linting):** Flake8 (Conformidade com os padrões PEP8).
- **CI (Integração Contínua):** GitHub Actions (Validação automática de código a cada push).

## 📦 Instruções de Instalação
1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/joaowictorr/donations-manager.git](https://github.com/joaowictorr/donations-manager.git)
   cd donations-manager

2. **Configurar o Ambiente Virtual (Recomendado)**
O ambiente virtual isola as dependências do projeto para evitar conflitos:

```bash
python -m venv venv

.\venv\Scripts\activate

source venv/bin/activate
```

3. **Instalar Dependências**
Com o ambiente ativo, instale os pacotes necessários:

```bash
pip install -r requirements.txt
```
4. **Rodar a Aplicação**
Para iniciar o sistema de gestão, execute o comando abaixo na raiz do projeto:

```bash
python -m src.main
