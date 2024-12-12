
import mysql.connector
def conexao_database():
    conexao =  mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'greatt'
)
    return conexao
    
