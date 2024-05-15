from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','Gourmet')
restaurante_praca.receber_avaliacao('Gui',10)
restaurante_praca.receber_avaliacao('Lais',2)
restaurante_praca.receber_avaliacao('Pedro',4)
restaurante_mexicano = Restaurante('Mexican Food','mexicana')
restaurante_japones = Restaurante('Japa','Japonesa')
restaurante_praca.alternar_estado()

def main():
    '''Funcoes de restaurante possuem docstring'''
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
