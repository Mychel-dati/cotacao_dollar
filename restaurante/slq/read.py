from slq.conexao_bd import conexao_database

def read():
    conexao = conexao_database()
    cursor = conexao.cursor()

    consulta = "SELECT * FROM restaurante"
    cursor.execute(consulta)

    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)

    cursor.close()
    conexao.close()

# Exemplo de uso
if __name__ == "__main__":
    read()
