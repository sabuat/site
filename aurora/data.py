import gspread 
from pathlib import Path

#-- Google Spreadsheet -------------------------------------------------------------------------------

# Configuração do caminho para o arquivo Json do google spreadsheets
# Está sendo usada a biblioteca pathlib para permitir compatibilidade em diversos SO
# file_path = Path('../') / 'site-aurora.json'

gc = gspread.service_account("site-aurora.json")
db = gc.open('loja-online')

Produtos = db.get_worksheet(0)
Contatos = db.get_worksheet(1)

fonte = {
    "codigo" : Produtos.acell("A2").value,
    "imagem" : Produtos.acell("B2").value,
    "nome": Produtos.acell("C2").value,
    "preco": Produtos.acell("D2").value,
}