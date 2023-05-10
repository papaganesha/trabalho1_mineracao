from sql_alchemy import get_engine
from load import load
import pandas as pd


def etl_stores():
        engine = get_engine()
	
        stores_df = pd.read_sql_query("SELECT * FROM EXTRACT_STORES;",engine)
        print("LOJAS PRA EXTRAIR => ",stores_df['ENDERECO'].count())
       
        count_before_insertion = stores_df['ENDERECO'].count()

        load(count_before_insertion, stores_df, engine, "dw_d_lojas")

