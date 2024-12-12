from slq.conexao_bd import conexao_database

def create(nome, categoria):
    conexao = conexao_database()
    cursor = conexao.cursor()
    cursor.execute

    consulta = "INSERT INTO restaurante (nome, categoria) VALUES (%s, %s)"
    valores = (nome, categoria)

    cursor.execute(consulta, valores)
    conexao.commit()

    print(f"O restaurante '{nome}'foi inserido com sucesso!")

    cursor.close()
    conexao.close()