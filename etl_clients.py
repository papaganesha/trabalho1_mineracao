from sql_alchemy import get_engine
from load import load
import pandas as pd



def etl_clients():
        engine = get_engine()

        clients_df = pd.read_sql_query("SELECT * FROM EXTRACT_CLIENTS;",engine)
        print("CLIENTES PRA EXTRAIR => ",clients_df['ID_CLIENTE'].count())
        count_before_insertion = clients_df['ID_CLIENTE'].count()
        load(count_before_insertion, clients_df, engine, "dw_d_clientes")


etl_clients()