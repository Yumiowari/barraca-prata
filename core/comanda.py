### bibliotecas

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as msg
import os
import datetime
from babel.dates import format_date, format_time

# minhas
import lib.arquivo as arquivo
#

# tipo de dado
import classes.comanda as tipo
#

###

# Janela de cadastro de comanda
class LimiteCadastro(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)

        self.controle = controle

        self.geometry('400x300')
        self.title('Cadastro de Comanda')

        self.frameTopo = tk.Frame(self)
        self.frameBase = tk.Frame(self)
        self.baseDir = tk.Frame(self.frameBase)
        self.baseEsq = tk.Frame(self.frameBase)

        ### entrada de dados

        # nome do produto
        listaNomes = []
        listaProdutos = arquivo.recupera('produtos.pkl', 'list')
        for produto in listaProdutos:
            listaNomes.append(produto.nome)
        
        self.frameNome = tk.Frame(self.frameTopo)
        self.labelNome = tk.Label(self.frameNome, text = 'Nome:')
        self.nome = tk.StringVar()
        self.inputNome = ttk.Combobox(self.frameNome, textvariable = self.nome, values = listaNomes, width = 15)
        self.nome.trace('w', self.verificacao_nome)
        self.labelNome.pack(side = 'left')
        self.inputNome.pack(side = 'right')
        self.frameNome.pack()
        #

        # quantidade
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

        self.frameTopo.pack(side = 'top')

        ### botões

        # adicionar
        self.botaoAdicionar = tk.Button(self.baseEsq, text = 'Adicionar')
        self.botaoAdicionar.bind('<ButtonRelease-1>', self.controle.adicionarProduto)
        self.botaoAdicionar.pack(side = 'top')
        #

        # confirmar
        self.botaoConfirmar = tk.Button(self.baseEsq, text = 'Confirmar')
        self.botaoConfirmar.bind('<ButtonRelease-1>', self.controle.confirmarCadastro)
        self.botaoConfirmar.pack(side = 'bottom')
        #

        # remover
        self.botaoRemover = tk.Button(self.baseDir, text = 'Remover')
        self.botaoRemover.bind('<ButtonRelease-1>', self.controle.removerProduto)
        self.botaoRemover.pack(side = 'top')
        #

        # limpar
        self.botaoLimpar = tk.Button(self.baseDir, text = 'Limpar')
        self.botaoLimpar.bind('<ButtonRelease-1>', self.controle.limparCadastro)
        self.botaoLimpar.pack(side = 'bottom')
        #

        ###

        self.baseEsq.pack(side = 'left')
        self.baseDir.pack(side = 'right')
        self.frameBase.pack(side = 'bottom')

    ### funções de verificação

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

    # quantidade
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

class ControleComanda():
    def __init__(self):
        self.listaProdutos = []
        self.listaComandas = []

    ##### CADASTRO DE COMANDA #####
    def criarComanda(self):
        if not os.path.isfile('data/produtos.pkl'):
            msg.showerror('Erro!', 'Não há produtos cadastrados para o cadastro de comanda!')
        else:
            self.comanda = tipo.Comanda([],0)
            self.limiteCadastro = LimiteCadastro(self)

    def adicionarProduto(self, event):
        ### recuperando as informações

        # nome
        nome = self.limiteCadastro.inputNome.get()
        #

        # quantidade
        qtd = self.limiteCadastro.inputQtd.get()
        if qtd != '':
            qtd = int(qtd)
        #

        ###

        if (nome != '') and (qtd != ''):
            self.produto = None
            self.listaProdutos = arquivo.recupera('produtos.pkl', 'list')

            # busca o produto
            for produto in self.listaProdutos:
                if produto.nome == nome:
                    self.produto = produto
            #
            
            if self.produto != None:
                codigo = self.produto.codigo
                self.comanda.inserir_produto(codigo, qtd)

                msg.showinfo('Sucesso!', '{} {} adicionados à comanda!'.format(qtd,
                                                                        self.produto.nome))
            
                self.limparCadastro(event)
            else: # se não achou
                msg.showerror('Erro!', 'Produto removido após a abertura da janela de cadastro de comanda.')
        
                self.limparCadastro(event)
        else:
            msg.showerror('Erro!', 'Todos os campos são obrigatórios!')

    def removerProduto(self, event):
        ### recuperando as informações

        # nome
        nome = self.limiteCadastro.nome.get()
        #

        # quantidade
        qtd = self.limiteCadastro.inputQtd.get()
        if qtd != '':
            qtd = int(qtd)
        #

        ###

        if (nome != '') and (qtd != ''):
            self.produto = None
            self.listaProdutos = arquivo.recupera('produtos.pkl', 'list')

            # busca o produto
            for produto in self.listaProdutos:
                if produto.nome == nome:
                    self.produto = produto
            #

            if self.produto != None:
                codigo = self.produto.codigo

                self.comanda.remover_produto(codigo, qtd)

                msg.showinfo('Sucesso!', '{} {} removidos da comanda!'.format(qtd, 
                                                                              self.produto.nome))
            else:
                msg.showerror('Erro!', 'Produto removido após a abertura da janela de criação de comanda.')
        else:
            msg.showerror('Erro!', 'Todos os campos são obrigatórios!')

    def confirmarCadastro(self, event):
        # verifica se algum produto não existe mais
        self.listaProdutos = arquivo.recupera('produtos.pkl', 'list')

        flag = False

        for produto in self.comanda.produtos:
            for aux in self.listaProdutos:
                if produto.codigo == aux.codigo:
                    flag = True
        
        if flag == False: # se nunca achou o produto
            msg.showwarning('Aviso!', 'Nenhum produto foi vendido.')

            return False
        #

        # ajusta os estoques, valor a ser cobrado e o lucro
        listaAux = self.comanda.produtos
        
        valor = 0
        lucro = 0

        for produto in self.listaProdutos:
            for aux in listaAux: # produtos na comanda
                if produto.codigo == aux.codigo:
                    produto.estoque -= aux.qtd
                    valor += produto.preco * aux.qtd
                    lucro += (produto.preco - produto.custo) * aux.qtd

        arquivo.guarda(self.listaProdutos, 'produtos.pkl')
        self.comanda.valor = valor
        self.comanda.lucro = lucro
        #

        # guarda a comanda no banco de dados
        data_hora = datetime.datetime.now()
        data = format_date(data_hora, format = 'short', locale = 'pt_BR')
        hora = format_time(data_hora, format = 'short', locale = 'pt_BR')

        if os.path.isfile('data/comandas.pkl'):
            self.listaComandas = arquivo.recupera('comandas.pkl', 'list')
            self.comanda.data = data
            self.comanda.hora = hora
            self.listaComandas.append(self.comanda)
            arquivo.guarda(self.listaComandas, 'comandas.pkl')
        else:
            self.listaComandas = []
            self.comanda.data = data
            self.comanda.hora = hora
            self.listaComandas.append(self.comanda)
            arquivo.guarda(self.listaComandas, 'comandas.pkl')
        #

        msg.showinfo('Sucesso!','Comanda cadastrada com sucesso!')

        msg.showinfo('Sucesso!','É a comanda:\n\n' \
                                'Data: {}\n'       \
                                'Hora: {}\n\n'     \
                                'Valor: {}'.format(self.comanda.data, 
                                                   self.comanda.hora, 
                                                   self.comanda.valor))

        self.limiteCadastro.destroy() # termina a janela!

        return True

    def limparCadastro(self, event):
        self.limiteCadastro.nome.set('')
        self.limiteCadastro.qtd.set('')
    ###############################

    ##### FECHAMENTO DAS COMANDAS #####
    def fechamentoComandas(self):
        if not os.path.isfile('data/comandas.pkl'):
            msg.showerror('Erro!', 'Não há comandas cadastradas para o fechamento do dia!')
        else:
            data_hora = datetime.datetime.now()
            data = format_date(data_hora, format = 'short', locale = 'pt_BR')
            data = data.replace('/', '-') # '/' é proibido em nomes de pastas!
            if not os.path.exists('out/{}'.format(data)):
                os.makedirs('out/{}'.format(data)) # faz o 

                # fazendo o relatório
                output = ''

                listaComandas = arquivo.recupera('comandas.pkl', 'list')

                total = 0
                lucro = 0

                for comanda in listaComandas:
                    output += '###\n\n' \
                              'Hora: {}\n\n'.format(comanda.hora)
                    
                    for produto in comanda.produtos:
                        output += '{} - {}\n'.format(produto.codigo, 
                                                     produto.qtd)
                        
                    output += '\nTotal: R$ {}\n\n' \
                              '###\n\n'.format(comanda.valor)
                    
                    total += comanda.valor
                    lucro += comanda.lucro

                output += '\n\nTotal bruto: {}\n' \
                          'Lucro: {}'.format(total, 
                                             lucro)

                with open('out/{}/controle.txt'.format(data), 'w') as txt:
                    txt.write(output)
                
                os.rename('data/comandas.pkl', 'out/{}/comandas.pkl'.format(data)) # limpa as comandas!
                #

                msg.showinfo('Sucesso!', 'O dia terminou!\n' \
                                         'Relatório salvo em out/{}/controle.txt.'.format(data))
            else:
                msg.showerror('Erro!', 'O dia já fechou.\n' \
                                       'Deixe essas para amanhã!')
    ###################################