# bibliotecas
import pickle as pkl
import os
#

def guarda(lista, nome):
    with open('data/{}'.format(nome), 'wb') as arquivo:
        pkl.dump(lista, arquivo)

def recupera(nome, tipo):
    if os.path.isfile('data/{}'.format(nome)):
        with open('data/{}'.format(nome), 'rb') as arquivo:
            if tipo == 'list':
                return list(pkl.load(arquivo))
            elif tipo == 'dict':
                return dict(pkl.load(arquivo))
            else:
                print('Erro: Tipo de estrutura de dados inexistente!')
    else:
        if tipo == 'list':
            return []
        elif tipo == 'dict':
            return {}
        else:
            print('Erro: Tipo de estrutura de dados inexistente!')

def recuperaAlt(caminho, tipo):
    if os.path.isfile('{}'.format(caminho)):
        with open('{}'.format(caminho), 'rb') as arquivo:
            if tipo == 'list':
                return list(pkl.load(arquivo))
            elif tipo == 'dict':
                return dict(pkl.load(arquivo))
            else:
                print('Erro: Tipo de estrutura de dados inexistente!')
    else:
        if tipo == 'list':
            return []
        elif tipo == 'dict':
            return {}
        else:
            print('Erro: Tipo de estrutura de dados inexistente!')