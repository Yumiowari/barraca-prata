class Comanda():
    def __init__(self, produtos, valor):
        self.__produtos = produtos
        self.__valor = valor
        self.__lucro = None
        self.__data = None
        self.__hora = None
    
    @property
    def produtos(self):
        return self.__produtos

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, novo_valor):
        self.__valor = novo_valor

    @property
    def lucro(self):
        return self.__lucro
    
    @lucro.setter
    def lucro(self, novo_lucro):
        self.__lucro = novo_lucro

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, nova_data):
        self.__data = nova_data

    @property
    def hora(self):
        return self.__hora
    
    @hora.setter
    def hora(self, nova_hora):
        self.__hora = nova_hora

    def inserir_produto(self, codigo, qtd):
        flag = False
        for produto in self.__produtos:
            if produto.codigo == codigo:
                aux = produto
                flag = True
        
        if flag == True:
            qtd += aux.qtd # recupera a antiga qtd e incrementa
            novoProduto = Produto(codigo, qtd)
            for produto in self.__produtos:
                if produto.codigo == codigo: # sempre ocorrerá
                    self.__produtos.remove(produto) # remove o antigo produto
            
            self.__produtos.append(novoProduto) # e insere o novo
        else: # se o produto nunca foi inserido
            novoProduto = Produto(codigo, qtd)
            self.__produtos.append(novoProduto)

    def remover_produto(self, codigo, qtd):
        flag = False
        for produto in self.__produtos:
            if produto.codigo == codigo:
                aux = produto
                flag = True
        
        if flag == True:
            qtd -= aux.qtd # recupera a antiga qtd e incrementa
            novoProduto = Produto(codigo, qtd)
            for produto in self.__produtos:
                if produto.codigo == codigo: # sempre ocorrerá
                    self.__produtos.remove(produto) # remove o antigo produto
            
            self.__produtos.append(novoProduto) # e insere o novo

            return True
        else: # se o produto nunca foi inserido
            
            return False

class Produto(): # classe resumida de produto
    def __init__(self, codigo, qtd):
        self.__codigo = codigo
        self.__qtd = qtd

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def qtd(self):
        return self.__qtd
    
    @qtd.setter
    def qtd(self, nova_qtd):
        self.__qtd = nova_qtd