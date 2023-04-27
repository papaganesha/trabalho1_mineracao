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

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()


storesToInsert = []
storesToInput = 20

storesAdresses = pd.read_excel('./dados/clientes.xlsx', sheet_name="Plan1")

storesDf = pd.DataFrame(storesAdresses)

count = 0

# ENQUANTO COUNT FOR MENOR QUE O NUMERO DE CLIENTES A SEREM INSERIDOS
while (count < storesToInput):
    # EXTRAI LINHA DO DATAFRAME
    lin = storesDf.loc[count]
    # INSERE OS DADOS DO CLIENTE EM UM ARRAY DE OBJETOS
    storesToInsert.append(lin.ENDERECO.upper())
    # INCREMENTA CONTADOR
    count += 1

    


add_client = ("INSERT INTO LOJAS (NOME, ENDERECO) VALUES (%s, %s)")
countAdded = 0
# RODAR CLIENTES A SEREM INSERIDOS
for address in storesToInsert:
    # INSERIR NO BANCO AQUI
    try:
        cursor.execute(add_client, (address, address,))
        countAdded +=1
    except Exception as e:
        print(e)
    
    
print(f"{countAdded} novas lojas inseridos")

cnx.commit()

cursor.close()

cnx.close()
