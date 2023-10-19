### bibliotecas

import tkinter as tk
import os

###

# janelas
import core.produto as produto
import core.comanda as comanda
import core.faturamento as faturamento
#

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle

        self.root = root
        self.root.geometry('400x300')
        self.root.title('Controle Financeiro')

        ##### barra de menu
        
        self.menuPrincipal = tk.Menu(self.root)

        self.produtoMenu = tk.Menu(self.menuPrincipal, tearoff = 0)
        self.comandaMenu = tk.Menu(self.menuPrincipal, tearoff = 0)
        self.faturamentoMenu = tk.Menu(self.menuPrincipal, tearoff = 0)

        ### dropdowns

        # produto
        self.produtoMenu.add_command(label = 'Cadastro', command = self.controle.cadastrarProduto)
        
        self.consultaSubMenu = tk.Menu(self.produtoMenu, tearoff = 0)
        self.produtoMenu.add_cascade(label = 'Consulta', menu = self.consultaSubMenu)
        self.consultaSubMenu.add_command(label = 'Individual', command = self.controle.consultarProduto)
        self.consultaSubMenu.add_command(label = 'Geral', command = self.controle.imprimirEstoque)

        self.edicaoSubMenu = tk.Menu(self.produtoMenu, tearoff = 0)
        self.produtoMenu.add_cascade(label = 'Edição', menu = self.edicaoSubMenu)
        self.edicaoSubMenu.add_command(label = 'Produto', command = self.controle.editarProduto)
        self.edicaoSubMenu.add_command(label = 'Estoque', command = self.controle.atualizarEstoque)

        self.remocaoSubMenu = tk.Menu(self.produtoMenu, tearoff = 0)
        self.produtoMenu.add_cascade(label = 'Remoção', menu = self.remocaoSubMenu)
        self.remocaoSubMenu.add_command(label = 'Única', command = self.controle.removerProduto)
        self.remocaoSubMenu.add_command(label = 'Limpeza', command = self.controle.limpezaProdutos)

        self.menuPrincipal.add_cascade(label = 'Produto', menu = self.produtoMenu)
        #

        # comanda
        self.comandaMenu.add_command(label = 'Cria', command = self.controle.criarComanda)
        self.comandaMenu.add_command(label = 'Fechamento', command = self.controle.fechamentoComandas)

        self.menuPrincipal.add_cascade(label = 'Comanda', menu = self.comandaMenu)
        #

        # faturamento
        self.faturamentoMenu.add_command(label = 'Imprime', command = self.controle.imprimirFaturamento)

        self.menuPrincipal.add_cascade(label = 'Faturamento', menu = self.faturamentoMenu)
        #

        ###

        #####

        self.frameBase = tk.Frame(self.root)

        # botões
        self.botaoComanda = tk.Button(self.frameBase, text = 'Vender')
        self.botaoComanda.bind('<ButtonRelease-1>', self.controle.bypassCriarComanda)
        self.botaoComanda.pack(side = 'left')

        self.botaoEntrada = tk.Button(self.frameBase, text = 'Entrada')
        self.botaoEntrada.bind('<ButtonRelease-1>', self.controle.bypassAtualizarEstoque)
        self.botaoEntrada.pack(side = 'right')
        #

        self.frameBase.pack(side = 'bottom')

        root.config(menu = self.menuPrincipal)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.limite = LimitePrincipal(self.root, self)

        # controles
        self.ctrlProduto = produto.ControleProduto()
        self.ctrlComanda = comanda.ControleComanda()
        self.ctrlFaturamento = faturamento.ControleFaturamento()
        #

        self.root.mainloop()

    ### funções

    # produto
    def cadastrarProduto(self):
        self.ctrlProduto.cadastrarProduto()

    def consultarProduto(self):
        self.ctrlProduto.consultarProduto()

    def imprimirEstoque(self):
        self.ctrlProduto.imprimirProdutos()

    def editarProduto(self):
        self.ctrlProduto.editarProduto()

    def removerProduto(self):
        self.ctrlProduto.removerProduto()

    def limpezaProdutos(self):
        self.ctrlProduto.limpezaProdutos()

    def atualizarEstoque(self):
        self.ctrlProduto.atualizarEstoque()

    def bypassAtualizarEstoque(self, event):
        self.ctrlProduto.atualizarEstoque()
    #

    # comanda
    def criarComanda(self):
        self.ctrlComanda.criarComanda()

    def bypassCriarComanda(self, event):
        self.ctrlComanda.criarComanda()

    def fechamentoComandas(self):
        self.ctrlComanda.fechamentoComandas()
    #

    # faturamento
    def imprimirFaturamento(self):
        self.ctrlFaturamento.imprimirFaturamento()
    #

    ###

def main():
    try:
        # adiciona os diretórios ignorados pelo github
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('out'):
            os.makedirs('out')
        #

        c = ControlePrincipal()
    except KeyboardInterrupt:
        print("\nEncerrou por KeyboardInterrupt.")

main()