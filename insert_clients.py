# INSERIR CLIENTES NO BANCO DE DADOS
# CARREGAR CSV
# EXTRAIR DADOS DO CSV
# CONECTAR COM BANCO
# INSERIR CLIENTES

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


clientsToInsert = []
clientsToInput = 350

clients = pd.read_excel('./dados/clientes.xlsx', sheet_name="Plan1")

clientsDf = pd.DataFrame(clients)

count = 0

# ENQUANTO COUNT FOR MENOR QUE O NUMERO DE CLIENTES A SEREM INSERIDOS
while (count < clientsToInput):
    # EXTRAI LINHA DO DATAFRAME
    lin = clientsDf.loc[count]
    print(lin.NOME, lin.ENDERECO.upper())
    # INSERE OS DADOS DO CLIENTE EM UM ARRAY DE OBJETOS
    clientsToInsert.append({
        "NOME": lin.NOME,
        "ENDERECO": lin.ENDERECO.upper()
    })
    # INCREMENTA CONTADOR
    count += 1

print(clientsToInsert)
print(clientsToInsert[2])


add_client = ("INSERT INTO CLIENTES (NOME, ENDERECO) VALUES (%s, %s)")
countAdded = 0
# RODAR CLIENTES A SEREM INSERIDOS
for client in clientsToInsert:
    # INSERIR NO BANCO AQUI
    print(client['NOME'])
    nome = client['NOME']
    endereco = client['ENDERECO']
    data_client = (nome, endereco)
    cursor.execute(add_client, data_client)
    countAdded +=1
    
print(f"{countAdded} novos clientes inseridos")

cnx.commit()

cursor.close()

cnx.close()
