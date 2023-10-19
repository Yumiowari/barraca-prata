### bibliotecas

from tkinter import messagebox as msg
import os
from datetime import datetime, timedelta # timedelta para facilitar a incrementação das datas!
from babel.dates import format_date, format_time

# minhas
import lib.arquivo as arquivo
#

###

class ControleFaturamento():
    def __init__(self):
        self.listaComandas = []

    def imprimirFaturamento(self):
        valor = 0
        lucro = 0

        data_hora = datetime.today()
        mes = data_hora.month
        data = format_date(data_hora, format = 'short', locale = 'pt_BR')
        data = data.replace('/', '-')

        if os.path.isfile('out/{}/faturamento.txt'.format(data)):
            msg.showerror('Erro!', 'O faturamento do mês já foi impresso!')

            return False

        # retrocede até o começo do mês
        while data_hora.day > 1:
            self.listaComandas = arquivo.recuperaAlt('out/{}/comandas.pkl'.format(data), 'list')

            data_hora = data_hora - timedelta(days = 1)
            data = format_date(data_hora, format = 'short', locale = 'pt_BR')
            data = data.replace('/', '-')

            for comanda in self.listaComandas:
                valor += comanda.valor
                lucro += comanda.lucro
        #

        if (valor == 0) or (lucro == 0): # se não haviam comandas
            msg.showerror('Erro!','Nenhuma comanda foi vendida ainda!')

            return False

        data_hora = datetime.now()
        data = format_date(data_hora, format = 'short', locale = 'pt_BR')
        hora = format_time(data_hora, format = 'short', locale = 'pt_BR')

        output = 'Emissão: {} - {}\n\n' \
                 'Mês: {}\n'            \
                 'Faturamento: {}\n'    \
                 'Lucro: {}\n'.format(data, hora,
                                          mes,
                                          valor,
                                          lucro)
            
        data = data.replace('/', '-')
        
        with open('out/{}/faturamento.txt'.format(data), 'w') as txt:
            txt.write(output)

        msg.showinfo('Sucesso!', 'Relatório do mês salvo em out/{}/faturamento.txt.'.format(data))

        return True

        

    