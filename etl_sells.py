from sql_alchemy import get_engine
from datetime import datetime
from load import load
from create_surrogate import generate_surrogate

import pandas as pd
now_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# PADRAO VENDAS
# NUMERO - DATA - LOJA - VALOR - LIVRO - DATA ETL
def etl_sells():
    engine = get_engine()

    sells_df = pd.read_sql_query(f'SELECT A.ID_VENDA, A.ID_LOJA ,A.VALOR, A.DATA_VENDA, A.DATA_CORTE, B.ID_LIVRO FROM VENDAS A, ITENS_VENDAS B WHERE A.ID_VENDA = B.ID_VENDA AND A.DATA_CORTE IS NULL;', engine)
    print("c ", sells_df['ID_VENDA'].count())

    count_before_insertion = sells_df['ID_VENDA'].count()
    surrogates = []
    for i in range(count_before_insertion):
        surrogates.append(generate_surrogate())
    
    sells_df['SURROGATE'] = surrogates
    sells_df.set_index('SURROGATE', drop=True, inplace=True)

    #MUDANDO VALORES NULOS DE DATA_CORTE, PARA DATA ATUAL
    sells_df['DATA_CORTE'] = now_date
    # CRIANDO TABELA DIMENSOES DE CLIENTES E PEGANDO COUNT DE REGISTROS INSERIDOS
    result  = sells_df.to_sql('dw_f_vendas',con=engine,if_exists='append',index=True)

    if(count_before_insertion == result):
        print(f"{result} NOVOS REGISTROS PARA OLAP FATO VENDAS CONCLUIDO")
        
        #SALVAR NA TABELA CONTROLE ULTIMA_DATA CORTE
    else:
         print("Erro durante extraçao e conversao dos dados")

    result = engine.execute(f'UPDATE VENDAS SET DATA_CORTE = "{now_date}"')

    print(result)

