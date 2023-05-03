# INSERIR LIVROS NO BANCO DE DADOS
# CARREGAR CSV
# EXTRAIR DADOS DO CSV
# CONECTAR COM BANCO
# INSERIR LIVROS NO BANCO

import pandas as pd
import mysql.connector
from numpy import random


config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'mineracao',
    'raise_on_warnings': True
}

def insert_books(books_nbr):
    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()

    booksToInsert = []

    books = pd.read_csv('./dados/books.csv', sep=",")

    booksDf = pd.DataFrame(books)

    count = 0

    # ENQUANTO COUNT FOR MENOR QUE O NUMERO DE LIVROS A SEREM INSERIDOS
    while (count < books_nbr):
        # EXTRAI LINHA DO DATAFRAME
        lin = booksDf.loc[count]
        #print(lin.title)

        buy_value = random.randint(19, 121)

        to_add = random.randint(19, 40)

        sell_value = buy_value + to_add
        # INSERE OS DADOS DO LIVRO EM UM ARRAY DE OBJETOS
        booksToInsert.append({
            "TITULO": lin.title,
            "VALOR_COMPRA": buy_value,
            "VALOR_VENDA": sell_value
        })
        # INCREMENTA CONTADOR
        count += 1



    add_book = ("INSERT INTO LIVROS (TITULO, VALOR_COMPRA, VALOR_VENDA) VALUES (%s, %s, %s)")
    countAdded = 0
    # RODAR LIVROS A SEREM INSERIDOS
    for book in booksToInsert:
        # INSERIR NO BANCO AQUI
        #print(book['TITULO'])
        title = book['TITULO']
        buy_value = book['VALOR_COMPRA']
        sell_value = book['VALOR_VENDA']
        data_book = (title, buy_value, sell_value)
        #print(data_book)
        try:
            cursor.execute(add_book, data_book)
        except Exception as e:
            print(e)
        
        countAdded += 1


    print(f"{countAdded} novos livros inseridos")

    cnx.commit()

    cursor.close()

    cnx.close()

