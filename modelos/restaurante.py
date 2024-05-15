from modelos.avaliacao import Avaliacao

class Restaurante:
    '''Representa um restaurante e suas caracteristicas'''

    restaurantes = []

    def __init__(self, nome, categoria):
        
        '''Inicia uma instancia Restaurante
        
        Input:
        -nome (str): nome do restaurante
        -categoria (str): categoria do restaurante
        
        '''

        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Retorna uma apresentação em string do restaurante'''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Exibe uma lista formatada de todos os restaurantes'''
        print(f'{'Nome do reataurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        '''Retorna uma caixa indicando o status do restaurante'''
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        '''Alterna o estado de atividade do restaurante'''
        self._ativo = not self._ativo

    def receber_avaliacao(self,cliente,nota):
        '''Registra uma avaliação para o restaurante
        
        Input:
        -cliente (str): Nome do cliente que fez a avaliação
        -nota (Float): A nota atribuída ao restaurante (entre 0 e 5)

        '''
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente,nota)
            self._avaliacao.append(avaliacao)
        else:
            print (f'Nota de {cliente} inválida')

    @property
    def media_avaliacao(self):

        '''Calcula e retorna a avaliação média do restaurante '''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas,1)
        return media
