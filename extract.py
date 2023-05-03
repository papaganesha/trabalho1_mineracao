# DATA CORTE 30/04/2023
# CORTE A CADA 2 HORAS
# CRIAR ROTINAS

import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'mineracao',
    'raise_on_warnings': True
}

start_date = '2023-04-30 14:00:00'

last_cut = ""

# input_to_cancel = 1

# count = 0
# while input_to_cancel != 0:
#     input_to_cancel = input("Cancel ETL? 1 for cancel 0 for continue: ")
#     print(count)
#     count +=1

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()

#PEGA OS IDS E NOMES DE TODOS OS CLIENTES COM CARGA 0
get_from_clients = "SELECT A.ID_CLIENTE, A.NOME FROM CLIENTES A, TABELA_CHAVE B WHERE B.ID = A.ID_CLIENTE AND B.TABELA = 'CLIENTES' AND CARGA = 0 LIMIT 5;"

# EXECUTANDO QUERY
cursor.execute(get_from_clients)
# PEGANDO RESULTADOS DA QUERY
result = cursor.fetchall()

print(result)


#PEGA OS IDS, TITULOS, VALOR_COMPRA, VALOR_VENDA DE TODOS OS LIVROS COM CARGA 0
get_from_books = "SELECT A.ID_LIVRO, A.TITULO, A.VALOR_COMPRA, VALOR_VENDA FROM LIVROS A, TABELA_CHAVE B WHERE B.ID = A.ID_LIVRO AND B.TABELA = 'LIVROS' AND CARGA = 0 LIMIT 5;"

# EXECUTANDO QUERY
cursor.execute(get_from_books)
# PEGANDO RESULTADOS DA QUERY
result = cursor.fetchall()

print(result)


#PEGA OS IDS, TITULOS, VALOR_COMPRA, VALOR_VENDA DE TODOS OS LIVROS COM CARGA 0
get_from_sales = "SELECT * FROM VENDAS A WHERE A.DATA_CORTE > %s LIMIT 5;"

# EXECUTANDO QUERY
cursor.execute(get_from_sales, (start_date, ))
# PEGANDO RESULTADOS DA QUERY
result = cursor.fetchall()

print(result)


#PEGA OS IDS, ID_LIVRO, TITULO LIVRO, VALOR_COMPRA, VALOR_VENDA DE TODOS OS ITENS VENDA DE DATA_CORTE MAIOR QUE E MENOR QUE
get_from_sales = "SELECT A.ID_VENDA, A.ID_LIVRO, C.TITULO, B.VALOR FROM ITENS_VENDAS A, VENDAS B, LIVROS C WHERE A.ID_VENDA = B.ID_VENDA AND B.DATA_CORTE > %s AND A.ID_LIVRO = C.ID_LIVRO LIMIT 5;"

# EXECUTANDO QUERY
cursor.execute(get_from_sales, (start_date, ))
# PEGANDO RESULTADOS DA QUERY
result = cursor.fetchall()

print(result)


cursor.close()

cnx.commit()

cnx.close()
