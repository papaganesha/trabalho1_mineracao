# INSERIR LOJAS NO BANCO DE DADOS
# CARREGAR CSV
# EXTRAIR DADOS DO CSV
# CONECTAR COM BANCO
# INSERIR LOJAS

import pandas as pd
import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'mineracao',
    'raise_on_warnings': True
}

def insert_models():
    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()

    models_to_insert = ["clientes","lojas","livros"]

    count_inserted = 0
    
    for model in models_to_insert:
        try:
            add_model = "INSERT INTO MODELOS(ASSUNTO, SERVIDOR_ORIGEM, SERVIDOR_DESTINO) VALUES(%s, 'OLTP', 'STAGE');"
            cursor.execute(add_model, (model, ))
            count_inserted +=1
        except Exception as e:
            print(e)
        
        
    print(f"{count_inserted} modelos inseridos com sucesso")

    cnx.commit()

    cursor.close()

    cnx.close()

