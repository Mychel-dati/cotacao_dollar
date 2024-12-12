from modelos.restaurante import Restaurante
# from modelos.cardapio.bebida import Bebida
# from modelos.cardapio.prato import Prato
from slq.conexao_bd import conexao_database

from slq.main import main


conexao = conexao_database()
cursor = conexao.cursor()


if __name__ == '__main__':
    main()
Restaurante()






    

    
