import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'mineracao',
    'raise_on_warnings': True
}


def drop_table(table_name):
    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()

    try:
            drop_table_query = f'DROP TABLE {table_name}'
            cursor.execute(drop_table_query)
    except Exception as e:
            print(e)
        
        
    print(f"Tabela {table_name} dropada com sucesso")

    cnx.commit()

    cursor.close()

    cnx.close()


