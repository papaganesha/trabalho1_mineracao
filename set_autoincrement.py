import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'mineracao',
    'raise_on_warnings': True
}


def set_autoincrement(table_name):
    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()

    try:
            alter_query = f'ALTER TABLE {table_name} AUTO_INCREMENT = 1'
            cursor.execute(alter_query)
    except Exception as e:
            print(e)
        
        
    print(f"{table_name} auto_increment resetado com sucesso")

    cnx.commit()

    cursor.close()

    cnx.close()


