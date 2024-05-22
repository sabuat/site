import gspread 
from pathlib import Path

#-- Google Spreadsheet -------------------------------------------------------------------------------

# Configuração do caminho para o arquivo Json do google spreadsheets
# Está sendo usada a biblioteca pathlib para permitir compatibilidade em diversos SO
# file_path = Path('../') / 'site-aurora.json'

gc = gspread.service_account("site-aurora.json")
db = gc.open('loja-online')

Top4 = db.get_worksheet(0)
Contatos = db.get_worksheet(1)
Blog = db.get_worksheet(2)
Post = db.get_worksheet(3)
Produtos = db.get_worksheet(4)

prod_mais_vendidos = Top4.get_all_records()
post = Blog.get_all_records()
post_comp = Post.get_all_records()
prod_loja = Produtos.get_all_records()

# Diccionario dos Produtos mais vendidos
vac = {}
 
i = 1

while i < len(prod_mais_vendidos):
    for item in prod_mais_vendidos:
        vac[i] = item
        i = i +1
    
vacuo = vac

# Diccionario dos ultimos post
vac2 = {}

i = 1

while i < len(post):
    for item in post:
        vac2[i] = item
        i = i +1
    
blog = vac2

# Diccionario de todos os post
vac3 = {}

i = 1

while i < len(post_comp):
    for item in post_comp:
        vac3[i] = item
        i = i +1
    
post = vac3

# Diccionario de todos os produtos
vac4 = {}

i = 1

while i < len(prod_loja):
    for item in prod_loja:
        vac4[i] = item
        i = i +1
    
prods = vac4

varios = [vacuo, blog, post, prods]