from playwright.sync_api import sync_playwright
import openpyxl

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # Abrir o site
    page.goto('https://produtos-devaprender.netlify.app/')
    # Obter todas as linhas
    cards = page.get_by_role('article').all()
    produtos = []
    for produto in cards:
        nome = produto.get_by_role('heading').inner_text()
        preco = produto.locator('.price').inner_text()
        descricao = produto.locator('p').inner_text()
        produtos.append([nome, preco, descricao])

    browser.close()

# Salvar em uma planilha
planilha = openpyxl.Workbook()
pagina_inicial = planilha.active

pagina_inicial.append(['Nome','Preço','Descrição'])

for produto in produtos:
    pagina_inicial.append(produto)

planilha.save('produtos.xlsx')

