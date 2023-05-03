from sql_alchemy import get_engine
from load import load

import pandas as pd





if __name__ == '__main__':
        engine = get_engine()
	
        stores_df = pd.read_sql_query("SELECT * FROM EXTRACT_STORES;",engine)
        print("c ",stores_df['ENDERECO'].count())
        # client_id = clients_df[clients_df['ID_CLIENTE']==1]
        # print(client_id)
        count_before_insertion = stores_df['ENDERECO'].count()

        #CRIANDO TABELA DIMENSOES DE CLIENTES E PEGANDO COUNT DE REGISTROS INSERIDOS
        result  = stores_df.to_sql('dw_d_lojas',con=engine,if_exists='append',index=False)

        if(count_before_insertion == result):
            print("OLAP DIMENSAO LOJAS CONCLUIDO")
        else:
             print("Erro durante extraçao e conversao dos dados")


        
        # result = engine.execute("SELECT 1")
        
        # for row in result.mappings():
        #     print("Author:" , row["1"])

