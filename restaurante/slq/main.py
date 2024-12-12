from slq.create import create
from slq.read import read
from slq.update import update
from slq.delete import delete
import os
# from conexao_bd import conexao_database

def mostrar_menu():
    print("\n--- Menu de Operações ---")
    print("1. Adicionar um novo restaurante")
    print("2. Ver lista de restaurantes")
    print("3. Atualizar Restaurante")
    print("4. Deletar Restaurante")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def main():
    while True:
        
        opcao = mostrar_menu()
        
        if opcao == '1':
            nome_restaurante = input("Digite o nome do restaurante: ")
            categoria = (input("Digite a categoria do restaurante: "))
            create(nome_restaurante, categoria)
        
        elif opcao == '2':
            read()
        
        elif opcao == '3':
            categoria = (input("Digite  o nome do restaurante que você deseja atualizar: "))
            novo_nome = (input("Digite o novo nome do restaurante: "))
            update(categoria, novo_nome)
        
        elif opcao == '4':
            visualizar_lista = input('voce deseja visualizar a lista de Restaurantes antes de deletar? ')
            if visualizar_lista == 's':
                read()
                
            delete()


               
                    
                    
   
        elif opcao == '5':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")
        input('\nTecle Enter para voltar ao inicio')
        os.system('cls')    


if __name__ == "__main__":
    main()

