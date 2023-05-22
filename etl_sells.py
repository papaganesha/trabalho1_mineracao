from sql_alchemy import get_engine
from datetime import date,datetime, timedelta
from load import load
from create_surrogate import generate_surrogate

import pandas as pd

# PADRAO VENDAS
# NUMERO - DATA - LOJA - VALOR - LIVRO - DATA ETL
def etl_sells():
    engine = get_engine()

    #ULTIMA DATA CORTE PARA TABELAS VENDAS
    #select max(data_ultimo_corte) from etl_controle WHERE tabela = 'VENDAS'
    get_data_ultimo_corte = engine.execute("select max(data_ultimo_corte) as 'data' from etl_controle WHERE tabela = 'VENDAS'")
    data_ultimo_corte = get_data_ultimo_corte.mappings().all()[0]['data']

    print("ULTIMA DATA_CORTE => ",data_ultimo_corte)
    #CASO NAO EXISTA DATA DE ULTIMO CORTE
    if data_ultimo_corte != None:
        # data_ultimo_corte = get_data_ultimo_corte.mappings().all()[0]['data']
        
        #NOVA DATA DE CORTE
        #REGISTROS DEVEM CONTER DATA_VENDA MINIMA COM ESTE VALOR
        data_corte = data_ultimo_corte + timedelta(minutes=3)
        # print(data_ultimo_corte)
        print(f'NOVA DATA_CORTE => {data_corte}')

        #DATA DE VENDA DEVE SER D-1 DA DATA_ULTIMO_CORTE # teste d-3 minutos
        sells_df = pd.read_sql_query(f'SELECT A.ID_VENDA, A.ID_LOJA ,A.VALOR, A.DATA_VENDA, A.DATA_CORTE, B.ID_LIVRO FROM VENDAS A, ITENS_VENDAS B WHERE A.ID_VENDA = B.ID_VENDA AND A.DATA_VENDA <= "{data_corte}" AND A.DATA_CORTE IS NULL;', engine)
        print("VENDAS PARA TRANSFERIR =>", sells_df['ID_VENDA'].count())

        count_before_insertion = sells_df['ID_VENDA'].count()
        surrogates = []
        for i in range(count_before_insertion):
            surrogates.append(generate_surrogate())
        
        sells_df['SURROGATE'] = surrogates
        sells_df.set_index('SURROGATE', drop=True, inplace=True)


        #MUDANDO VALORES NULOS DE DATA_CORTE, PARA DATA ATUAL
        sells_df['DATA_CORTE'] = data_corte
        # CRIANDO TABELA DIMENSOES DE CLIENTES E PEGANDO COUNT DE REGISTROS INSERIDOS
        result  = sells_df.to_sql('dw_f_vendas',con=engine,if_exists='append',index=True)

        if(count_before_insertion == result):
            print(f"{result} NOVOS REGISTROS PARA OLAP FATO VENDAS CONCLUIDO")
            
            #SALVAR NA TABELA CONTROLE ULTIMA_DATA CORTE
        else:
            print("Erro durante extraçao e conversao dos dados")

        result = engine.execute(f'UPDATE VENDAS SET DATA_CORTE = now() WHERE DATA_VENDA <= "{data_corte}"')

        result = engine.execute(f'INSERT INTO ETL_CONTROLE(TABELA, ID_MODELO, DATA_ULTIMO_CORTE) VALUES("VENDAS", 1, "{data_corte}")')

        print(result)
    
    else:
        # data_ultimo_corte = get_data_ultimo_corte.mappings().all()[0]['data']
        get_date_now = engine.execute("select now() as 'data' ")

        date_now = get_date_now.mappings().all()[0]['data']
        #NOVA DATA DE CORTE
        #REGISTROS DEVEM CONTER DATA_VENDA MINIMA COM ESTE VALOR
        data_corte = date_now
        # print(data_ultimo_corte)
        print(f'NOVA DATA_CORTE => {data_corte}')

        #DATA DE VENDA DEVE SER D-1 DA DATA_ULTIMO_CORTE # teste d-3 minutos
        sells_df = pd.read_sql_query(f'SELECT A.ID_VENDA, A.ID_LOJA ,A.VALOR, A.DATA_VENDA, A.DATA_CORTE, B.ID_LIVRO FROM VENDAS A, ITENS_VENDAS B WHERE A.ID_VENDA = B.ID_VENDA AND A.DATA_VENDA <= "{data_corte}" AND A.DATA_CORTE IS NULL;', engine)
        print("VENDAS PARA TRANSFERIR =>", sells_df['ID_VENDA'].count())

        count_before_insertion = sells_df['ID_VENDA'].count()
        surrogates = []
        for i in range(count_before_insertion):
            surrogates.append(generate_surrogate())
        
        sells_df['SURROGATE'] = surrogates
        sells_df.set_index('SURROGATE', drop=True, inplace=True)

        #MUDANDO VALORES NULOS DE DATA_CORTE, PARA DATA ATUAL
        sells_df['DATA_CORTE'] = date_now
        # CRIANDO TABELA DIMENSOES DE CLIENTES E PEGANDO COUNT DE REGISTROS INSERIDOS
        result  = sells_df.to_sql('dw_f_vendas',con=engine,if_exists='append',index=True)

        if(count_before_insertion == result):
            print(f"{result} NOVOS REGISTROS PARA OLAP FATO VENDAS CONCLUIDO")
            
            #SALVAR NA TABELA CONTROLE ULTIMA_DATA CORTE
        else:
            print("Erro durante extraçao e conversao dos dados")

        result = engine.execute(f'UPDATE VENDAS SET DATA_CORTE = now() WHERE DATA_VENDA <= "{data_corte}"')

        result = engine.execute(f'INSERT INTO ETL_CONTROLE(TABELA, ID_MODELO, DATA_ULTIMO_CORTE) VALUES("VENDAS", 1, "{data_corte}")')

        print(result)


# PADRAO VENDAS
# NUMERO - DATA - LOJA - VALOR - LIVRO - DATA ETL
def etl_sells_all():
        engine = get_engine()
        # data_ultimo_corte = get_data_ultimo_corte.mappings().all()[0]['data']
        get_date_now = engine.execute("select now() as 'data' ")

        date_now = get_date_now.mappings().all()[0]['data']
        #NOVA DATA DE CORTE
        #REGISTROS DEVEM CONTER DATA_VENDA MINIMA COM ESTE VALOR
        data_corte = date_now
        # print(data_ultimo_corte)
        print(f'NOVA DATA_CORTE => {data_corte}')

        #DATA DE VENDA DEVE SER D-1 DA DATA_ULTIMO_CORTE # teste d-3 minutos
        sells_df = pd.read_sql_query(f'SELECT A.ID_VENDA, A.ID_LOJA ,A.VALOR, A.DATA_VENDA, A.DATA_CORTE, B.ID_LIVRO FROM VENDAS A, ITENS_VENDAS B WHERE A.ID_VENDA = B.ID_VENDA AND A.DATA_CORTE IS NULL;', engine)
        print("VENDAS PARA TRANSFERIR =>", sells_df['ID_VENDA'].count())

        count_before_insertion = sells_df['ID_VENDA'].count()
        surrogates = []
        for i in range(count_before_insertion):
            surrogates.append(generate_surrogate())
        
        sells_df['SURROGATE'] = surrogates
        sells_df.set_index('SURROGATE', drop=True, inplace=True)

        #MUDANDO VALORES NULOS DE DATA_CORTE, PARA DATA ATUAL
        sells_df['DATA_CORTE'] = date_now
        # CRIANDO TABELA DIMENSOES DE CLIENTES E PEGANDO COUNT DE REGISTROS INSERIDOS
        result  = sells_df.to_sql('dw_f_vendas',con=engine,if_exists='append',index=True)

        if(count_before_insertion == result):
            print(f"{result} NOVOS REGISTROS PARA OLAP FATO VENDAS CONCLUIDO")
            
            #SALVAR NA TABELA CONTROLE ULTIMA_DATA CORTE
        else:
            print("Erro durante extraçao e conversao dos dados")

        result = engine.execute(f'UPDATE VENDAS SET DATA_CORTE = now() WHERE DATA_VENDA <= "{data_corte}"')

        result = engine.execute(f'INSERT INTO ETL_CONTROLE(TABELA, ID_MODELO, DATA_ULTIMO_CORTE) VALUES("VENDAS", 1, "{data_corte}")')

        print(result)


etl_sells()

# etl_sells_all()