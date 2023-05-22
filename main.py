
from insert_models import insert_models
from insert_clients import insert_clients
from insert_books import insert_books
from insert_stores import insert_stores
from insert_sells import insert_sells
from delete_table_data import delete_table_data
from set_autoincrement import set_autoincrement

from numpy import random


# DELETAR DADOS DAS TABELAS
to_delete  = ["CLIENTES" ,"LOJAS", "ITENS_VENDAS", "LIVROS","VENDAS", "TABELA_CHAVE", "MODELOS", "DW_D_CLIENTES", "DW_D_LOJAS", "DW_D_LIVROS", "DW_F_VENDAS", 'ETL_CONTROLE']
for table_name in to_delete:
    delete_table_data(table_name)



# SETAR AUTOINCREMENT = 0
to_set_autoincrement = ["CLIENTES", "LOJAS", "LIVROS", "VENDAS", "TABELA_CHAVE", "MODELOS", 'ETL_CONTROLE']
for table_name in to_set_autoincrement:
    set_autoincrement(table_name)


# CRIAR MODELOS DE EXTRAÇAO
insert_models()

# INSERIR 300 CLIENTES
# DEFININDO NUMERO DE CLIENTES
clients_to_insert = 350
# CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_clients(clients_to_insert)

# INSERIR 1200 LIVROS
# DEFININDO NUMERO DE LIVROS
books_to_insert = 1200
# CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_books(books_to_insert)

# INSERIR 20 LOJAS
# DEFININDO NUMERO DE LIVROS
stores_to_insert = 20
# CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_stores(stores_to_insert)


# INSERIR ENTRE 500 E 2000 VENDAS FICTIAS PARA DATA VENDA X
sell_dates = ['2023-04-15 16:40:00', '2023-05-18 16:45:40', '2023-05-20 16:55:00', '2023-04-23 16:40:00', '2023-04-30 16:40:00']
total_inserted_sells = 0
for sell_date in sell_dates:
    sells_to_insert = random.randint(500, 2001)
    total_inserted_sells += sells_to_insert
    insert_sells(sells_to_insert, sell_date)

print(f"Total de vendas inseridas: {total_inserted_sells}")

# REALIZAR EXTRACAO DO OLTP, TRANSFORMAR DADOS RESTANTES, CARREGAR DE VOLTA NO OLTP(SIMULANDO OLAP)
# RODAR ARQUIVO SCHEDULER
