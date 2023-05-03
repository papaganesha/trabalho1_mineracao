def load(count_before_insertion, df_to_load, engine, dw_name):
    #load data to OLAP table in MYSQL
    result = df_to_load.to_sql(dw_name ,engine,if_exists='append',index=False)
    if(count_before_insertion == result):
        print(f"{dw_name} carregado com sucesso")
    else:
        print("Erro durante extraçao e conversao dos dados")