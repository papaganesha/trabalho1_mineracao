# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine
import pandas as pd

# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'mineracao'

# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(url=F"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")


if __name__ == '__main__':
        try:
            # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
            engine = get_connection()
            print(f"Connection to the {host} for user {user} created successfully.")

        
        except Exception as ex:
            print("Connection could not be made due to the following error: \n", ex)
	
        clients_df = pd.read_sql_query("SELECT A.ID_CLIENTE, A.NOME, A.ENDERECO, SUM(C.VALOR) AS 'GASTOS', COUNT(D.ID_VENDA) AS 'LIVROS' FROM CLIENTES A, TABELA_CHAVE B, VENDAS C, ITENS_VENDAS D WHERE A.ID_CLIENTE = B.ID AND B.TABELA = 'CLIENTES' AND CARGA = 0 AND A.ID_CLIENTE = C.ID_CLIENTE AND C.ID_VENDA = D.ID_VENDA GROUP BY ID;",engine)
        print(clients_df.head(5))
        client_id = clients_df[clients_df['ID_CLIENTE']==1]
        print(client_id)

        clients_df.to_sql('dw_d_clientes',con=engine,if_exists='replace',index=False)
        
        #SOMANDO GASTOS DO CLIENTE
        # waste=0
        # if sal >500 and sal <=1250:
        #     tax=sal*.125
        # elif sal>1250 and sal<=1700:
        #     tax=sal*.175
        # elif sal>1700 and sal<=2500:
        #     tax=sal*.225
        # elif sal>2500:
        #     tax=sal*.275
        # else:
        #     tax=0
        # peint(waste)

