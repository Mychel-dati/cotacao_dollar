from slq.conexao_bd import conexao_database

def update(categoria, novo_nome):
    conexao = conexao_database()
    cursor = conexao.cursor()

    consulta = "UPDATE restaurante SET nome = %s WHERE nome = %s"
    valores = (novo_nome, categoria)

    cursor.execute(consulta, valores)
    conexao.commit()

    print(f"Nome atualixado para {novo_nome} ")

    cursor.close()
    conexao.close()

# Exemplo de uso
if __name__ == "__main__":
    update(1, 25)
