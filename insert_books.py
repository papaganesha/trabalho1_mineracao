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


    books = pd.read_csv('./dados/books.csv', sep=",")

    booksDf = pd.DataFrame(books)

    booksDf.dropna(inplace=True)

    count = 0
    countAdded = 0

    # ENQUANTO COUNT FOR MENOR QUE O NUMERO DE LIVROS A SEREM INSERIDOS
    while (count < books_nbr):
        # EXTRAI LINHA DO DATAFRAME
        lin = booksDf.iloc[count]
        #print(lin.title)

        buy_value = random.randint(19, 121)

        to_add = random.randint(19, 40)

        sell_value = buy_value + to_add


        add_book = ("INSERT INTO LIVROS (TITULO, CATEGORIA, VALOR_COMPRA, VALOR_VENDA) VALUES (%s, %s, %s, %s)")

        # INSERIR NO BANCO AQUI
        title = lin.title
        gender = lin.gender
        buy_value = buy_value
        sell_value = sell_value
        data_book = (title, gender, buy_value, sell_value)
        #print(data_book)
        try:
            cursor.execute(add_book, data_book)

        except Exception as e:
            print(e)
            countAdded -= 1
            
        countAdded += 1        

        count +=1

    print(f"{countAdded} novos livros inseridos")

    cnx.commit()

    cursor.close()

    cnx.close()


