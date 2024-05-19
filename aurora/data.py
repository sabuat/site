import gspread 
from pathlib import Path

#-- Google Spreadsheet -------------------------------------------------------------------------------

# Configuração do caminho para o arquivo Json do google spreadsheets
# Está sendo usada a biblioteca pathlib para permitir compatibilidade em diversos SO
file_path = Path('../') / 'site-aurora.json'

gc = gspread.service_account("site-aurora.json")
db = gc.open('loja-online')

Top4 = db.get_worksheet(0)
Contatos = db.get_worksheet(1)
Blog = db.get_worksheet(2)

prod_mais_vendidos = Top4.get_all_records()
post_blog = Blog.get_all_records()

vac = {}

i = 1

while i < len(prod_mais_vendidos):
    for item in prod_mais_vendidos:
        vac[i] = item
        i = i +1
    
vacuo = vac

vac2 = {}

i = 1

while i < len(post_blog):
    for item in post_blog:
        vac2[i] = item
        i = i +1
    
blog = vac2

varios = [vacuo, blog]