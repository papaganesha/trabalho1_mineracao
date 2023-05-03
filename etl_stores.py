from sql_alchemy import get_engine
from load import load

import pandas as pd


def transform(data):
    #transform data here
    return data


if __name__ == '__main__':
        engine = get_engine()
	
        stores_df = pd.read_sql_query("SELECT * FROM EXTRACT_STORES;",engine)
        print("LOJAS PRA EXTRAIR => ",stores_df['ENDERECO'].count())
        # client_id = clients_df[clients_df['ID_CLIENTE']==1]
        # print(client_id)
        count_before_insertion = stores_df['ENDERECO'].count()

        load(count_before_insertion, stores_df, engine, "dw_d_lojas")


        
        # result = engine.execute("SELECT 1")
        
        # for row in result.mappings():
        #     print("Author:" , row["1"])

