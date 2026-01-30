# 🛒 Web Scraping de Produtos com Playwright e Excel

Este projeto realiza a coleta automatizada de dados de produtos em um site de testes utilizando **Playwright** e exporta as informações para uma planilha Excel com **OpenPyXL**.

O script acessa a página, extrai o **nome**, **preço** e **descrição** de cada produto disponível e salva os dados em um arquivo `.xlsx`.

---

## 🚀 Funcionalidades

- Navegação automatizada em página web
- Extração de múltiplos produtos
- Coleta de:
  - Nome do produto
  - Preço
  - Descrição
- Geração automática de planilha Excel

---

## 🧰 Tecnologias Utilizadas

- **Python**
- **Playwright**
- **OpenPyXL**

---

## 📦 Dependências

Instale as dependências necessárias com:

```bash
pip install playwright openpyxl
Após isso, instale os navegadores do Playwright:

playwright install

📁 Saída do Projeto

O script gera automaticamente o arquivo:

produtos.xlsx


Contendo os dados extraídos do site monitorado.

📌 Observações

Projeto desenvolvido com foco educacional e demonstrativo.

O site utilizado é um ambiente de testes.

Ideal para demonstrar conceitos de web scraping, automação e exportação de dados.
