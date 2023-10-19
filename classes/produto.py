class Produto():
    def __init__(self, codigo, nome, custo, preco, estoque):
        self.__codigo = codigo
        self.__nome = nome
        self.__custo = custo
        self.__preco = preco
        self.__estoque = estoque

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def custo(self):
        return self.__custo
    
    @custo.setter
    def custo(self, novoCusto):
        self.__custo = novoCusto
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novoPreco):
        self.__preco = novoPreco
    
    @property
    def estoque(self):
        return self.__estoque
    
    @estoque.setter
    def estoque(self, novoEstoque):
        self.__estoque = novoEstoque