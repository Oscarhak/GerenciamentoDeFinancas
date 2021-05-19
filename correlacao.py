from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
import yfinance as yf
import os
from os import walk
import matplotlib.pyplot as plt
import datetime, xlrd
from PIL import Image, ImageTk
from matplotlib import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from openpyxl import Workbook, load_workbook
import pandas as pd
import shutil
import re

#UNIVERSAL #06c767ativos_ja_comprados.dicionarioOrdemCrescente[[key for key in ativos_ja_comprados.dicionarioOrdemCrescente.keys()][1]]

class interface_ativos:
    inicio = tk.Tk()
    inicio.title("CORRELAÇÃO")

    inicio.geometry("500x500+300+100")
    #inicio.resizable(0, 0)
    inicio.state("zoomed")
    inicio.configure(bg='#FFFFFF')

class frames_universal_ativos:
    
    frameBarraSuperior = Frame(interface_ativos.inicio, width=1310, height=75,
                               bg='#FFFFFF',
                               highlightbackground='#DCDCDC', highlightthickness=0.5)
    frameSaldo = Frame(interface_ativos.inicio, width=220, height=770,
                               bg='#FFFFFF',
                               highlightbackground='#DCDCDC', highlightthickness=0.5)
    frameAtivosEmHistorico = Frame(interface_ativos.inicio, width=600, height=500,
                               bg='#FFFFFF')

    frameAtivosEmHistorico.place(x=600,y=90)
    frameSaldo.place(x=-3, y=74)
    frameBarraSuperior.place(x=-3, y=0)

class barra_universal_ativos:

    barraProgresso = ttk.Progressbar(interface_ativos.inicio)

#CORRELAÇÃO

class ativos_correlacao:

    listaAtivos = []
    path = 'ativos'
    for (dirpath, dirnames, filenames) in walk(path):
      listaAtivos.extend(filenames)
      break
    cont = 0
    while cont < len(listaAtivos):
        arquivo = '.xlsx' in listaAtivos[cont]
        if arquivo == False:
          listaAtivos[cont] = ''
        cont += 1
    listaAtivos = list(filter(None, listaAtivos))

class informacoes_correlacao:

    resultadoCorrelacao = Label(interface_ativos.inicio,
                   text='', font=("Finance", 10), foreground='#696969',
                                bg='#FFFFFF')

    significadoCorrelacao = Label(interface_ativos.inicio,
                   text='', font=("Finance", 18), foreground='#696969',
                                  bg='#FFFFFF')

    significadoCorrelacao.place(x=330, y=650)

    resultadoCorrelacao.place(x=250, y=700)

class botao_correlacao:

    imagem_correlacao = PhotoImage(file='imagens\\button_correlacao-entre-ativos.png')
    correlacao = Button(interface_ativos.inicio, image=imagem_correlacao,
                      command=lambda: funcoes.interfaceCorrelacao(self=None),
                      bg='#FFFFFF',
                      bd=0)
    correlacao.place(x=250, y=600)

    imagem_update = PhotoImage(file='imagens\\button_atualizar.png')
    update = Button(interface_ativos.inicio, image=imagem_update,
                    command=lambda: funcoes.atualizar(self=None),
                    bg='#FFFFFF',
                    bd=0
                      )
    update.place(x=1170,y=700)

    imagem_limpar = PhotoImage(file='imagens\\vassoura.png')
    limparCorrelacao = Button(interface_ativos.inicio,
                              command=lambda: [informacoes_correlacao.significadoCorrelacao.place_forget(),
                                               informacoes_correlacao.resultadoCorrelacao.place_forget(),
                                               funcoes.limparCorrelacao(self=None)],
                              image=imagem_limpar,
                              bg='#FFFFFF',
                              bd=0)

    imagem_fechar = PhotoImage(file='imagens\\botao-x.png')
    fecharCorrelacao = Button(interface_ativos.inicio,
                              command=lambda: funcoes.sairCorrelacao(self=None),
                              image=imagem_fechar,
                              bg='#06c767',
                              bd=0)

#CADASTRO ATIVOS

class botao_cadastro:

    imagemAdicionarAtivo = PhotoImage(file='imagens\\button_adicionar_ativo.png')
    adicionarAtivo = Button(interface_ativos.inicio, image=imagemAdicionarAtivo,
                          command=lambda: funcoes.buscarInformacao(self=None),
                            bg='#FFFFFF',
                            bd=0
                          )
    adicionarAtivo.place(x=1250, y=30)

    imagem_fechar = PhotoImage(file='imagens\\botao-x.png')
    fecharCadastro = Button(interface_ativos.inicio,
                           command=lambda: funcoes.sairAdicionarAtivo(self=None),
                           image=imagem_fechar,
                           bg='#06c767',
                           bd=0)

#GRAFICOS

class ativos_graficos:

    listaativos_graficos = []
    path = os.getcwd()

    for (dirpath, dirnames, filenames) in walk(path):

        listaativos_graficos.extend(filenames)
        break
    cont = 0

    while cont < len(listaativos_graficos):

        arquivo = '.xlsx' in listaativos_graficos[cont]

        if arquivo == False:

            listaativos_graficos[cont] = ''
        cont += 1

    listaativos_graficos = list(filter(None, listaativos_graficos))

class botao_graficos:

    imagemGrafico = PhotoImage(file='imagens\\button_graficos.png')
    geragrafico_graficos = Button(interface_ativos.inicio, image=imagemGrafico,
                         command=lambda: funcoes.grafico(self=None),
                                  bg = '#FFFFFF',bd = 0
                         )
    geragrafico_graficos.place(x=1150, y=30)

    imagem_fechar = PhotoImage(file='imagens\\botao-x.png')
    fecharGrafico = Button(interface_ativos.inicio,
                              command=lambda: funcoes.sairGrafico(self=None),
                              image=imagem_fechar,
                              bg='#06c767',
                              bd=0)

#CORPO

class ativos_ja_comprados:

    leitura = pd.read_excel('Dados\\dadosFinanceiros.xlsx', 'acoes')
    array = np.asarray(leitura)
    array = np.delete(array, (0), axis=1)
    matriz = pd.DataFrame(array)
    analise = []
    cont = 0
    while cont < len(array):
        analise.append(array[cont, 0])
        cont += 1

    listaSemRepeticao = []
    for i in analise:
        if i not in listaSemRepeticao:
            listaSemRepeticao.append(i)

    cont = 0
    quantidadeDeNomes = len(listaSemRepeticao)
    dicionario = {}

    while cont < len(listaSemRepeticao):
        soma = 0
        cont1 = 0

        if bool(dicionario) == False:
            dicionario = {listaSemRepeticao[cont]: 0}

        else:
            dicionario[listaSemRepeticao[cont]] = 0

        while cont1 < len(array):
            if listaSemRepeticao[cont] == array[cont1, 0]:
                soma += int(array[cont1, 2])
                dicionario[listaSemRepeticao[cont]] = soma
            cont1 += 1
        cont += 1
    dicionarioOrdemCrescente = {k: v for k, v in
                sorted(dicionario.items(), key=lambda item: item[1], reverse=True)}
    cont2 = 0
    dicionarioValorAcoes = {}

    while cont2 < len(listaSemRepeticao):
        soma = 0
        cont3 = 0
        if bool(dicionarioValorAcoes) == False:
            dicionarioValorAcoes = {listaSemRepeticao[cont2]: 0}
        else:
            dicionarioValorAcoes[listaSemRepeticao[cont2]] = 0
        while cont3 < len(array):
            if listaSemRepeticao[cont2] == array[cont3, 0]:
                somaParcial = float(array[cont3, 1]) * float(array[cont3, 2])
                soma += somaParcial
                dicionarioValorAcoes[listaSemRepeticao[cont2]] = soma
            cont3 += 1
        cont2 += 1
    dicionarioOrdemCrescenteDosValores= {k: v for k, v in
                sorted(dicionarioValorAcoes.items(), key=lambda item: item[1], reverse=True)}

class informativos_corpo:

    minhasAcoes = Label(interface_ativos.inicio, text='Minhas acoes',
                                   font=('Finance', 18),
                                   bg='#FFFFFF',
                                   foreground='#696969',
                                   bd=0)

    totalNegocios = Label(interface_ativos.inicio, text=str(len(ativos_ja_comprados.dicionarioOrdemCrescente.keys())-1)
                                                        +' Negocio',
                        font=('Finance', 10, 'italic'),
                        bg='#FFFFFF',
                        foreground='#696969',
                        bd=0)

    totalAtivos = Label(interface_ativos.inicio, text=str(sum(ativos_ja_comprados.dicionarioOrdemCrescente.values()))\
                                                        + ' Ativo',
                          font=('Finance', 10, 'italic'),
                          bg='#FFFFFF',
                          foreground='#696969',
                          bd=0)

    minhasAcoes.place(x=270, y=105)
    totalNegocios.place(x=455, y=95)
    totalAtivos.place(x=455, y=115)

class ativos_adquiridos:

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) < 0 \
            or str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][0]) == 'nan':
        ativoAdquirido = Label(interface_ativos.inicio,bd=0)
        quantidadeAtivo = Label(interface_ativos.inicio,bd=0)
        quantidadeAtivo.place(x=850, y=100)
        ativoAdquirido.place(x=650, y=100)

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 0 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][0]) != 'nan':
        nomeDoAtivo = [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][0]
        ativoAdquirido = Label(frames_universal_ativos.frameAtivosEmHistorico,
                               font=('Finance', 18),
                               text=[[key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][0]],
                               bg='#FFFFFF',
                               foreground='#696969',
                               bd=0)
        quantidadeAtivo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                               font=('Finance', 18),
                               text='{:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(ativos_ja_comprados.dicionarioValorAcoes.values()))+' %',
                               bg='#FFFFFF',
                               foreground='#696969',
                               bd=0)
        valorAtivo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                font=('Finance', 18),
                                text='R${:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]),
                                bg='#FFFFFF',
                                foreground='#696969',
                                bd=0)
        valorAtivo.place(x=270, y=10)
        quantidadeAtivo.place(x=170, y=10)
        ativoAdquirido.place(x=50, y=10)

        legenda = Canvas(frames_universal_ativos.frameAtivosEmHistorico, width=20, height=15, bg='darkgreen')
        legenda.place(x=15, y=15)

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 1 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][1]) != 'nan':
        nomeDoAtivo = [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][1]
        ativoAdquiridoSegundo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                           font=('Finance', 18),
                           text=[[key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][1]],
                           bg='#FFFFFF',
                           foreground='#696969',
                           bd=0)
        quantidadeAtivoSegundo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                font=('Finance', 18),
                                text='{:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(ativos_ja_comprados.dicionarioValorAcoes.values()))+' %',
                                bg='#FFFFFF',
                                foreground='#696969',
                                bd=0)
        valorAtivoSegundo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                           font=('Finance', 18),
                           text='R${:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]),
                           bg='#FFFFFF',
                           foreground='#696969',
                           bd=0)
        valorAtivoSegundo.place(x=270, y=55)
        quantidadeAtivoSegundo.place(x=170, y=55)
        ativoAdquiridoSegundo.place(x=50, y=55)

        legendaSegunda = Canvas(frames_universal_ativos.frameAtivosEmHistorico, width=20, height=15, bg='limegreen')
        legendaSegunda.place(x=15, y=60)

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 2 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][2]) != 'nan':
        nomeDoAtivo = [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][2]
        ativoAdquiridoTerceiro = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                  font=('Finance', 18),
                                  text=[[key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][2]],
                                  bg='#FFFFFF',
                                  foreground='#696969',
                                  bd=0)
        quantidadeAtivoTerceiro = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                font=('Finance', 18),
                                text='{:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(ativos_ja_comprados.dicionarioValorAcoes.values()))+' %',
                                bg='#FFFFFF',
                                foreground='#696969',
                                bd=0)
        valorAtivoTerceiro = Label(frames_universal_ativos.frameAtivosEmHistorico,
                           font=('Finance', 18),
                           text='R${:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]),
                           bg='#FFFFFF',
                           foreground='#696969',
                           bd=0)
        valorAtivoTerceiro.place(x=270, y=100)
        quantidadeAtivoTerceiro.place(x=170, y=100)
        ativoAdquiridoTerceiro.place(x=50, y=100)

        legendaTerceira = Canvas(frames_universal_ativos.frameAtivosEmHistorico, width=20, height=15, bg='aquamarine')
        legendaTerceira.place(x=15, y=105)

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 3 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][3]) != 'nan':
        nomeDoAtivo = [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][3]
        ativoAdquiridoQuarto = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                   font=('Finance', 18),
                                   text=[[key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][3]],
                                   bg='#FFFFFF',
                                   foreground='#696969',
                                   bd=0)
        quantidadeAtivoQuarto = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                font=('Finance', 18),
                                text='{:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(ativos_ja_comprados.dicionarioValorAcoes.values()))+' %',
                                bg='#FFFFFF',
                                foreground='#696969',
                                bd=0)
        valorAtivoQuarto = Label(frames_universal_ativos.frameAtivosEmHistorico,
                           font=('Finance', 18),
                           text='R${:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]),
                           bg='#FFFFFF',
                           foreground='#696969',
                           bd=0)
        valorAtivoQuarto.place(x=270, y=145)
        quantidadeAtivoQuarto.place(x=170, y=145)
        ativoAdquiridoQuarto.place(x=50, y=145)

        legendaQuarto = Canvas(frames_universal_ativos.frameAtivosEmHistorico, width=20, height=15, bg='goldenrod')
        legendaQuarto.place(x=15, y=150)

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 4 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][4]) != 'nan':
        nomeDoAtivo = [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][4]
        ativoAdquiridoQuinto = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                 font=('Finance', 18),
                                 text=[[key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][4]],
                                 bg='#FFFFFF',
                                 foreground='#696969',
                                 bd=0)
        quantidadeAtivoQuinto = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                font=('Finance', 18),
                                text='{:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(ativos_ja_comprados.dicionarioValorAcoes.values()))+' %',
                                bg='#FFFFFF',
                                foreground='#696969',
                                bd=0)
        valorAtivoQuinto = Label(frames_universal_ativos.frameAtivosEmHistorico,
                           font=('Finance', 18),
                           text='R${:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]),
                           bg='#FFFFFF',
                           foreground='#696969',
                           bd=0)
        valorAtivoQuinto.place(x=270, y=190)
        quantidadeAtivoQuinto.place(x=170, y=190)
        ativoAdquiridoQuinto.place(x=50, y=190)

        legendaQuinto = Canvas(frames_universal_ativos.frameAtivosEmHistorico, width=20, height=15, bg='darkviolet')
        legendaQuinto.place(x=15, y=195)

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 5 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][5]) != 'nan':
        nomeDoAtivo = [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][5]
        ativoAdquiridoSexto = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                 font=('Finance', 18),
                                 text=[[key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][5]],
                                 bg='#FFFFFF',
                                 foreground='#696969',
                                 bd=0)
        quantidadeAtivoSexto = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                font=('Finance', 18),
                                text='{:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(ativos_ja_comprados.dicionarioValorAcoes.values()))+' %',
                                bg='#FFFFFF',
                                foreground='#696969',
                                bd=0)
        valorAtivoSexto = Label(frames_universal_ativos.frameAtivosEmHistorico,
                           font=('Finance', 18),
                           text='R${:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]),
                           bg='#FFFFFF',
                           foreground='#696969',
                           bd=0)
        valorAtivoSexto.place(x=270, y=235)
        quantidadeAtivoSexto.place(x=170, y=235)
        ativoAdquiridoSexto.place(x=50, y=235)

        legendaSexto = Canvas(frames_universal_ativos.frameAtivosEmHistorico, width=20, height=15, bg='mediumvioletred')
        legendaSexto.place(x=15, y=240)

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 6 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][6]) != 'nan':
        nomeDoAtivo = [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][6]
        ativoAdquiridoSetimo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                font=('Finance', 18),
                                text=[[key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][6]],
                                bg='#FFFFFF',
                                foreground='#696969',
                                bd=0)
        quantidadeAtivoSetimo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                font=('Finance', 18),
                                text='{:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(ativos_ja_comprados.dicionarioValorAcoes.values()))+' %',
                                bg='#FFFFFF',
                                foreground='#696969',
                                bd=0)
        valorAtivoSetimo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                           font=('Finance', 18),
                           text='R${:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]),
                           bg='#FFFFFF',
                           foreground='#696969',
                           bd=0)
        valorAtivoSetimo.place(x=270, y=280)
        quantidadeAtivoSetimo.place(x=170, y=280)
        ativoAdquiridoSetimo.place(x=50, y=280)

        legendaSetimo = Canvas(frames_universal_ativos.frameAtivosEmHistorico, width=20, height=15, bg='orange')
        legendaSetimo.place(x=15, y=285)

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 7 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][7]) != 'nan':
        nomeDoAtivo = [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][7]
        ativoAdquiridoOitavo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                 font=('Finance', 18),
                                 text=[[key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][7]],
                                 bg='#FFFFFF',
                                 foreground='#696969',
                                 bd=0)
        quantidadeAtivoOitavo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                font=('Finance', 18),
                                text='{:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(ativos_ja_comprados.dicionarioValorAcoes.values()))+' %',
                                bg='#FFFFFF',
                                foreground='#696969',
                                bd=0)
        valorAtivoOitavo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                           font=('Finance', 18),
                           text='R${:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]),
                           bg='#FFFFFF',
                           foreground='#696969',
                           bd=0)
        valorAtivoOitavo.place(x=270, y=325)
        quantidadeAtivoOitavo.place(x=170, y=325)
        ativoAdquiridoOitavo.place(x=50, y=325)

        legendaOitavo = Canvas(frames_universal_ativos.frameAtivosEmHistorico, width=20, height=15, bg='khaki')
        legendaOitavo.place(x=15, y=330)

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 8 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][8]) != 'nan':
        nomeDoAtivo = [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][8]
        ativoAdquiridoNono = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                 font=('Finance', 18),
                                 text=[[key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][8]],
                                 bg='#FFFFFF',
                                 foreground='#696969',
                                 bd=0)
        quantidadeAtivoNono = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                font=('Finance', 18),
                                text='{:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(ativos_ja_comprados.dicionarioValorAcoes.values()))+' %',
                                bg='#FFFFFF',
                                foreground='#696969',
                                bd=0)
        valorAtivoNono = Label(frames_universal_ativos.frameAtivosEmHistorico,
                           font=('Finance', 18),
                           text='R${:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]),
                           bg='#FFFFFF',
                           foreground='#696969',
                           bd=0)
        valorAtivoNono.place(x=270, y=370)
        quantidadeAtivoNono.place(x=170, y=370)
        ativoAdquiridoNono.place(x=50, y=370)

        legendaNono = Canvas(frames_universal_ativos.frameAtivosEmHistorico, width=20, height=15, bg='peru')
        legendaNono.place(x=15, y=375)

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 9 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][9]) != 'nan':
        nomeDoAtivo = [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][9]
        ativoAdquiridoDecimo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                 font=('Finance', 18),
                                 text=[[key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][9]],
                                 bg='#FFFFFF',
                                 foreground='#696969',
                                 bd=0)
        quantidadeAtivoDecimo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                font=('Finance', 18),
                                text='{:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(ativos_ja_comprados.dicionarioValorAcoes.values()))+' %',
                                bg='#FFFFFF',
                                foreground='#696969',
                                bd=0)
        valorAtivoDecimo = Label(frames_universal_ativos.frameAtivosEmHistorico,
                           font=('Finance', 18),
                           text='R${:.2f}'.format(ativos_ja_comprados.dicionarioValorAcoes[nomeDoAtivo]),
                           bg='#FFFFFF',
                           foreground='#696969',
                           bd=0)
        valorAtivoDecimo.place(x=270, y=415)
        quantidadeAtivoDecimo.place(x=170, y=415)
        ativoAdquiridoDecimo.place(x=50, y=415)

        legendaDecimo = Canvas(frames_universal_ativos.frameAtivosEmHistorico, width=20, height=15, bg='saddlebrown')
        legendaDecimo.place(x=15, y=420)

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 11:
        cont = 10
        valorDosOutrosAtivos = 0
        while cont < len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores):
            nomeDoAtivo = [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][cont]
            valorDosOutrosAtivos += ativos_ja_comprados.dicionarioOrdemCrescenteDosValores[nomeDoAtivo]
            cont += 1
        ativoAdquiridoOutros = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                 font=('Finance', 18),
                                 text='Outros',
                                 bg='#FFFFFF',
                                 foreground='#696969',
                                 bd=0)
        quantidadeAtivoOutros = Label(frames_universal_ativos.frameAtivosEmHistorico,
                                font=('Finance', 18),
                                text='{:.2f}'.format(valorDosOutrosAtivos*100
                                    /sum(ativos_ja_comprados.dicionarioValorAcoes.values()))+' %',
                                bg='#FFFFFF',
                                foreground='#696969',
                                bd=0)
        valorAtivoOutros = Label(frames_universal_ativos.frameAtivosEmHistorico,
                           font=('Finance', 18),
                           text='R${:.2f}'.format(valorDosOutrosAtivos),
                           bg='#FFFFFF',
                           foreground='#696969',
                           bd=0)
        valorAtivoOutros.place(x=270, y=460)
        quantidadeAtivoOutros.place(x=170, y=460)
        ativoAdquiridoOutros.place(x=50, y=460)

        legendaDecimo = Canvas(frames_universal_ativos.frameAtivosEmHistorico, width=20, height=15, bg='gray')
        legendaDecimo.place(x=15, y=465)

class contagemDeAtivosParaOGrafico:

    global dadosQuantidade

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) == 0 \
            or str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][0]) == 'nan':
        dadosQuantidade = [0]

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 0 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][0]) != 'nan':
        dadosQuantidade = [ativos_ja_comprados.dicionarioOrdemCrescenteDosValores
                           [[key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][0]]]

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 1 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][1]) != 'nan':
        dadosQuantidade.append(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores[
                                   [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][1]])

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 2 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][2]) != 'nan':
        dadosQuantidade.append(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores[
                                   [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][2]])

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 3 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][3]) != 'nan':
        dadosQuantidade.append(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores[
                                   [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][3]])

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 4 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][4]) != 'nan':
        dadosQuantidade.append(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores[
                                   [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][4]])

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 5 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][5]) != 'nan':
        dadosQuantidade.append(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores[
                                   [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][5]])

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 6 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][6]) != 'nan':
        dadosQuantidade.append(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores[
                                   [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][6]])

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 7 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][7]) != 'nan':
        dadosQuantidade.append(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores[
                                   [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][7]])

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 8 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][8]) != 'nan':
        dadosQuantidade.append(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores[
                                   [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][8]])

    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 9 \
            and str([key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][9]) != 'nan':
        dadosQuantidade.append(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores[
                                   [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][9]])
    if len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores) > 11:
        cont = 10
        valorDosOutrosAtivos = 0
        while cont < len(ativos_ja_comprados.dicionarioOrdemCrescenteDosValores):
            nomeDoAtivo = [key for key in ativos_ja_comprados.dicionarioOrdemCrescenteDosValores.keys()][cont]
            valorDosOutrosAtivos += ativos_ja_comprados.dicionarioOrdemCrescenteDosValores[nomeDoAtivo]
            cont+=1
        dadosQuantidade.append(valorDosOutrosAtivos)

class grafico_dos_ativos_tela:

    font = {'family': 'finance',
            'weight': 'bold',
            'size': 13}
    plt.rc('font', **font)
    cores = ('darkgreen','limegreen','aquamarine','goldenrod','darkviolet',
             'mediumvioletred','orange','khaki','peru','saddlebrown','gray')

    #textprops=dict(color='w'),autopct='%0.0f%%'
    plt.figure(figsize=(0.2, 0.2))
    fig1, axl = plt.subplots()
    c2 = axl.pie(dadosQuantidade,shadow=False, colors=cores)
    fig1.patch.set_facecolor('none')
    fig1.savefig('temp.png', facecolor=fig1.get_facecolor(), edgecolor='none')

    canvas_width = 300
    canvas_height = 300

    canvas = Canvas(interface_ativos.inicio, bd=0,
                    highlightthickness=0, width=canvas_width, height=canvas_height,
                    bg='#FFFFFF')
    canvas.place(x=250, y=180)

    image = PhotoImage(file='temp.png')
    image_id2 = canvas.create_image(143, 147, image=image)

    image2 = PhotoImage(file='imagens\\circulo_branco.png')
    image_id = canvas.create_image(150, 150, image=image2)

#BARRA DE PATRIMONIO

class informativos_patrimonio:

    quantidadeDeAcoes = Label(interface_ativos.inicio, text='Total em acoes',
                              font=('Finance',15),
                              bg='#FFFFFF',
                              foreground='#696969',
                              bd=0)

    quantidadeDePatrimonio = Label(interface_ativos.inicio, text='Total Patrimonio',
                              font=('Finance', 13),
                              bg='#FFFFFF',
                              foreground='#696969',
                              bd=0)

    quantidadeDeAcoes.place(x=30, y=100)
    quantidadeDePatrimonio.place(x=30, y=200)

class valores_patrimonio:

    valorAcoes = Label(interface_ativos.inicio, text='R$ {:.2f}'.format(sum(ativos_ja_comprados.dicionarioValorAcoes.values())),
                                   font=('Finance', 20),
                                   bg='#FFFFFF',
                                   foreground='#696969',
                                   bd=0)

    valorAcoes.place(x=30, y=130)

#COMPRA DE ATIVOS

class botao_compra_de_ativo:

    imagem_compra = PhotoImage(file='imagens\\button_comprei-ativo.png')

    comprei = Button(interface_ativos.inicio, image=imagem_compra,
                      command=lambda: funcoes.compra(self=None),
                      bg='#FFFFFF',
                      bd=0
                      )

    comprei.place(x=30, y=650)

    imagemFechar = PhotoImage(file='imagens\\botao-x.png')
    fechar = Button(interface_ativos.inicio,
                    image=imagemFechar,
                    bg='#06c767', bd=0,)

#FUNÇÕES

class funcoes:

    def interfaceCorrelacao(self):

        global ativo1
        global ativo2
        global frameAvisos
        global avisoAtivo1
        global avisoAtivo2
        global igualdade

        #CANVAS
        IMAGE_PATH = 'imagens\\fundo_avisos.png'
        WIDTH, HEIGTH = 200, 230

        frameAvisos = tk.Canvas(interface_ativos.inicio, width=200, height=230,
                                bg='#FFFFFF',
                                highlightbackground='#FFFFFF', highlightthickness=0.5)

        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
        frameAvisos.background = img
        bg = frameAvisos.create_image(0, 0, anchor=tk.NW, image=img)

        #FRAME DENTRO DO CANVAS
        frame = Frame(interface_ativos.inicio, bg='#06c767')
        frame_window = frameAvisos.create_window(100, 120, window=frame)

        #PRIMEIRO E SEGUNDO LABEL
        informeAtivo = Image.open('imagens\\button_selecione-o-ativo.png')
        tkimage = ImageTk.PhotoImage(informeAtivo)
        avisoAtivo1 = tk.Label(frame,
                            image=tkimage, bg='#06c767')
        avisoAtivo1.tkimage = tkimage

        informeAtivo2 = Image.open('imagens\\button_selecione-o-ativo2.png')
        tkimage2 = ImageTk.PhotoImage(informeAtivo2)
        avisoAtivo2 = tk.Label(frame,
                               image=tkimage2, bg='#06c767')
        avisoAtivo2.tkimage2 = tkimage2

        #BOTÃO DE IGUAL(=)
        imagemIgualdade = Image.open('imagens\\sinal_de_igual.png')
        tkigualdade = ImageTk.PhotoImage(imagemIgualdade)
        igualdade = tk.Button(frame,
                               image=tkigualdade, bg='#06c767',
                              bd=0,
                              command=lambda: [funcoes.resultadoCorrelacao(self=None),
                                               frameAvisos.place_forget()])
        igualdade.tkigualdade = tkigualdade

        frameAvisos.place(x=8, y=400)
        avisoAtivo1.pack(pady=5)
        ativo1 = ttk.Combobox(frame, values=ativos_correlacao.listaAtivos)
        ativo2 = ttk.Combobox(frame, values=ativos_correlacao.listaAtivos)
        ativo1.pack(pady=5, padx=10)
        avisoAtivo2.pack()
        ativo2.pack(pady=5, padx=10)
        igualdade.pack()
        botao_correlacao.fecharCorrelacao.lift()
        botao_correlacao.fecharCorrelacao.place(x=160,y=600)

    def sairCorrelacao(self):

        frameAvisos.place_forget(),
        botao_correlacao.fecharCorrelacao.place_forget()

    def grafico(self):

        global ativo1Grafico
        global ativo2Grafico
        global frameAvisos

        # CANVAS
        IMAGE_PATH = 'imagens\\fundo_avisos.png'
        WIDTH, HEIGTH = 200, 230

        frameAvisos = tk.Canvas(interface_ativos.inicio, width=200, height=230,
                                bg='#FFFFFF',
                                highlightbackground='#FFFFFF', highlightthickness=0.5)

        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
        frameAvisos.background = img
        bg = frameAvisos.create_image(0, 0, anchor=tk.NW, image=img)

        # FRAME DENTRO DO CANVAS
        frame = Frame(interface_ativos.inicio, bg='#06c767')
        frame_window = frameAvisos.create_window(100, 120, window=frame)

        # PRIMEIRO E SEGUNDO LABEL
        informeAtivo = Image.open('imagens\\button_selecione-o-ativo.png')
        tkimage = ImageTk.PhotoImage(informeAtivo)
        avisoAtivo1 = tk.Label(frame,
                               image=tkimage, bg='#06c767')
        avisoAtivo1.tkimage = tkimage

        informeAtivo2 = Image.open('imagens\\button_selecione-o-ativo2.png')
        tkimage2 = ImageTk.PhotoImage(informeAtivo2)
        avisoAtivo2 = tk.Label(frame,
                               image=tkimage2, bg='#06c767')
        avisoAtivo2.tkimage2 = tkimage2

        # BOTÃO DE IGUAL(=)
        imagemIgualdade = Image.open('imagens\\sinal_de_igual.png')
        tkigualdade = ImageTk.PhotoImage(imagemIgualdade)
        igualdade = tk.Button(frame,
                              image=tkigualdade, bg='#06c767',
                              bd=0,
                              command=lambda: funcoes.imprimiGrafico(self=None))
        igualdade.tkigualdade = tkigualdade

        frameAvisos.place(x=8, y=400)
        avisoAtivo1.pack(pady=5)
        ativo1Grafico = ttk.Combobox(frame, values=ativos_correlacao.listaAtivos)
        ativo2Grafico = ttk.Combobox(frame, values=ativos_correlacao.listaAtivos)
        ativo1Grafico.pack(pady=5, padx=10)
        avisoAtivo2.pack()
        ativo2Grafico.pack(pady=5, padx=10)
        igualdade.pack()
        botao_graficos.fecharGrafico.lift()
        botao_graficos.fecharGrafico.place(x=150, y=600)

    def imprimiGrafico(self):

        escolha1_graficos = 'ativos\\' + ativo1Grafico.get()
        escolha2_graficos = 'ativos\\' + ativo2Grafico.get()

        book_graficos = pd.read_excel(escolha1_graficos)
        book2_graficos = pd.read_excel(escolha2_graficos)
        ativo1 = np.asarray(book_graficos)
        ativo2 = np.asarray(book2_graficos)
        valor = []
        data = []
        valor2 = []
        cont1_graficos = 1

        while cont1_graficos != 440:

            barra_universal_ativos.barraProgresso.place(x=55, y=700)
            barra_universal_ativos.barraProgresso.update()

            valor.append(ativo1[cont1_graficos, 1])
            data.append((ativo1[cont1_graficos, 0]))

            valor2.append(ativo2[cont1_graficos, 1])

            cont1_graficos += 1
            barra_universal_ativos.barraProgresso['value'] = (cont1_graficos * 100 / 490)

        nomenclatura2 = escolha2_graficos.replace('.xlsx', '')
        nomenclatura2 = nomenclatura2.replace('ativos', '')
        nomenclatura2 = list(nomenclatura2)
        del nomenclatura2[0]
        nomenclatura2 = ','.join(nomenclatura2)
        nomenclatura2 = nomenclatura2.replace(',', '')

        nomenclatura1 = escolha1_graficos.replace('.xlsx', '')
        nomenclatura1 = nomenclatura1.replace('ativos','')
        nomenclatura1 = list(nomenclatura1)
        del nomenclatura1[0]
        nomenclatura1 = ','.join(nomenclatura1)
        nomenclatura1 = nomenclatura1.replace(',', '')
        fig = plt.figure()
        plt.rcParams['figure.figsize'] = 20,20
        plt.rcParams['xtick.labelsize'] = 8
        plt.plot(data, valor, c='#363636', label=nomenclatura1)
        plt.plot(data, valor2, c='#3CB371', label=nomenclatura2)

        plt.legend()
        plt.title('Cotação ativos: ' + nomenclatura1 + ' ' + nomenclatura2, font='Finance',
                      color='#363636')
        fig.savefig('teste.png', edgecolor='none')

        #plt.show(grafico())

        barra_universal_ativos.barraProgresso.place_forget()
        frameAvisos.place_forget()

    def sairGrafico(self):

        frameAvisos.place_forget()
        botao_graficos.fecharGrafico.place_forget()

    def atualizar(self):

        cont = 0

        while cont < len(ativos_correlacao.listaAtivos):
            barra_universal_ativos.barraProgresso.place(x=55, y=700)
            barra_universal_ativos.barraProgresso.update()

            mudanca = ativos_correlacao.listaAtivos[cont].replace('.xlsx', '')
            dado = yf.download(tickers=mudanca + '.SA', period='2y')['Adj Close']
            dado.to_excel('ativos\\' + mudanca + '.xlsx')
            cont += 1

            barra_universal_ativos.barraProgresso['value'] = (cont * 100 / len(ativos_correlacao.listaAtivos))

        barra_universal_ativos.barraProgresso.place_forget()

        ativo1['value'] = ativos_correlacao.listaAtivos
        ativo2['value'] = ativos_correlacao.listaAtivos
        ativo1Grafico['value'] = ativos_correlacao.listaAtivos
        ativo2Grafico['value'] = ativos_correlacao.listaAtivos

    def resultadoCorrelacao(self):

        escolha1 = ativo1.get()
        escolha2 = ativo2.get()

        book = pd.read_excel('ativos\\' + escolha1)
        lista1 = []
        cont1 = 1

        valorAtivo1 = np.asarray(book)

        while cont1 != 440:

            lista1.append(valorAtivo1[cont1, 1])
            cont1 += 1

        book = pd.read_excel('ativos\\' + escolha2)
        lista2 = []
        cont2 = 1
        iten = 'começar'

        valorAtivo2 = np.asarray(book)

        while cont2 != 440:

            lista2.append(valorAtivo2[cont2, 1])
            cont2 += 1

        r = np.corrcoef(lista1, lista2)

        resultado = r[0, 1]

        informacoes_correlacao.significadoCorrelacao['text'] = '%.2f' % resultado

        if resultado <= 1 and resultado >= 0.5:

            informacoes_correlacao.resultadoCorrelacao['text'] = 'CORRELAÇÃO MUITO ALTA POSITIVA'

        elif resultado < 0.5 and resultado >= 0.2:

            informacoes_correlacao.resultadoCorrelacao['text'] = 'CORRELAÇÃO MÉDIA POSITIVA'

        elif resultado < 0.2 and resultado > -0.2:

            informacoes_correlacao.resultadoCorrelacao['text'] = 'SEM CORRELAÇÃO'

        elif resultado < -0.5 and resultado >= -0.2:

            informacoes_correlacao.resultadoCorrelacao['text'] = 'CORRELAÇÃO MÉDIA NEGATIVA'

        if resultado <= -1 and resultado >= -0.5:
            informacoes_correlacao.resultadoCorrelacao['text'] = 'CORRELAÇÃO MUITO ALTA NEGATIVA'

        botao_correlacao.limparCorrelacao.place(x=480, y=600)

    def limparCorrelacao(self):

        botao_correlacao.limparCorrelacao.place_forget()

    def compra(self):

        # CANVAS
        IMAGE_PATH = 'imagens\\fundo_avisos.png'
        WIDTH, HEIGTH = 200, 280

        frameAvisos = tk.Canvas(interface_ativos.inicio, width=200, height=280,
                                bg='#FFFFFF',
                                highlightbackground='#FFFFFF', highlightthickness=0.5)

        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
        frameAvisos.background = img
        bg = frameAvisos.create_image(0, 0, anchor=tk.NW, image=img)

        # FRAME DENTRO DO CANVAS
        frame = Frame(interface_ativos.inicio, bg='#06c767')
        frame_window = frameAvisos.create_window(100, 120, window=frame)

        # TODOS LABELS
        informeCodigo = Image.open('imagens\\label_codigo.png')
        tkimage = ImageTk.PhotoImage(informeCodigo)
        avisoAtivo1 = tk.Label(interface_ativos.inicio,
                               image=tkimage, bg='#06c767')
        avisoAtivo1.tkimage = tkimage

        informeData = Image.open('imagens\\button_data.png')
        tkimage2 = ImageTk.PhotoImage(informeData)
        avisoAtivo2 = tk.Label(interface_ativos.inicio,
                               image=tkimage2, bg='#06c767')
        avisoAtivo2.tkimage2 = tkimage2

        informeValor = Image.open('imagens\\button_valor.png')
        tkimage = ImageTk.PhotoImage(informeValor)
        avisoAtivo3 = tk.Label(interface_ativos.inicio,
                               image=tkimage, bg='#06c767')
        avisoAtivo3.tkimage = tkimage

        informeQuantidade = Image.open('imagens\\button_quantidade.png')
        tkimage2 = ImageTk.PhotoImage(informeQuantidade)
        avisoAtivo4 = tk.Label(interface_ativos.inicio,
                               image=tkimage2, bg='#06c767')
        avisoAtivo4.tkimage2 = tkimage2

        # BOTÃO DE IGUAL(=)
        imagemIgualdade = Image.open('imagens\\soma.png')
        tkigualdade = ImageTk.PhotoImage(imagemIgualdade)
        igualdade = tk.Button(interface_ativos.inicio,
                              image=tkigualdade, bg='#06c767',
                              bd=0,
                              command=lambda: [funcoes.addCompraAtivo(self=None),
                                               funcoes.atualizaItensComprados(self=None),
                                               grafico_dos_ativos_tela.canvas.place_forget(),
                                               frames_universal_ativos.frameAtivosEmHistorico.place_forget(),
                                               funcoes.atualizarDezAtivos(self=None)])
        igualdade.tkigualdade = tkigualdade

        botao_compra_de_ativo.fechar['command']= lambda: [frameAvisos.place_forget(), avisoAtivo1.place_forget(),
                                     codigo.place_forget(), avisoAtivo2.place_forget(),
                                     data.place_forget(), avisoAtivo3.place_forget(),
                                     preco.place_forget(), avisoAtivo4.place_forget(),
                                     quantidade.place_forget(), igualdade.place_forget(),
                                     botao_compra_de_ativo.fechar.place_forget()]
        global codigo
        global preco
        global data
        global quantidade

        codigo = ttk.Entry(interface_ativos.inicio)
        preco = ttk.Entry(interface_ativos.inicio, width=11)
        data = ttk.Entry(interface_ativos.inicio, width=11)
        quantidade = ttk.Entry(interface_ativos.inicio, width=8)

        frameAvisos.place(x=8, y=350)
        avisoAtivo1.place(x=30, y=360)
        codigo.place(x=42, y=403)
        avisoAtivo2.place(x=22, y=432)
        data.place(x=22, y=475)
        avisoAtivo3.place(x=117, y=432)
        preco.place(x=117, y=475)
        avisoAtivo4.place(x=47, y=505)
        quantidade.place(x=79, y=545)
        igualdade.place(x=83, y=570)
        botao_compra_de_ativo.fechar.lift()
        botao_compra_de_ativo.fechar.place(x=157, y=600)

    def addCompraAtivo(self):

        leitura = pd.read_excel('Dados\\dadosFinanceiros.xlsx', 'acoes')

        if ',' in preco.get():
            precoDoAtivo = str(preco.get())
            semVirgula = precoDoAtivo.replace(',','.')
        else:
            semVirgula = preco.get()
        array = np.asarray(leitura)
        array = np.delete(array, (0), axis=1)
        matriz = pd.DataFrame(array)
        dadosNovos = pd.DataFrame([[str(codigo.get()).upper(), str(semVirgula).upper(),
                                    str(quantidade.get()).upper(), data.get()]])
        matriz = pd.concat([matriz, dadosNovos], axis=0)

        matriz.to_excel('Dados\\dadosFinanceiros.xlsx', 'acoes')

    def atualizaItensComprados(self):

        global dicionarioOrdemCrescente
        global dicionarioOrdemCrescenteDosValores
        global dicionarioValorAcoes

        leitura = pd.read_excel('Dados\\dadosFinanceiros.xlsx', 'acoes')
        array = np.asarray(leitura)
        array = np.delete(array, (0), axis=1)
        matriz = pd.DataFrame(array)
        analise = []
        cont = 0
        while cont < len(array):
            analise.append(array[cont, 0])
            cont += 1

        listaSemRepeticao = []
        for i in analise:
            if i not in listaSemRepeticao:
                listaSemRepeticao.append(i)
        cont = 0
        quantidadeDeNomes = len(listaSemRepeticao)
        dicionario = {}

        while cont < len(listaSemRepeticao):
            soma = 0
            cont1 = 0
            if bool(dicionario) == False:
                dicionario = {listaSemRepeticao[cont]: 0}
            else:
                dicionario[listaSemRepeticao[cont]] = 0
            while cont1 < len(array):
                if listaSemRepeticao[cont] == array[cont1, 0]:
                    soma += int(array[cont1, 2])
                    dicionario[listaSemRepeticao[cont]] = soma
                cont1 += 1
            cont += 1
        dicionarioOrdemCrescente = {k: v for k, v in
                                    sorted(dicionario.items(), key=lambda item: item[1], reverse=True)}
        cont2 = 0
        dicionarioValorAcoes = {}

        while cont2 < len(listaSemRepeticao):
            soma = 0
            cont3 = 0
            if bool(dicionarioValorAcoes) == False:
                dicionarioValorAcoes = {listaSemRepeticao[cont2]: 0}
            else:
                dicionarioValorAcoes[listaSemRepeticao[cont2]] = 0
            while cont3 < len(array):
                if listaSemRepeticao[cont2] == array[cont3, 0]:
                    somaParcial = float(array[cont3, 1])*float(array[cont3, 2])
                    soma += somaParcial
                    dicionarioValorAcoes[listaSemRepeticao[cont2]] = soma
                cont3 += 1
            cont2 += 1
        dicionarioOrdemCrescenteDosValores = {k: v for k, v in
                                              sorted(dicionarioValorAcoes.items(), key=lambda item: item[1],
                                                     reverse=True)}

        #ATUALIZAÇÃO DO LABEL DO CORPO
        informativos_corpo.totalNegocios['text']=str(len(dicionarioOrdemCrescente.keys())-1) + ' Negocio'
        informativos_corpo.totalAtivos['text']=str(sum(dicionarioOrdemCrescente.values())) + ' Ativo'
        valores_patrimonio.valorAcoes['text']='R$ '+ str(sum(dicionarioValorAcoes.values()))

    def buscarInformacao(self):

        global frameAvisos
        global avisoAtivo1
        global codigo
        global igualdade

        # CANVAS

        IMAGE_PATH = 'imagens\\fundo_avisos.png'
        WIDTH, HEIGTH = 200, 170

        frameAvisos = tk.Canvas(interface_ativos.inicio, width=200, height=170,
                                bg='#FFFFFF',
                                highlightbackground='#FFFFFF', highlightthickness=0.5)

        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
        frameAvisos.background = img
        bg = frameAvisos.create_image(0, 0, anchor=tk.NW, image=img)

        # FRAME DENTRO DO CANVAS

        frame = Frame(interface_ativos.inicio, bg='#06c767')
        frame_window = frameAvisos.create_window(100, 120, window=frame)

        # TODOS LABELS

        informeCodigo = Image.open('imagens\\label_codigo.png')
        tkimage = ImageTk.PhotoImage(informeCodigo)
        avisoAtivo1 = tk.Label(interface_ativos.inicio,
                               image=tkimage, bg='#06c767')
        avisoAtivo1.tkimage = tkimage

        # BOTÃO DE IGUAL(=)

        imagemIgualdade = Image.open('imagens\\soma.png')
        tkigualdade = ImageTk.PhotoImage(imagemIgualdade)
        igualdade = tk.Button(interface_ativos.inicio,
                              image=tkigualdade, bg='#06c767',
                              bd=0,
                              command=lambda: [funcoes.adicionaInformacaoDeAtivo(self=None),
                                               frameAvisos.place_forget(),
                                               avisoAtivo1.place_forget(),
                                               codigo.place_forget(),
                                               igualdade.place_forget()
                                               ])
        igualdade.tkigualdade = tkigualdade

        global codigo

        codigo = ttk.Entry(interface_ativos.inicio)

        #frameAvisos.place(x=500, y=280)
        frameAvisos.place(x=8, y=460)
        avisoAtivo1.place(x=30, y=480)
        codigo.place(x=42, y=530)
        igualdade.place(x=84, y=560)
        botao_cadastro.fecharCadastro.lift()
        botao_cadastro.fecharCadastro.place(x=150, y=600)

    def sairAdicionarAtivo(self):

        frameAvisos.place_forget()
        botao_cadastro.fecharCadastro.place_forget()
        avisoAtivo1.place_forget()
        codigo.place_forget()
        igualdade.place_forget()

    def adicionaInformacaoDeAtivo(self):

        x = codigo.get().upper()

        if x != '':

            dados1 = yf.download(tickers=x+'.SA', period='2y')['Adj Close']
            nome1 = x
            dados1.to_excel('ativos\\'+ nome1 + '.xlsx')

            ativos_correlacao.listaAtivos.append(x + '.xlsx')

    def atualizarDezAtivos(self):

        if len(dicionarioOrdemCrescenteDosValores) > 0 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][0]) != 'nan':
            nomeDoAtivo = [key for key in dicionarioOrdemCrescenteDosValores.keys()][0]
            ativoAdquirido = Label(interface_ativos.inicio,
                                   font=('Finance', 18),
                                   text=[[key for key in dicionarioOrdemCrescenteDosValores.keys()][0]],
                                   bg='#FFFFFF',
                                   foreground='#696969',
                                   bd=0)
            quantidadeAtivo = Label(interface_ativos.inicio,
                                    font=('Finance', 18),
                                    text='{:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(dicionarioValorAcoes.values()))+' %',
                                    bg='#FFFFFF',
                                    foreground='#696969',
                                    bd=0)
            valorAtivo = Label(interface_ativos.inicio,
                               font=('Finance', 18),
                               text='R${:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]),
                               bg='#FFFFFF',
                               foreground='#696969',
                               bd=0)
            valorAtivo.place(x=870, y=100)
            quantidadeAtivo.place(x=770, y=100)
            ativoAdquirido.place(x=650, y=100)

            legenda = Canvas(interface_ativos.inicio, width=20, height=15, bg='darkgreen')
            legenda.place(x=615, y=105)

        if len(dicionarioOrdemCrescenteDosValores) > 1 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][1]) != 'nan':
            nomeDoAtivo = [key for key in dicionarioOrdemCrescenteDosValores.keys()][1]
            ativoAdquiridoSegundo = Label(interface_ativos.inicio,
                                          font=('Finance', 18),
                                          text=[[key for key in dicionarioOrdemCrescenteDosValores.keys()][1]],
                                          bg='#FFFFFF',
                                          foreground='#696969',
                                          bd=0)
            quantidadeAtivoSegundo = Label(interface_ativos.inicio,
                                           font=('Finance', 18),
                                           text='{:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(dicionarioValorAcoes.values()))+' %',
                                           bg='#FFFFFF',
                                           foreground='#696969',
                                           bd=0)
            valorAtivoSegundo = Label(interface_ativos.inicio,
                               font=('Finance', 18),
                               text='R${:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]),
                               bg='#FFFFFF',
                               foreground='#696969',
                               bd=0)
            valorAtivoSegundo.place(x=870, y=145)
            quantidadeAtivoSegundo.place(x=770, y=145)
            ativoAdquiridoSegundo.place(x=650, y=145)

            legendaSegunda = Canvas(interface_ativos.inicio, width=20, height=15, bg='limegreen')
            legendaSegunda.place(x=615, y=150)

        if len(dicionarioOrdemCrescenteDosValores) > 2 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][2]) != 'nan':
            nomeDoAtivo = [key for key in dicionarioOrdemCrescenteDosValores.keys()][2]
            ativoAdquiridoTerceiro = Label(interface_ativos.inicio,
                                           font=('Finance', 18),
                                           text=[[key for key in dicionarioOrdemCrescenteDosValores.keys()][2]],
                                           bg='#FFFFFF',
                                           foreground='#696969',
                                           bd=0)
            quantidadeAtivoTerceiro = Label(interface_ativos.inicio,
                                            font=('Finance', 18),
                                            text='{:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(dicionarioValorAcoes.values()))+' %',
                                            bg='#FFFFFF',
                                            foreground='#696969',
                                            bd=0)
            valorAtivoTerceiro = Label(interface_ativos.inicio,
                               font=('Finance', 18),
                               text='R${:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]),
                               bg='#FFFFFF',
                               foreground='#696969',
                               bd=0)
            valorAtivoTerceiro.place(x=870, y=190)
            quantidadeAtivoTerceiro.place(x=770, y=190)
            ativoAdquiridoTerceiro.place(x=650, y=190)

            legendaTerceira = Canvas(interface_ativos.inicio, width=20, height=15, bg='aquamarine')
            legendaTerceira.place(x=615, y=195)

        if len(dicionarioOrdemCrescenteDosValores) > 3 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][3]) != 'nan':
            nomeDoAtivo = [key for key in dicionarioOrdemCrescenteDosValores.keys()][3]
            ativoAdquiridoQuarto = Label(interface_ativos.inicio,
                                         font=('Finance', 18),
                                         text=[[key for key in dicionarioOrdemCrescenteDosValores.keys()][3]],
                                         bg='#FFFFFF',
                                         foreground='#696969',
                                         bd=0)
            quantidadeAtivoQuarto = Label(interface_ativos.inicio,
                                          font=('Finance', 18),
                                          text='{:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(dicionarioValorAcoes.values()))+' %',
                                          bg='#FFFFFF',
                                          foreground='#696969',
                                          bd=0)
            valorAtivoQuarto = Label(interface_ativos.inicio,
                               font=('Finance', 18),
                               text='R${:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]),
                               bg='#FFFFFF',
                               foreground='#696969',
                               bd=0)
            valorAtivoQuarto.place(x=870, y=235)
            quantidadeAtivoQuarto.place(x=770, y=235)
            ativoAdquiridoQuarto.place(x=650, y=235)

            legendaQuarto = Canvas(interface_ativos.inicio, width=20, height=15, bg='goldenrod')
            legendaQuarto.place(x=615, y=240)

        if len(dicionarioOrdemCrescenteDosValores) > 4 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][4]) != 'nan':
            nomeDoAtivo = [key for key in dicionarioOrdemCrescenteDosValores.keys()][4]
            ativoAdquiridoQuinto = Label(interface_ativos.inicio,
                                         font=('Finance', 18),
                                         text=[[key for key in dicionarioOrdemCrescenteDosValores.keys()][4]],
                                         bg='#FFFFFF',
                                         foreground='#696969',
                                         bd=0)
            quantidadeAtivoQuinto = Label(interface_ativos.inicio,
                                          font=('Finance', 18),
                                          text='{:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(dicionarioValorAcoes.values()))+' %',
                                          bg='#FFFFFF',
                                          foreground='#696969',
                                          bd=0)
            valorAtivoQuinto = Label(interface_ativos.inicio,
                               font=('Finance', 18),
                               text='R${:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]),
                               bg='#FFFFFF',
                               foreground='#696969',
                               bd=0)
            valorAtivoQuinto.place(x=870, y=280)
            quantidadeAtivoQuinto.place(x=770, y=280)
            ativoAdquiridoQuinto.place(x=650, y=280)

            legendaQuinto = Canvas(interface_ativos.inicio, width=20, height=15, bg='darkviolet')
            legendaQuinto.place(x=615, y=285)

        if len(dicionarioOrdemCrescenteDosValores) > 5 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][5]) != 'nan':
            nomeDoAtivo = [key for key in dicionarioOrdemCrescenteDosValores.keys()][5]
            ativoAdquiridoSexto = Label(interface_ativos.inicio,
                                        font=('Finance', 18),
                                        text=[[key for key in dicionarioOrdemCrescenteDosValores.keys()][5]],
                                        bg='#FFFFFF',
                                        foreground='#696969',
                                        bd=0)
            quantidadeAtivoSexto = Label(interface_ativos.inicio,
                                         font=('Finance', 18),
                                         text='{:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(dicionarioValorAcoes.values()))+' %',
                                         bg='#FFFFFF',
                                         foreground='#696969',
                                         bd=0)
            valorAtivoSexto = Label(interface_ativos.inicio,
                               font=('Finance', 18),
                               text='R${:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]),
                               bg='#FFFFFF',
                               foreground='#696969',
                               bd=0)
            valorAtivoSexto.place(x=870, y=325)
            quantidadeAtivoSexto.place(x=770, y=325)
            ativoAdquiridoSexto.place(x=650, y=325)

            legendaSexto = Canvas(interface_ativos.inicio, width=20, height=15, bg='mediumvioletred')
            legendaSexto.place(x=615, y=330)

        if len(dicionarioOrdemCrescenteDosValores) > 6 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][6]) != 'nan':
            nomeDoAtivo = [key for key in dicionarioOrdemCrescenteDosValores.keys()][6]
            ativoAdquiridoSetimo = Label(interface_ativos.inicio,
                                         font=('Finance', 18),
                                         text=[[key for key in dicionarioOrdemCrescenteDosValores.keys()][6]],
                                         bg='#FFFFFF',
                                         foreground='#696969',
                                         bd=0)
            quantidadeAtivoSetimo = Label(interface_ativos.inicio,
                                          font=('Finance', 18),
                                          text='{:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(dicionarioValorAcoes.values()))+' %',
                                          bg='#FFFFFF',
                                          foreground='#696969',
                                          bd=0)
            valorAtivoSetimo = Label(interface_ativos.inicio,
                               font=('Finance', 18),
                               text='R${:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]),
                               bg='#FFFFFF',
                               foreground='#696969',
                               bd=0)
            valorAtivoSetimo.place(x=870, y=370)
            quantidadeAtivoSetimo.place(x=770, y=370)
            ativoAdquiridoSetimo.place(x=650, y=370)

            legendaSetimo = Canvas(interface_ativos.inicio, width=20, height=15, bg='orange')
            legendaSetimo.place(x=615, y=375)

        if len(dicionarioOrdemCrescenteDosValores) > 7 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][7]) != 'nan':
            nomeDoAtivo = [key for key in dicionarioOrdemCrescenteDosValores.keys()][7]
            ativoAdquiridoOitavo = Label(interface_ativos.inicio,
                                         font=('Finance', 18),
                                         text=[[key for key in dicionarioOrdemCrescenteDosValores.keys()][7]],
                                         bg='#FFFFFF',
                                         foreground='#696969',
                                         bd=0)
            quantidadeAtivoOitavo = Label(interface_ativos.inicio,
                                          font=('Finance', 18),
                                          text='{:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(dicionarioValorAcoes.values()))+' %',
                                          bg='#FFFFFF',
                                          foreground='#696969',
                                          bd=0)
            valorAtivoOitavo = Label(interface_ativos.inicio,
                               font=('Finance', 18),
                               text='R${:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]),
                               bg='#FFFFFF',
                               foreground='#696969',
                               bd=0)
            valorAtivoOitavo.place(x=870, y=415)
            quantidadeAtivoOitavo.place(x=770, y=415)
            ativoAdquiridoOitavo.place(x=650, y=415)

            legendaOitavo = Canvas(interface_ativos.inicio, width=20, height=15, bg='khaki')
            legendaOitavo.place(x=615, y=420)

        if len(dicionarioOrdemCrescenteDosValores) > 8 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][8]) != 'nan':
            nomeDoAtivo = [key for key in dicionarioOrdemCrescenteDosValores.keys()][8]
            ativoAdquiridoNono = Label(interface_ativos.inicio,
                                       font=('Finance', 18),
                                       text=[[key for key in dicionarioOrdemCrescenteDosValores.keys()][8]],
                                       bg='#FFFFFF',
                                       foreground='#696969',
                                       bd=0)
            quantidadeAtivoNono = Label(interface_ativos.inicio,
                                        font=('Finance', 18),
                                        text='{:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(dicionarioValorAcoes.values()))+' %',
                                        bg='#FFFFFF',
                                        foreground='#696969',
                                        bd=0)
            valorAtivoNono = Label(interface_ativos.inicio,
                               font=('Finance', 18),
                               text='R${:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]),
                               bg='#FFFFFF',
                               foreground='#696969',
                               bd=0)
            valorAtivoNono.place(x=870, y=460)
            quantidadeAtivoNono.place(x=770, y=460)
            ativoAdquiridoNono.place(x=650, y=460)

            legendaNono = Canvas(interface_ativos.inicio, width=20, height=15, bg='peru')
            legendaNono.place(x=615, y=465)

        if len(dicionarioOrdemCrescenteDosValores) > 9 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][9]) != 'nan':
            nomeDoAtivo = [key for key in dicionarioOrdemCrescenteDosValores.keys()][9]
            ativoAdquiridoDecimo = Label(interface_ativos.inicio,
                                         font=('Finance', 18),
                                         text=[[key for key in dicionarioOrdemCrescenteDosValores.keys()][9]],
                                         bg='#FFFFFF',
                                         foreground='#696969',
                                         bd=0)
            quantidadeAtivoDecimo = Label(interface_ativos.inicio,
                                          font=('Finance', 18),
                                          text='{:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]*100
                                    /sum(dicionarioValorAcoes.values()))+' %',
                                          bg='#FFFFFF',
                                          foreground='#696969',
                                          bd=0)
            valorAtivoDecimo = Label(interface_ativos.inicio,
                               font=('Finance', 18),
                               text='R${:.2f}'.format(dicionarioValorAcoes[nomeDoAtivo]),
                               bg='#FFFFFF',
                               foreground='#696969',
                               bd=0)
            valorAtivoDecimo.place(x=870, y=505)
            quantidadeAtivoDecimo.place(x=770, y=505)
            ativoAdquiridoDecimo.place(x=650, y=505)

            legendaDecimo = Canvas(interface_ativos.inicio, width=20, height=15, bg='saddlebrown')
            legendaDecimo.place(x=615, y=510)

        if len(dicionarioOrdemCrescenteDosValores) > 11:
            cont = 10
            valorDosOutrosAtivos = 0
            while cont < len(dicionarioOrdemCrescenteDosValores):
                nomeDoAtivo = [key for key in dicionarioOrdemCrescenteDosValores.keys()][cont]
                valorDosOutrosAtivos += dicionarioOrdemCrescenteDosValores[nomeDoAtivo]
                cont += 1
            ativoAdquiridoOutros = Label(interface_ativos.inicio,
                                         font=('Finance', 18),
                                         text='Outros',
                                         bg='#FFFFFF',
                                         foreground='#696969',
                                         bd=0)
            quantidadeAtivoOutros = Label(interface_ativos.inicio,
                                          font=('Finance', 18),
                                          text='{:.2f}'.format(valorDosOutrosAtivos * 100
                                                               / sum(
                                              dicionarioValorAcoes.values())) + ' %',
                                          bg='#FFFFFF',
                                          foreground='#696969',
                                          bd=0)
            valorAtivoOutros = Label(interface_ativos.inicio,
                                     font=('Finance', 18),
                                     text='R${:.2f}'.format(valorDosOutrosAtivos),
                                     bg='#FFFFFF',
                                     foreground='#696969',
                                     bd=0)
            valorAtivoOutros.place(x=870, y=550)
            quantidadeAtivoOutros.place(x=770, y=550)
            ativoAdquiridoOutros.place(x=650, y=550)

            legendaOutros = Canvas(interface_ativos.inicio, width=20, height=15, bg='gray')
            legendaOutros.place(x=615, y=555)

        #DADOS DO GRAFICO PRINCIPAL ATUALIZADO APÓS ADICIONAR UMA COMPRA OU VENDA DE ATIVO

        if len(dicionarioOrdemCrescenteDosValores) > 0 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][0]) != 'nan':
            dadosQuantidade = [dicionarioOrdemCrescenteDosValores
                               [[key for key in dicionarioOrdemCrescenteDosValores.keys()][0]]]

        if len(dicionarioOrdemCrescenteDosValores) > 1 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][1]) != 'nan':
            dadosQuantidade.append(dicionarioOrdemCrescenteDosValores[
                                       [key for key in dicionarioOrdemCrescenteDosValores.keys()][1]])

        if len(dicionarioOrdemCrescenteDosValores) > 2 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][2]) != 'nan':
            dadosQuantidade.append(dicionarioOrdemCrescenteDosValores[
                                       [key for key in dicionarioOrdemCrescenteDosValores.keys()][2]])

        if len(dicionarioOrdemCrescenteDosValores) > 3 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][3]) != 'nan':
            dadosQuantidade.append(dicionarioOrdemCrescenteDosValores[
                                       [key for key in dicionarioOrdemCrescenteDosValores.keys()][3]])

        if len(dicionarioOrdemCrescenteDosValores) > 4 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][4]) != 'nan':
            dadosQuantidade.append(dicionarioOrdemCrescenteDosValores[
                                       [key for key in dicionarioOrdemCrescenteDosValores.keys()][4]])

        if len(dicionarioOrdemCrescenteDosValores) > 5 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][5]) != 'nan':
            dadosQuantidade.append(dicionarioOrdemCrescenteDosValores[
                                       [key for key in dicionarioOrdemCrescenteDosValores.keys()][5]])

        if len(dicionarioOrdemCrescenteDosValores) > 6 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][6]) != 'nan':
            dadosQuantidade.append(dicionarioOrdemCrescenteDosValores[
                                       [key for key in dicionarioOrdemCrescenteDosValores.keys()][6]])

        if len(dicionarioOrdemCrescenteDosValores) > 7 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][7]) != 'nan':
            dadosQuantidade.append(dicionarioOrdemCrescenteDosValores[
                                       [key for key in dicionarioOrdemCrescenteDosValores.keys()][7]])

        if len(dicionarioOrdemCrescenteDosValores) > 8 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][8]) != 'nan':
            dadosQuantidade.append(dicionarioOrdemCrescenteDosValores[
                                       [key for key in dicionarioOrdemCrescenteDosValores.keys()][8]])

        if len(dicionarioOrdemCrescenteDosValores) > 9 \
                and str([key for key in dicionarioOrdemCrescenteDosValores.keys()][9]) != 'nan':
            dadosQuantidade.append(dicionarioOrdemCrescenteDosValores[
                                       [key for key in dicionarioOrdemCrescenteDosValores.keys()][9]])
        if len(dicionarioOrdemCrescenteDosValores) > 11:
            cont = 10
            valorDosOutrosAtivos = 0
            while cont < len(dicionarioOrdemCrescenteDosValores):
                nomeDoAtivo = [key for key in dicionarioOrdemCrescenteDosValores.keys()][cont]
                valorDosOutrosAtivos += dicionarioOrdemCrescenteDosValores[nomeDoAtivo]
                cont += 1
            dadosQuantidade.append(valorDosOutrosAtivos)

        font = {'family': 'finance',
                'weight': 'bold',
                'size': 13}
        plt.rc('font', **font)
        cores = ('darkgreen', 'limegreen', 'aquamarine', 'goldenrod', 'darkviolet',
                 'mediumvioletred', 'orange', 'khaki', 'peru', 'saddlebrown', 'gray')

        plt.figure(figsize=(0.2, 0.2))
        fig1, axl = plt.subplots()
        c2 = axl.pie(dadosQuantidade, shadow=False, colors=cores)
        fig1.patch.set_facecolor('none')
        fig1.savefig('temp.png', facecolor=fig1.get_facecolor(), edgecolor='none')

        grafico_dos_ativos_tela.image =PhotoImage(file='temp.png')
        image_id2 = grafico_dos_ativos_tela.canvas.create_image(143, 147, image=grafico_dos_ativos_tela.image)
        grafico_dos_ativos_tela.image2 = PhotoImage(file='imagens\\circulo_branco.png')
        image_id = grafico_dos_ativos_tela.canvas.create_image(150, 150, image=grafico_dos_ativos_tela.image2)
        grafico_dos_ativos_tela.canvas.place(x=250, y=180)

interface_ativos.inicio.mainloop()