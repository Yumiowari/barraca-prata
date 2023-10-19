### bibliotecas

import tkinter as tk
from tkinter import messagebox as msg
import os
import datetime
from babel.dates import format_date, format_time # pip install Babel

# minhas
import lib.arquivo as arquivo # o nome do arquivo deve incluir .pkl!
#

# tipo de dado
import classes.produto as tipo
#

###

# Janela de cadastro de produto
class LimiteCadastro(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)

        self.controle = controle

        self.geometry('400x300')
        self.title('Cadastro de Produto')

        self.frameTopo = tk.Frame(self)
        self.frameBase = tk.Frame(self)

        ### entrada de dados

        # código
        self.frameCodigo = tk.Frame(self.frameTopo)
        self.labelCodigo = tk.Label(self.frameCodigo, text = 'Código:')
        self.codigo = tk.StringVar()
        self.inputCodigo = tk.Entry(self.frameCodigo, textvariable = self.codigo, width = 4)
        self.codigo.trace('w', self.verificacao_codigo)
        self.labelCodigo.pack(side = 'left')
        self.inputCodigo.pack(side = 'right')
        self.frameCodigo.pack()
        #

        # nome
        self.frameNome = tk.Frame(self.frameTopo)
        self.labelNome = tk.Label(self.frameNome, text = 'Nome:')
        self.nome = tk.StringVar()
        self.inputNome = tk.Entry(self.frameNome, textvariable = self.nome, width = 15)
        self.nome.trace('w', self.verificacao_nome)
        self.labelNome.pack(side = 'left')
        self.inputNome.pack(side = 'right')
        self.frameNome.pack()
        #

        # custo de produção
        self.frameCusto = tk.Frame(self.frameTopo)

        self.frameCustoEsq = tk.Frame(self.frameCusto)
        self.frameCustoDir = tk.Frame(self.frameCusto)

        # parte de real
        self.labelCustoEsq = tk.Label(self.frameCustoEsq, text = 'Custo:')
        self.realCusto = tk.StringVar()
        self.inputCustoEsq = tk.Entry(self.frameCustoEsq, textvariable = self.realCusto, width = 2)
        self.realCusto.trace('w', self.verificacao_custo_esq)
        self.labelCustoEsq.pack(side = 'left')
        self.inputCustoEsq.pack(side = 'right')
        self.frameCustoEsq.pack(side = 'left')
        #

        # parte de centavo
        self.labelCustoDir = tk.Label(self.frameCustoDir, text = ',')
        self.centavoCusto = tk.StringVar()
        self.inputCustoDir = tk.Entry(self.frameCustoDir, textvariable = self.centavoCusto, width = 2)
        self.centavoCusto.trace('w', self.verificacao_custo_dir)
        self.labelCustoDir.pack(side = 'left')
        self.inputCustoDir.pack(side = 'right')
        self.frameCustoDir.pack(side = 'right')
        #

        self.frameCusto.pack()
        #

        # preço de venda
        self.framePreco = tk.Frame(self.frameTopo)

        self.framePrecoEsq = tk.Frame(self.framePreco)
        self.framePrecoDir = tk.Frame(self.framePreco)

        # parte de real
        self.labelPrecoEsq = tk.Label(self.framePrecoEsq, text = 'Preço:')
        self.realPreco = tk.StringVar()
        self.inputPrecoEsq = tk.Entry(self.framePrecoEsq, textvariable = self.realPreco, width = 2)
        self.realPreco.trace('w', self.verificacao_preco_esq)
        self.labelPrecoEsq.pack(side = 'left')
        self.inputPrecoEsq.pack(side = 'right')
        self.framePrecoEsq.pack(side = 'left')
        #

        # parte de centavo
        self.labelPrecoDir = tk.Label(self.framePrecoDir, text = ',')
        self.centavoPreco = tk.StringVar()
        self.inputPrecoDir = tk.Entry(self.framePrecoDir, textvariable = self.centavoPreco, width = 2)
        self.centavoPreco.trace('w', self.verificacao_preco_dir)
        self.labelPrecoDir.pack(side = 'left')
        self.inputPrecoDir.pack(side = 'right')
        self.framePrecoDir.pack(side = 'right')
        #

        self.framePreco.pack()
        #

        # Estoque
        self.frameEstoque = tk.Frame(self.frameTopo)
        self.labelEstoque = tk.Label(self.frameEstoque, text = 'Estoque:')
        self.estoque = tk.StringVar()
        self.inputEstoque = tk.Entry(self.frameEstoque, textvariable = self.estoque, width = 3)
        self.estoque.trace('w', self.verificacao_estoque)
        self.labelEstoque.pack(side = 'left')
        self.inputEstoque.pack(side = 'right')
        self.frameEstoque.pack()
        #

        ###

        ###

        self.frameTopo.pack(side = 'top')

        ### botões

        # confirmar
        self.botaoConfirmar = tk.Button(self.frameBase, text = 'Confirmar')
        self.botaoConfirmar.bind('<ButtonRelease-1>', self.controle.confirmarCadastro)
        self.botaoConfirmar.pack(side = 'left')
        #

        # limpar
        self.botaoLimpar = tk.Button(self.frameBase, text = 'Limpar')
        self.botaoLimpar.bind('<ButtonRelease-1>', self.controle.limparCadastro)
        self.botaoLimpar.pack(side = 'right')
        #

        ###

        self.frameBase.pack(side = 'bottom')

    ### funções de verificação

    # código
    def verificacao_codigo(self, *args):
        codigo = self.codigo.get()

        aux = ''

        # verificação de tipo de dado
        for numero in codigo:
            if numero.isdigit():
                aux += numero
        #
        
        # verificação de tamanho
        if len(aux) > 4:
            aux = aux[:-1]
        #

        self.codigo.set(aux)
    #

    # nome
    def verificacao_nome(self, *args):
        nome = self.nome.get()

        aux = ''

        # verificação de tipo de dado
        for letra in nome:
            if not letra.isdigit():
                aux += letra
        #
        
        # verificação de tamanho
        if len(aux) > 30:
            aux = aux[:-1]
        #

        self.nome.set(aux)
    #

    # parte inteira do custo
    def verificacao_custo_esq(self, *args):
        custo = self.realCusto.get()

        aux = ''

        # verificação de tipo de dado
        for letra in custo:
            if letra.isdigit():
                aux += letra
        #
        
        # verificação de tamanho
        if len(aux) > 2:
            aux = aux[:-1]
        #

        self.realCusto.set(aux)
    #

    # parte decimal do custo
    def verificacao_custo_dir(self, *args):
        custo = self.centavoCusto.get()

        aux = ''

        # verificação de tipo de dado
        for letra in custo:
            if letra.isdigit():
                aux += letra
        #
        
        # verificação de tamanho
        if len(aux) > 2:
            aux = aux[:-1]
        #

        self.centavoCusto.set(aux)
    #

    # parte inteira do preço
    def verificacao_preco_esq(self, *args):
        preco = self.realPreco.get()

        aux = ''

        # verificação de tipo de dado
        for letra in preco:
            if letra.isdigit():
                aux += letra
        #
        
        # verificação de tamanho
        if len(aux) > 2:
            aux = aux[:-1]
        #

        self.realPreco.set(aux)
    #

    # parte decimal do preço
    def verificacao_preco_dir(self, *args):
        preco = self.centavoPreco.get()

        aux = ''

        # verificação de tipo de dado
        for letra in preco:
            if letra.isdigit():
                aux += letra
        #
        
        # verificação de tamanho
        if len(aux) > 2:
            aux = aux[:-1]
        #

        self.centavoPreco.set(aux)
    #

    # estoque
    def verificacao_estoque(self, *args):
        estoque = self.estoque.get()

        aux = ''

        # verificação de tipo de dado
        for numero in estoque:
            if numero.isdigit():
                aux += numero
        #
        
        # verificação de tamanho
        if len(aux) > 3:
            aux = aux[:-1]
        #

        self.estoque.set(aux)
    #

    ###

# Janela de consulta de produto
class LimiteConsulta(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)

        self.controle = controle

        self.geometry('400x300')
        self.title('Consulta de Produto')

        self.frameTopo = tk.Frame(self)
        self.frameBase = tk.Frame(self)

        ### entrada de dados

        # código
        self.frameCodigo = tk.Frame(self.frameTopo)
        self.labelCodigo = tk.Label(self.frameCodigo, text = 'Código:')
        self.codigo = tk.StringVar()
        self.inputCodigo = tk.Entry(self.frameCodigo, textvariable = self.codigo, width = 4)
        self.codigo.trace('w', self.verificacao_codigo)
        self.labelCodigo.pack(side = 'left')
        self.inputCodigo.pack(side = 'right')
        self.frameCodigo.pack()
        #

        ###

        self.frameTopo.pack(side = 'top')

        ### botões

        # confirmar
        self.botaoConfirmar = tk.Button(self.frameBase, text = 'Confirmar')
        self.botaoConfirmar.bind('<ButtonRelease-1>', self.controle.confirmarConsulta)
        self.botaoConfirmar.pack(side = 'left')
        #

        # limpar
        self.botaoLimpar = tk.Button(self.frameBase, text = 'Limpar')
        self.botaoLimpar.bind('<ButtonRelease-1>', self.controle.limparConsulta)
        self.botaoLimpar.pack(side = 'right')
        #

        ###

        self.frameBase.pack(side = 'bottom')

    # verificação de código
    def verificacao_codigo(self, *args):
        codigo = self.codigo.get()

        aux = ''

        # verificação de tipo de dado
        for numero in codigo:
            if numero.isdigit():
                aux += numero
        #
        
        # verificação de tamanho
        if len(aux) > 4:
            aux = aux[:-1]
        #

        self.codigo.set(aux)
    #

# Janela de edição de produto
class LimiteEdicao(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)

        self.controle = controle

        self.geometry('400x300')
        self.title('Edição de Produto')

        self.frameTopo = tk.Frame(self)
        self.frameBase = tk.Frame(self)

        ### entrada de dados

        # código
        self.frameCodigo = tk.Frame(self.frameTopo)
        self.labelCodigo = tk.Label(self.frameCodigo, text = 'Código:')
        self.codigo = tk.StringVar()
        self.inputCodigo = tk.Entry(self.frameCodigo, textvariable = self.codigo, width = 4)
        self.codigo.trace('w', self.verificacao_codigo)
        self.labelCodigo.pack(side = 'left')
        self.inputCodigo.pack(side = 'right')
        self.frameCodigo.pack()
        #

        # custo de produção
        self.frameCusto = tk.Frame(self.frameTopo)

        self.frameCustoEsq = tk.Frame(self.frameCusto)
        self.frameCustoDir = tk.Frame(self.frameCusto)

        # parte de real
        self.labelCustoEsq = tk.Label(self.frameCustoEsq, text = 'Novo custo:')
        self.realCusto = tk.StringVar()
        self.inputCustoEsq = tk.Entry(self.frameCustoEsq, textvariable = self.realCusto, width = 2)
        self.realCusto.trace('w', self.verificacao_custo_esq)
        self.labelCustoEsq.pack(side = 'left')
        self.inputCustoEsq.pack(side = 'right')
        self.frameCustoEsq.pack(side = 'left')
        #

        # parte de centavo
        self.labelCustoDir = tk.Label(self.frameCustoDir, text = ',')
        self.centavoCusto = tk.StringVar()
        self.inputCustoDir = tk.Entry(self.frameCustoDir, textvariable = self.centavoCusto, width = 2)
        self.centavoCusto.trace('w', self.verificacao_custo_dir)
        self.labelCustoDir.pack(side = 'left')
        self.inputCustoDir.pack(side = 'right')
        self.frameCustoDir.pack(side = 'right')
        #

        self.frameCusto.pack()
        #

        # preço de venda
        self.framePreco = tk.Frame(self.frameTopo)

        self.framePrecoEsq = tk.Frame(self.framePreco)
        self.framePrecoDir = tk.Frame(self.framePreco)

        # parte de real
        self.labelPrecoEsq = tk.Label(self.framePrecoEsq, text = 'Novo preço:')
        self.realPreco = tk.StringVar()
        self.inputPrecoEsq = tk.Entry(self.framePrecoEsq, textvariable = self.realPreco, width = 2)
        self.realPreco.trace('w', self.verificacao_preco_esq)
        self.labelPrecoEsq.pack(side = 'left')
        self.inputPrecoEsq.pack(side = 'right')
        self.framePrecoEsq.pack(side = 'left')
        #

        # parte de centavo
        self.labelPrecoDir = tk.Label(self.framePrecoDir, text = ',')
        self.centavoPreco = tk.StringVar()
        self.inputPrecoDir = tk.Entry(self.framePrecoDir, textvariable = self.centavoPreco, width = 2)
        self.centavoPreco.trace('w', self.verificacao_preco_dir)
        self.labelPrecoDir.pack(side = 'left')
        self.inputPrecoDir.pack(side = 'right')
        self.framePrecoDir.pack(side = 'right')
        #

        self.framePreco.pack()
        #

        ###

        ###

        self.frameTopo.pack(side = 'top')

        ### botões

        # confirmar
        self.botaoConfirmar = tk.Button(self.frameBase, text = 'Confirmar')
        self.botaoConfirmar.bind('<ButtonRelease-1>', self.controle.confirmarEdicao)
        self.botaoConfirmar.pack(side = 'left')
        #

        # limpar
        self.botaoLimpar = tk.Button(self.frameBase, text = 'Limpar')
        self.botaoLimpar.bind('<ButtonRelease-1>', self.controle.limparEdicao)
        self.botaoLimpar.pack(side = 'right')
        #

        ###

        self.frameBase.pack(side = 'bottom')

    ### funções de verificação

    # código
    def verificacao_codigo(self, *args):
        codigo = self.codigo.get()

        aux = ''

        # verificação de tipo de dado
        for numero in codigo:
            if numero.isdigit():
                aux += numero
        #
        
        # verificação de tamanho
        if len(aux) > 4:
            aux = aux[:-1]
        #

        self.codigo.set(aux)
    #

    # parte inteira do custo
    def verificacao_custo_esq(self, *args):
        custo = self.realCusto.get()

        aux = ''

        # verificação de tipo de dado
        for letra in custo:
            if letra.isdigit():
                aux += letra
        #
        
        # verificação de tamanho
        if len(aux) > 2:
            aux = aux[:-1]
        #

        self.realCusto.set(aux)
    #

    # parte decimal do custo
    def verificacao_custo_dir(self, *args):
        custo = self.centavoCusto.get()

        aux = ''

        # verificação de tipo de dado
        for letra in custo:
            if letra.isdigit():
                aux += letra
        #
        
        # verificação de tamanho
        if len(aux) > 2:
            aux = aux[:-1]
        #

        self.centavoCusto.set(aux)
    #

    # parte inteira do preço
    def verificacao_preco_esq(self, *args):
        preco = self.realPreco.get()

        aux = ''

        # verificação de tipo de dado
        for letra in preco:
            if letra.isdigit():
                aux += letra
        #
        
        # verificação de tamanho
        if len(aux) > 2:
            aux = aux[:-1]
        #

        self.realPreco.set(aux)
    #

    # parte decimal do preço
    def verificacao_preco_dir(self, *args):
        preco = self.centavoPreco.get()

        aux = ''

        # verificação de tipo de dado
        for letra in preco:
            if letra.isdigit():
                aux += letra
        #
        
        # verificação de tamanho
        if len(aux) > 2:
            aux = aux[:-1]
        #

        self.centavoPreco.set(aux)
    #

    ###

# Janela de atualização de estoque
class LimiteEdicaoEstoque(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)

        self.controle = controle

        self.geometry('400x300')
        self.title('Atualização de Estoque')

        self.frameTopo = tk.Frame(self)
        self.frameBase = tk.Frame(self)

        ### entrada de dados

        # código
        self.frameCodigo = tk.Frame(self.frameTopo)
        self.labelCodigo = tk.Label(self.frameCodigo, text = 'Código:')
        self.codigo = tk.StringVar()
        self.inputCodigo = tk.Entry(self.frameCodigo, textvariable = self.codigo, width = 4)
        self.codigo.trace('w', self.verificacao_codigo)
        self.labelCodigo.pack(side = 'left')
        self.inputCodigo.pack(side = 'right')
        self.frameCodigo.pack()
        #

        # qtd
        self.frameQtd = tk.Frame(self.frameTopo)
        self.labelQtd = tk.Label(self.frameQtd, text = 'Quantidade:')
        self.qtd = tk.StringVar()
        self.inputQtd = tk.Entry(self.frameQtd, textvariable = self.qtd, width = 3)
        self.qtd.trace('w', self.verificacao_qtd)
        self.labelQtd.pack(side = 'left')
        self.inputQtd.pack(side = 'right')
        self.frameQtd.pack()
        #

        ###

        ###

        self.frameTopo.pack(side = 'top')

        ### botões

        # adicionar
        self.botaoConfirmar = tk.Button(self.frameBase, text = 'Adicionar')
        self.botaoConfirmar.bind('<ButtonRelease-1>', self.controle.adicionarEstoqueProduto)
        self.botaoConfirmar.pack(side = 'left')
        #

        # remover
        self.botaoConfirmar = tk.Button(self.frameBase, text = 'Remover')
        self.botaoConfirmar.bind('<ButtonRelease-1>', self.controle.removerEstoqueProduto)
        self.botaoConfirmar.pack(side = 'left')
        #

        # limpar
        self.botaoLimpar = tk.Button(self.frameBase, text = 'Limpar')
        self.botaoLimpar.bind('<ButtonRelease-1>', self.controle.limparEdicaoEstoque)
        self.botaoLimpar.pack(side = 'right')
        #

        ###

        self.frameBase.pack(side = 'bottom')

    ### funções de verificação

    # código
    def verificacao_codigo(self, *args):
        codigo = self.codigo.get()

        aux = ''

        # verificação de tipo de dado
        for numero in codigo:
            if numero.isdigit():
                aux += numero
        #
        
        # verificação de tamanho
        if len(aux) > 4:
            aux = aux[:-1]
        #

        self.codigo.set(aux)
    #

    # qtd
    def verificacao_qtd(self, *args):
        qtd = self.qtd.get()

        aux = ''

        # verificação de tipo de dado
        for numero in qtd:
            if numero.isdigit():
                aux += numero
        #
        
        # verificação de tamanho
        if len(aux) > 3:
            aux = aux[:-1]
        #

        self.qtd.set(aux)
    #

    ###

# Janela de remoção de produto
class LimiteRemocao(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)

        self.controle = controle

        self.geometry('400x300')
        self.title('Remoção de Produto')

        self.frameTopo = tk.Frame(self)
        self.frameBase = tk.Frame(self)

        ### entrada de dados

        # código
        self.frameCodigo = tk.Frame(self.frameTopo)
        self.labelCodigo = tk.Label(self.frameCodigo, text = 'Código:')
        self.codigo = tk.StringVar()
        self.inputCodigo = tk.Entry(self.frameCodigo, textvariable = self.codigo, width = 4)
        self.codigo.trace('w', self.verificacao_codigo)
        self.labelCodigo.pack(side = 'left')
        self.inputCodigo.pack(side = 'right')
        self.frameCodigo.pack()
        #

        ###

        self.frameTopo.pack(side = 'top')

        ### botões

        # confirmar
        self.botaoConfirmar = tk.Button(self.frameBase, text = 'Confirmar')
        self.botaoConfirmar.bind('<ButtonRelease-1>', self.controle.confirmarRemocao)
        self.botaoConfirmar.pack(side = 'left')
        #

        # limpar
        self.botaoLimpar = tk.Button(self.frameBase, text = 'Limpar')
        self.botaoLimpar.bind('<ButtonRelease-1>', self.controle.limparRemocao)
        self.botaoLimpar.pack(side = 'right')
        #

        ###

        self.frameBase.pack(side = 'bottom')

    #  de verificação de código
    def verificacao_codigo(self, *args):
        codigo = self.codigo.get()

        aux = ''

        # verificação de tipo de dado
        for numero in codigo:
            if numero.isdigit():
                aux += numero
        #
        
        # verificação de tamanho
        if len(aux) > 4:
            aux = aux[:-1]
        #

        self.codigo.set(aux)
    #

class ControleProduto():
    def __init__(self):
        self.listaProdutos = []

    ##### CADASTRO DE PRODUTO #####
    def cadastrarProduto(self):
        self.limiteCadastro = LimiteCadastro(self)

    def confirmarCadastro(self, event):
        ### recuperando as informações

        # código
        codigo = self.limiteCadastro.inputCodigo.get()
        if codigo != '': # não é possível converter '' para inteiro!
            codigo = int(codigo)
        #

        # nome
        nome = self.limiteCadastro.inputNome.get()
        #

        # custo
        custoReal = self.limiteCadastro.inputCustoEsq.get()
        if custoReal != '':
            custoReal = int(custoReal)
        custoCentavo = self.limiteCadastro.inputCustoDir.get()
        if custoCentavo != '':
            if len(custoCentavo) == 1:
                custoCentavo += '0'
                custoCentavo = int(custoCentavo)
            else:
                custoCentavo = int(custoCentavo)
            custo = float(custoReal + (custoCentavo / 100))
        else:
            custo = ''
        #

        # preço
        precoReal = self.limiteCadastro.inputPrecoEsq.get()
        if precoReal != '':
            precoReal = int(precoReal)
        precoCentavo = self.limiteCadastro.inputPrecoDir.get()
        if precoCentavo != '':
            if len(precoCentavo) == 1:
                precoCentavo += '0'
                precoCentavo = int(precoCentavo)
            else:
                precoCentavo = int(precoCentavo)
            preco = float(precoReal + (precoCentavo / 100))
        else:
            preco = ''
        #

        # estoque
        estoque = self.limiteCadastro.inputEstoque.get()
        if estoque != '':
            estoque = int(estoque)
        #

        ###

        # fazendo o produto
        if (codigo != '') and (nome != '') and (custo != '') and (preco != '') and (estoque != ''):
            produto = tipo.Produto(codigo, nome, custo, preco, estoque)
        #

            # salvando o produto
            if os.path.isfile('data/produtos.pkl'):
                self.listaProdutos = [] # redundante?
                self.listaProdutos = arquivo.recupera('produtos.pkl', 'list')

                # verifica se o arquivo já existe
                for aux in self.listaProdutos:
                    if aux.codigo == produto.codigo:
                        msg.showerror('Erro!', 'O produto já existe!')

                        return False
                #

                self.listaProdutos.append(produto)
                arquivo.guarda(self.listaProdutos, 'produtos.pkl')
            else: # se é o primeiro produto 
                self.listaProdutos = []
                self.listaProdutos.append(produto)
                arquivo.guarda(self.listaProdutos, 'produtos.pkl')
            #

            msg.showinfo('Sucesso!', 'Produto cadastrado no banco de dados!')

            self.limparCadastro(event)

            return True
        else:
            msg.showwarning('Erro!', 'Todos os campos são obrigatórios!')

    def limparCadastro(self, event):
        self.limiteCadastro.codigo.set('')
        self.limiteCadastro.nome.set('')
        self.limiteCadastro.realCusto.set('')
        self.limiteCadastro.centavoCusto.set('')
        self.limiteCadastro.realPreco.set('')
        self.limiteCadastro.centavoPreco.set('')
        self.limiteCadastro.estoque.set('')
    ###############################

    ##### CONSULTA DE PRODUTO #####
    def consultarProduto(self):
        if not os.path.isfile('data/produtos.pkl'):
            msg.showerror('Erro!', 'Não há produtos cadastrados para a consulta!')
        else:
            self.limiteConsulta = LimiteConsulta(self)

    def confirmarConsulta(self, event):
        # recuperando o código
        codigo = self.limiteConsulta.inputCodigo.get()
        if codigo != '':
            codigo = int(codigo)
        else:
            msg.showerror('Erro!', 'Todos os campos são obrigatórios!')
        #

        # recuperando o produto
        self.listaProdutos = arquivo.recupera('produtos.pkl','list') # só chegou até aqui se havia produtos!
        
        for produto in self.listaProdutos:
            if produto.codigo == codigo:
                msg.showinfo('Sucesso!','É o produto:\n'  \
                                        'Código: {}\n'               \
                                        'Nome: {}\n'                 \
                                        'Custo de produção: R$ {}\n' \
                                        'Preço de venda: R$ {}\n'    \
                                        'Estoque: {}'.format(produto.codigo, 
                                                             produto.nome, 
                                                             produto.custo, 
                                                             produto.preco, 
                                                             produto.estoque))
        
                self.limparConsulta(event)
                
                return True
        #

        # se não havia produto
        msg.showwarning('Erro!','Produto não encontrado!\n\n' \
                        'O código {} não existe no banco de dados.'.format(codigo))
        
        return False
        #

    def limparConsulta(self, event):
        self.limiteConsulta.codigo.set('')

    def imprimirProdutos(self): # relatório de produtos
        if not os.path.isfile('data/produtos.pkl'):
            msg.showerror('Erro!', 'Não há produtos cadastrados para a consulta!')
        else:
            # recuperando os produtos
            self.listaProdutos = arquivo.recupera('produtos.pkl', 'list')
            #

            # imprimindo os produtos
            data_hora = datetime.datetime.now()
            data = format_date(data_hora, format = 'short', locale = 'pt_BR')
            hora = format_time(data_hora, format = 'short', locale = 'pt_BR')

            output = 'Emissão: {} - {}\n\n'.format(data, hora)

            for produto in self.listaProdutos:
                output += '####################\n\n'   \
                          'Código: {}\n'               \
                          'Nome: {}\n'                 \
                          'Custo de produção: R$ {}\n' \
                          'Preço de varejo: R$ {}\n'   \
                          'Estoque: {}\n\n'            \
                          '####################\n\n'.format(produto.codigo,
                                                                 produto.nome,
                                                                 produto.custo,
                                                                 produto.preco,
                                                                 produto.estoque)

            with open('out/estoque.txt', 'w') as txt:
                txt.write(output)
            #

            msg.showinfo('Sucesso!', 'Relatório de estoque salvo em out/estoque.txt!')
    ###############################

    ##### EDIÇÃO DE PRODUTO ##### 
    def editarProduto(self):
        if not os.path.isfile('data/produtos.pkl'):
            msg.showerror('Erro!', 'Não há produtos cadastrados para a edição!')
        else:
            self.limiteEdicao = LimiteEdicao(self)

    def confirmarEdicao(self, event):
        ### recuperando as informações

        # código
        codigo = self.limiteEdicao.inputCodigo.get()
        if codigo != '':
            codigo = int(codigo)
        #

        # custo
        custoReal = self.limiteEdicao.inputCustoEsq.get()
        if custoReal != '':
            custoReal = int(custoReal)
        custoCentavo = self.limiteEdicao.inputCustoDir.get()
        if custoCentavo != '':
            if len(custoCentavo) == 1:
                custoCentavo += '0'
                custoCentavo = int(custoCentavo)
            else:
                custoCentavo = int(custoCentavo)
            novoCusto = float(custoReal + (custoCentavo / 100))
        else:
            novoCusto = ''
        #

        # preço
        precoReal = self.limiteEdicao.inputPrecoEsq.get()
        if precoReal != '':
            precoReal = int(precoReal)
        precoCentavo = self.limiteEdicao.inputPrecoDir.get()
        if precoCentavo != '':
            if len(precoCentavo) == 1:
                precoCentavo += '0'
                precoCentavo = int(precoCentavo)
            else:
                precoCentavo = int(precoCentavo)
            novoPreco = float(precoReal + (precoCentavo / 100))
        else:
            novoPreco = ''
        #

        ###

        # verifica a legibilidade das entradas
        if (codigo == '') or (novoCusto == '') or (novoPreco == ''):
            msg.showerror('Erro!', 'Todos os campos são obrigatórios!')
            
            return False
        #

        # alterando o produto
        self.listaProdutos = arquivo.recupera('produtos.pkl','list')

        for produto in self.listaProdutos:
            if produto.codigo == codigo:
                # verifica se alguma característica se manteve
                if (produto.custo == novoCusto) and (produto.preco == novoPreco):
                    msg.showwarning('Aviso!', 'Nenhuma característica foi alterada.\n\n' \
                                              'O custo e o preço inserido são iguais aos do produto.')
                    
                if (produto.custo == novoCusto) and (produto.preco != novoPreco):
                    msg.showwarning('Aviso!', 'Somente uma característica foi alterada.\n\n' \
                                              'O custo inserido é igual ao do produto.')
                    
                if (produto.custo != novoCusto) and (produto.preco == novoPreco):
                    msg.showwarning('Aviso!', 'Somente uma característica foi alterada.\n\n' \
                                              'O preço inserido é igual ao do produto.')
                #
                    
                produto.custo = novoCusto
                produto.preco = novoPreco

                arquivo.guarda(self.listaProdutos, 'produtos.pkl')

                msg.showinfo('Sucesso!', 'Produto alterado no banco de dados!')

                self.limparEdicao(event)

                return True
        #

        # se o código de produto é inválido
        msg.showwarning('Aviso!', 'Produto não encontrado!\n\n' \
                                  'O código {} não existe no banco de dados.'.format(codigo))
        
        return False
        #

    def limparEdicao(self, event):
        self.limiteEdicao.codigo.set('')
        self.limiteEdicao.realCusto.set('')
        self.limiteEdicao.centavoCusto.set('')
        self.limiteEdicao.realPreco.set('')
        self.limiteEdicao.centavoPreco.set('')
    
    def atualizarEstoque(self):
        if not os.path.isfile('data/produtos.pkl'):
            msg.showerror('Erro!', 'Não há produtos cadastrados para a edição!')
        else:
            self.limiteEdicaoEstoque = LimiteEdicaoEstoque(self)

    def adicionarEstoqueProduto(self, event):
        ### recuperando as informações

        # código
        codigo = self.limiteEdicaoEstoque.inputCodigo.get()
        if codigo != '':
            codigo = int(codigo)
        #

        # qtd
        qtd = self.limiteEdicaoEstoque.inputQtd.get()
        if qtd != '':
            qtd = int(qtd)
        #

        ###

        # verifica a legibilidade das entradas
        if (codigo == '') or (qtd == ''):
            msg.showerror('Erro!', 'Todos os campos são obrigatórios!')
            
            return False
        #

        # alterando o produto
        self.listaProdutos = arquivo.recupera('produtos.pkl','list')

        for produto in self.listaProdutos:
            if produto.codigo == codigo:
                produto.estoque += qtd

                arquivo.guarda(self.listaProdutos, 'produtos.pkl')

                msg.showinfo('Sucesso!', 'Produto alterado no banco de dados!\n' \
                                         'Acrescentados {} {}.'.format(qtd, produto.nome))

                self.limparEdicaoEstoque(event)

                return True
        #

        # se o código de produto é inválido
        msg.showwarning('Aviso!', 'Produto não encontrado!\n\n' \
                                  'O código {} não existe no banco de dados.'.format(codigo))
        
        return False
        #

    def removerEstoqueProduto(self, event):
        ### recuperando as informações

        # código
        codigo = self.limiteEdicaoEstoque.inputCodigo.get()
        if codigo != '':
            codigo = int(codigo)
        #

        # qtd
        qtd = self.limiteEdicaoEstoque.inputQtd.get()
        if qtd != '':
            qtd = int(qtd)
        #

        ###

        # verifica a legibilidade das entradas
        if (codigo == '') or (qtd == ''):
            msg.showerror('Erro!', 'Todos os campos são obrigatórios!')
            
            return False
        #

        # alterando o produto
        self.listaProdutos = arquivo.recupera('produtos.pkl','list')

        for produto in self.listaProdutos:
            if produto.codigo == codigo:
                produto.estoque -= qtd

                arquivo.guarda(self.listaProdutos, 'produtos.pkl')

                msg.showinfo('Sucesso!', 'Produto alterado no banco de dados!\n' \
                                         'Removidos {} {}.'.format(qtd, produto.nome))

                self.limparEdicaoEstoque(event)

                return True
        #

        # se o código de produto é inválido
        msg.showwarning('Aviso!', 'Produto não encontrado!\n\n' \
                                  'O código {} não existe no banco de dados.'.format(codigo))
        
        return False
        #

    def limparEdicaoEstoque(self, event):
        self.limiteEdicaoEstoque.codigo.set('')
        self.limiteEdicaoEstoque.qtd.set('')
    #############################

    ##### REMOÇÃO DE PRODUTO #####
    def removerProduto(self):
        if not os.path.isfile('data/produtos.pkl'):
            msg.showerror('Erro!', 'Não há produtos cadastrados para a remoção!')
        else:
            self.limiteRemocao = LimiteRemocao(self)

    def confirmarRemocao(self, event):
        # recuperando o código
        codigo = self.limiteRemocao.inputCodigo.get()
        if codigo != '':
            codigo = int(codigo)
        else:
            msg.showerror('Erro!', 'Todos os campos são obrigatórios!')
        #

        # recuperando o produto
        self.listaProdutos = arquivo.recupera('produtos.pkl','list') # só chegou até aqui se havia produtos!
        
        for produto in self.listaProdutos:
            if produto.codigo == codigo:
                self.listaProdutos.remove(produto)

                if self.listaProdutos == []: # se era o último produto
                    self.limpezaProdutos() # apaga o arquivo (modo seguro)
                else:
                    arquivo.guarda(self.listaProdutos, 'produtos.pkl')

                    msg.showinfo('Sucesso!', 'Produto removido do banco de dados com sucesso!')
            
                    self.limparRemocao(event)
                    
                    return True
        #

        # se não havia produto
        msg.showwarning('Aviso!','Produto não encontrado!\n\n' \
                                 'O código {} não existe no banco de dados.'.format(codigo))
        
        return False
        #

    def limparRemocao(self, event):
        self.limiteRemocao.codigo.set('')

    def limpezaProdutos(self): # limpeza do banco de dados /!\
        if not os.path.isfile('data/produtos.pkl'):
            msg.showerror('Erro!', 'Não há produtos cadastrados para a limpeza!')
        else:
            os.remove('data/produtos.pkl')

            msg.showinfo('Sucesso!', 'Banco de dados removido da memória.')
    ##############################