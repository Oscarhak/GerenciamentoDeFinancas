from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
from os import walk
import matplotlib.pyplot as plt
import datetime, xlrd

class ativos_q3:
    listaativos_q3 = []
    path = os.getcwd()
    for (dirpath, dirnames, filenames) in walk(path):
        listaativos_q3.extend(filenames)
        break
    cont = 0
    while cont < len(listaativos_q3):
        arquivo = '.xls' in listaativos_q3[cont]
        if arquivo == False:
            listaativos_q3[cont] = ''
        cont += 1
    listaativos_q3 = list(filter(None, listaativos_q3))

class interface:
    inicio = tk.Tk()
    inicio.title("CORRELAÇÃO")

    inicio.geometry("500x500+300+100")
    # inicio.resizable(0, 0)
    # inicio.state("zoomed")

class localizacao_q3:
    frame_informativos_q3 = Frame(interface.inicio)
    frame_cima_q3 = Frame(interface.inicio)
    frame_meio_q3 = Frame(interface.inicio)
    frame_baixo_q3 = Frame(interface.inicio)
    frame_botao_q3 = Frame(interface.inicio)
    frame_barra_q3 = Frame(interface.inicio)

    frame_informativos_q3.pack()
    frame_cima_q3.pack()
    frame_meio_q3.pack()
    frame_baixo_q3.pack()
    frame_botao_q3.pack()
    frame_barra_q3.pack()

class informacoes_q3:
    colocarAtivo_q3 = Label(localizacao_q3.frame_informativos_q3,
                         text='ESCOLHA OS ativos_q3 PARA GERAR O GRÁFICO')

    colocarAtivo_q3.grid(row=0, column=1)

    ativo1_q3 = Label(localizacao_q3.frame_cima_q3,
                   text='ATIVO 1')

    ativo1_q3.grid(row=0, column=0, pady=10, padx=90)

    ativo2_q3 = Label(localizacao_q3.frame_cima_q3,
                   text='ATIVO 2')

    ativo2_q3.grid(row=0, column=2, pady=10, padx=100)

    barra_q3 = ttk.Progressbar(localizacao_q3.frame_barra_q3)

class botao_q3:
    geragrafico_q3_q3 = Button(localizacao_q3.frame_meio_q3, text="Gerar gráfico",
                         anchor=CENTER,
                         command=lambda: grafico_q3()
                         )

    geragrafico_q3_q3.grid(row=10, column=1, pady=10, padx=10)

class escolhaAtivo_q3():
    ativo1_q3 = ttk.Combobox(localizacao_q3.frame_meio_q3, values=ativos_q3.listaativos_q3)
    ativo2_q3 = ttk.Combobox(localizacao_q3.frame_meio_q3, values=ativos_q3.listaativos_q3)
    ativo1_q3.grid(row=0, column=0, pady=10, padx=10)
    ativo2_q3.grid(row=0, column=2, pady=10, padx=10)

def grafico_q3():

    escolha1_q3 = escolhaAtivo_q3.ativo1_q3.get()
    escolha2_q3 = escolhaAtivo_q3.ativo2_q3.get()

    book_q3 = xlrd.open_workbook(escolha1_q3)
    sh_q3 = book_q3.sheet_by_index(0)

    valores_q3 = []
    valores2_q3 = []
    data_q3 = []
    data2_q3 = []
    cont1_q3 = 1

    book2_q3 = xlrd.open_workbook(escolha2_q3)
    sh2_q3 = book2_q3.sheet_by_index(0)

    while cont1_q3 != 450:

        informacoes_q3.barra_q3.pack()
        informacoes_q3.barra_q3.update()

        valor = sh_q3.cell_value(rowx=cont1_q3, colx=1)
        valores_q3.append(valor)

        grafico_q31 = xlrd.open_workbook(escolha1_q3)
        a1 = sh_q3.cell_value(rowx=cont1_q3, colx=0)
        a1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(a1, book_q3.datemode))
        data_q3.append(a1_as_datetime)
        data2_q3.append(a1_as_datetime)

        plt.plot(data_q3, valores_q3, c='b')

        valor2_q3 = sh2_q3.cell_value(rowx=cont1_q3, colx=1)
        valores2_q3.append(valor2_q3)

        plt.plot(data2_q3, valores2_q3, c='r')

        cont1_q3 += 1
        informacoes_q3.barra_q3['value'] = (cont1_q3 * 100 / 450)

    informacoes_q3.barra_q3.pack_forget()

    plt.show()


interface.inicio.mainloop()
