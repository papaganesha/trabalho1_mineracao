import mysql.connector
import random as rd


config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'mineracao',
    'raise_on_warnings': True
}

def insert_sells(sells_nbr, cut_date):
    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()

    count = 0

    # PEGAR 100(OU MAIS) CLIENTES ALEATORIOS DO BANCO
    # SELECT * FROM CLIENTES ORDER BY RAND() LIMIT 100;

    for i in range(sells_nbr):
        # print(f'============ INSERINDO NOVA VENDA =================================================================')
        # print(f'VENDA NUMERO => {i}')
        # Definindo numero de livros por venda
        sorteio = rd.sample([1, 2, 3], counts=[12, 6, 2], k=1)
        # sorteio.sort()
        # print(f'NUMERO DE LIVROS DA VENDA => {sorteio[0]}')

        books_on_sell = []
        # print("===== LIVROS DA VENDA ========================================")
        for i in range(sorteio[0]):
            # pega livro aleatorio
            get_random_book = ("SELECT ID_LIVRO, TITULO, VALOR_VENDA FROM LIVROS ORDER BY RAND() LIMIT 1")
            #data_sell = (title, buy_value, sell_value)

            # EXECUTANDO QUERY
            cursor.execute(get_random_book)
            # PEGANDO RESULTADOS DA QUERY
            result = cursor.fetchall()
            # ID, TITULO E VALOR DE VENDA DO LIVRO ALEATORIO
            # print(f'ID_LIVRO => {result[0][0]} / TITULO => {result[0][1]} / VALOR => R${result[0][2]}')
            # cnx.commit()
            books_on_sell.append(result[0])



        # somar valor da venda
        # print(books_on_sell[0][2])
        soma = 0
        for i in books_on_sell:
            # print(i[2])
            soma += i[2]

        # print("SOMA_VENDA => ", soma)

        # pega cliente aleatorio
        get_random_client = (
            "SELECT ID_CLIENTE FROM CLIENTES ORDER BY RAND() LIMIT 1")
        #data_sell = (title, buy_value, sell_value)

        # EXECUTANDO QUERY
        cursor.execute(get_random_client)
        # PEGANDO RESULTADOS DA QUERY
        result = cursor.fetchall()
        # ID DO CLIENTE ALEATORIO
        # print(f'ID_CLIENTE => {result[0][0]}')
        id_cliente = result[0][0]
        # cnx.commit()

        # pega loja aleatoria
        get_random_store = ("SELECT ID_LOJA FROM LOJAS ORDER BY RAND() LIMIT 1")
        #data_sell = (title, buy_value, sell_value)

        # EXECUTANDO QUERY
        cursor.execute(get_random_store)
        # PEGANDO RESULTADOS DA QUERY
        result = cursor.fetchall()
        # ID DA LOJA ALEATORIA
        # print(f'ID_LOJA => {result[0][0]}')
        id_loja = result[0][0]
        # Query da venda
        add_sell = ('INSERT INTO `VENDAS`(ID_CLIENTE, ID_LOJA, VALOR, DATA_VENDA, DATA_CORTE) VALUES (%s, %s, %s, %s, %s);')

        # EXECUTANDO QUERY DA VENDA
        #print(id_cliente, id_loja, soma, cut_date, cut_date)
        cursor.execute(add_sell, (id_cliente, id_loja, soma, cut_date, cut_date))
        # #PEGANDO ID DA VENDA
        sell_id = cursor.lastrowid
        count+=1

        # Adicionar item venda para cada livro
        for i in range(sorteio[0]):
            #Query de item_venda
            add_book_sell = ("INSERT INTO ITENS_VENDAS (ID_VENDA, ID_LIVRO) VALUES (%s, %s)")
            #DADOS DE INSERCAO DA VENDA
            #print("test", books_on_sell[i][0])
            #EXECUTANDO QUERY DA VENDA
            cursor.execute(add_book_sell, (sell_id, books_on_sell[i][0]))
        

    print(f"{count} novas vendas inseridas para data_corte => {cut_date}")

    cursor.close()

    cnx.commit()

    cnx.close()
