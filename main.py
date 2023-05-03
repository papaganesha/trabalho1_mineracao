
from insert_clients import insert_clients
from insert_books import insert_books
from insert_stores import insert_stores
from insert_sells import insert_sells

from datetime import datetime, time    

#INSERIR 300 CLIENTES
#DEFININDO NUMERO DE CLIENTES
clients_to_insert = 350
# #CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_clients(clients_to_insert)

# #INSERIR 850 LIVROS
# #DEFININDO NUMERO DE LIVROS
books_to_insert = 850
# # #CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_books(books_to_insert)

# # INSERIR 20 LOJAS
# # DEFININDO NUMERO DE LIVROS
stores_to_insert = 20
# #CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_stores(stores_to_insert)


#INSERIR 250 VENDAS FICTIAS PARA DATA CORTE X
#DEFININDO NUMERO DE VENDAS
sells_to_insert = 250
#DEFININDO DATA CORTE X
#"2023-04-30 16:08:40" 
cut_date = '2023-04-30 14:01:10'
print(cut_date)


# cut_date = now.strftime('%Y-%m-%d %H:%M:%S')

#CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_sells(sells_to_insert, cut_date)


#INSERIR 250 VENDAS FICTIAS PARA DATA CORTE X
#DEFININDO NUMERO DE VENDAS
sells_to_insert = 250
#DEFININDO DATA CORTE X
#"2023-04-30 16:08:40" 
cut_date = '2023-05-30 16:08:40'
print(cut_date)


# cut_date = now.strftime('%Y-%m-%d %H:%M:%S')

#CHAMANDO FUNCAO PASSANDO PARAMETRO 
insert_sells(sells_to_insert, cut_date)