import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost', database='db_meuslivros',user='root',password='100senha')
    consulta_sql="select *from tbl_produtos"
    cursor=con.cursor()
    cursor.execute(consulta_sql)
    linhas=cursor.fetchall()
    print("Numero total de registros retornados:",cursor.rowcount)
    print("\n Mostrar os produtos cadastrados \n")
    for linha in linhas:
        print("Id do Produto:",linha[0])
        print("Nome do produto:",linha[1])
        print("Preço:",linha[2])
        print("Quantidade:",linha[3],"\n")
except Error as e:
    print("Erro ao acessar tabela MySQL",e)
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada!")