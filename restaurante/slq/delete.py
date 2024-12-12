from slq.conexao_bd import conexao_database

def delete():
    conexao = conexao_database()
    cursor = conexao.cursor()


    escolha =  int(input(''' 
    VOCÊ DESEJA DELETAR PELO ID OU NOME?
    1 - CATEGORIA
    2 - NOME

'''))
    

    match escolha:

        case 1:
                categoria = input('Digite o nome da categoria que você deseja deletar: ')
                consulta = f'DELETE FROM restaurante WHERE categoria = "{categoria}"'
                print(f" {categoria} deletado com sucesso!")

        case 2:
                nome = input('Digite o nome do produto que você deseja deletar: ')
                consulta = f'DELETE FROM restaurante WHERE nome = "{nome}"'
                print(f" {nome} deletado com sucesso!")


    cursor.execute(consulta)
    conexao.commit()

    
    
    cursor.close()
    conexao.close()
    
# Exemplo de uso
if __name__ == "__main__":
    delete(1)
