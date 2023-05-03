import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'mineracao',
    'raise_on_warnings': True
}


def delete_table_data(table_name):
    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()

    try:
            delete_query = f'DELETE FROM {table_name}'
            cursor.execute(delete_query)
    except Exception as e:
            print(e)
        
        
    print(f"{table_name} resetada com sucesso")

    cnx.commit()

    cursor.close()

    cnx.close()


