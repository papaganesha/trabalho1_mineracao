import pandas as pd
from pandasql import sqldf
import matplotlib.pyplot as plt
import seaborn as sns

from sql_alchemy import get_engine
engine = get_engine()

query = 'SELECT A.SURROGATE, A.ID_VENDA, A.ID_LIVRO, C.CATEGORIA, A.VALOR, A.ID_LOJA, B.ENDERECO, A.DATA_VENDA, A.DATA_CORTE, B.FATURAMENTO_BRUTO, B.FATURAMENTO_LIQUIDO FROM DW_F_VENDAS A, DW_D_LOJAS B, DW_D_LIVROS C WHERE A.ID_LOJA = B.ID_LOJA AND A.ID_LIVRO = C.ID_LIVRO'

sells_df = pd.read_sql_query(query, engine)


#RENDA POR LOJAS
stores_profit = sqldf("SELECT ID_LOJA, ENDERECO, FATURAMENTO_BRUTO AS 'FAT_BRUTO', FATURAMENTO_LIQUIDO AS 'FAT_LIQUIDO' FROM sells_df group by id_loja")

#DUMP DATAFRAME RENDA POR LOJAS
stores_profit.to_csv('./output/stores_profit.csv', sep=',', encoding='utf-8', index=False)

# OS 5 LIVROS MAIS VENDIDOS
most_selled = sqldf("SELECT ID_LOJA, ENDERECO, ID_LIVRO,  COUNT(ID_LIVRO) AS 'QNT' FROM sells_df group by id_livro order by 'QNT' asc")

most_selled_largest_5 = most_selled.nlargest(4, 'QNT', keep='all')

# DUMP DATAFRAME RENDA POR LOJAS
most_selled_largest_5.to_csv('./output/most_selled.csv', sep=',', encoding='utf-8', index=False)


#LIVROS VENDIDOS - CATEGORIAS POR LOJA
categories_stores= sqldf("SELECT ID_LOJA, CATEGORIA, COUNT(CATEGORIA) AS 'QNT' FROM sells_df group by ID_LOJA order by 'id_loja' ASC")

#DUMP DATAFRAME CATEGORIA POR LOJA
stores_profit.to_csv('./output/categories_stores.csv', sep=',', encoding='utf-8', index=False)



