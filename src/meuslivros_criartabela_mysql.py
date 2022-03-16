# https://www.youtube.com/watch?v=yMqBfSl53MA
import mysql.connector

try:
    #criar conexao ao banco de dados
    con = mysql.connector.connect(host='localhost', database='db_meuslivros',user='root',password='100senha')
    #declaracao SQL a ser executada
    criar_tabela_SQL ="""CREATE TABLE tbl_productos(
        IdProduto int(11) NOT NULL,
        NomeProduto VARCHAR(70) NOT NULL,
        Preco FLOAT NOT NULL,
        Quantidade TINYINT NOT NULL,
        PRIMARY KEY (IdPRoduto))"""
    #criar cursor e executar SQL no banco de dados
    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print("Tabela de Produtos criada com sucesso!")
except mysql.connector.Error as erro:
    print("Falha ao criar tabela no MySQL:{}".format(erro))
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada.")


