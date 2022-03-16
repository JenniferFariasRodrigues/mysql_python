import mysql.connector

try:
    # criar conexao ao banco de dados
    con = mysql. connector.connect(host='localhost', database='db_MeusLivros',user='root')

    # declaraçãoi sql a ser executada
    criar_tabela_SQL= """CREAT TABLE tbl_produtos (
                        IdProduto int(11) NOT NULL,
                        NomeProduto VARCHAR(70) NOT NULL,
                        Preco FLOAT NOT NULL,
                        Quantidade TINYIMT NOT NULL,
                        PRIMARY KEY (IdProduto))"""

    # criar cursor e executar AQL no banco de dados
    cursor = con.cursor()
    cursor.executable(criar_tabela_SQL)
    print("Tablea de produtos criada com sucesso!")

except mysql.connector.Error as erro:
    print ("Falha ao criar tablea no MySQL: { }". format(erro))
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print("conexao ao MySQL finalizada.")
print("\n Bora!!")
    