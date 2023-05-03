from sql_alchemy import get_engine
from load import load


import pandas as pd


def etl_books():
        engine = get_engine()
	
        books_df = pd.read_sql_query("SELECT * FROM EXTRACT_BOOKS;",engine)
        print("LIVROS PRA EXTRAIR => ",books_df['ID_LIVRO'].count())
        # client_id = clients_df[clients_df['ID_CLIENTE']==1]
        # print(client_id)
        count_before_insertion = books_df['ID_LIVRO'].count()

        load(count_before_insertion, books_df, engine, "dw_d_livros")



        
        # result = engine.execute("SELECT 1")
        
        # for row in result.mappings():
        #     print("Author:" , row["1"])

