
from insert_models import insert_models
from insert_clients import insert_clients
from insert_books import insert_books
from insert_stores import insert_stores
from insert_sells import insert_sells
from delete_table_data import delete_table_data
from set_autoincrement import set_autoincrement
from drop_table import drop_table

from etl_clients import etl_clients
from etl_stores import etl_stores
from etl_books import etl_books

from datetime import datetime, time    

#DELETAR DADOS DAS TABELAS
delete_table_data("CLIENTES")
delete_table_data("LOJAS")
delete_table_data("ITENS_VENDAS")
delete_table_data("LIVROS")
delete_table_data("VENDAS")
delete_table_data("TABELA_CHAVE")
delete_table_data("MODELOS")
delete_table_data("DW_D_CLIENTES")
delete_table_data("DW_D_LOJAS")
delete_table_data("DW_D_LIVROS")


#SETAR AUTOINCREMENT = 0
set_autoincrement("CLIENTES")
set_autoincrement("LOJAS")
set_autoincrement("LIVROS")
set_autoincrement("VENDAS")
set_autoincrement("TABELA_CHAVE")
set_autoincrement("MODELOS")



#CRIAR MODELOS DE EXTRAÇAO
insert_models()

#INSERIR 300 CLIENTES
#DEFININDO NUMERO DE CLIENTES
clients_to_insert = 350
# #CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_clients(clients_to_insert)

# #INSERIR 800 LIVROS
# #DEFININDO NUMERO DE LIVROS
books_to_insert = 800
# # #CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_books(books_to_insert)

# # INSERIR 20 LOJAS
# # DEFININDO NUMERO DE LIVROS
stores_to_insert = 20
# #CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_stores(stores_to_insert)


#INSERIR 450 VENDAS FICTIAS PARA DATA CORTE X
#DEFININDO NUMERO DE VENDAS
sells_to_insert = 450
#DEFININDO DATA CORTE X
#"2023-04-30 14:01:10" 
cut_date = '2023-04-30 14:01:10'
#CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_sells(sells_to_insert, cut_date)


#INSERIR 1000 VENDAS FICTIAS PARA DATA CORTE X
#DEFININDO NUMERO DE VENDAS
sells_to_insert = 1000
#DEFININDO DATA CORTE X
#"2023-04-30 16:08:40" 
cut_date = '2023-05-30 16:08:40'
#CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_sells(sells_to_insert, cut_date)



#RELIZAR EXTRACAO DO OLTP, TRANSFORMAR DADOS RESTANTES, CARREGAR DE VOLTA NO OLTP(SIMULANDO OLAP)
# etl_clients()
# etl_stores()
# etl_books()