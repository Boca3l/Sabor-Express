from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

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
        self._cardapio = []
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
    
    # def adicionar_bebida_no_cardapio(self,bebida):
    #     self._cardapio.append(bebida)

    # def adicionar_prato_no_cardapio(self,prato):
    #     self._cardapio.append(prato)

    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do Restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,'tipo'):
                mensagem_sobremesa = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao} | Tipo: {item.tipo}'
                print(mensagem_sobremesa)
            elif hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
