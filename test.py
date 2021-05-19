from openpyxl import Workbook, load_workbook
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import datetime
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
from openpyxl import Workbook, load_workbook
import pandas as pd

#xls = pd.ExcelFile('Dados\\dadosFinanceiros.xlsx')

#sheetX = xls.parse(0)

#var1 = sheetX['cod']

#print(var1[0]) #1 is the row number...

import numpy as np

#teste = pd.read_excel('Dados\\dadosFinanceiros.xlsx', 'acoes')

#array1 = np.asarray(teste)
#array1 = np.delete(array1,(0), axis=1)
#matriz=pd.DataFrame(array1)
#dado =pd.DataFrame([['test3', 16, 2, '12-5-2010']])
#dados =pd.DataFrame(dado)
#matriz = pd.concat([matriz,dado], axis=0)

#array.append(['TEST2',15,1,(2020,5,10,0,0)])

#matriz.to_excel('Dados\\dadosFinanceiros.xlsx', 'acoes')

#matriz = array1.drop(columns=[0])
#print(matriz)
#tips.head()
#cont = 1
#numero = str(cont)

#while folha1['A'+numero] != '':

    #cont +=1
    #numero = str(cont)

#print('A'+numero)
#print(type(numero))
#folha1['A'+str(teste)]='aqui oh'
#sheet['B'+numero]=quantidade.get()
#sheet['C'+numero]=preco.get()
#sheet['D'+numero]=data.get()

#dados.save('Dados\\dadosFinanceiros.xlsx')

#workbook = xlrd.open_workbook('Dados\\

#worksheet = workbook.sheet_by_index(0)
#cont = 0

#while worksheet.isnull().sum:
 #   cont += 1

from collections import Counter


leitura = pd.read_excel('ativos\AGRO3.xlsx')
array = np.asarray(leitura)
array = np.delete(array, (0), axis=1)
matriz = pd.DataFrame(array)
print(array)
print(matriz)
analise = []
#print(array)
#print(type(array))
#cont = 0
#while cont < len(array):
  #  analise.append(array[cont,0])
 #   cont +=1

#nomes = []
#for i in analise:
  #  if i not in nomes:
 #       nomes.append(i)

#viu = Counter(analise)
#print('esse')
#print(nomes)
#print(analise)

#cont = 0
#quantidadeDeNomes = len(nomes)
#dicionario = {}
#print(nomes)
#while cont < len(nomes):
    #print(bool(dicionario))
    #soma=0
    #print('começo')
    #cont1 = 0
    #if bool(dicionario) == False:

     #   dicionario = {nomes[cont]:0}
        #print('olha aqui')
        #print(dicionario)

    #else:

     #   dicionario[nomes[cont]] = 0
        #print('olhando de novo')
        #print(dicionario)

    #while cont1 < len(array):

        #if nomes[cont]==array[cont1,0]:
            #print('meio')
            #print(array[cont1,1])
        #    somaParcial = float(array[cont1, 1]) * float(array[cont1, 2])
            #print(somaParcial)
       #     soma += somaParcial
      #      dicionario[nomes[cont]] = soma
            # dicionario[nomes[cont]] = soma
            #dicionario[nomes[cont]] = dicionario.get(nomes[cont], soma)

     #   cont1+=1
    #print(nomes[cont])
    #cont += 1
    #print(cont)
    #print('fim')
#print(sum(dicionario.values()))
#print(dicionario)
#print(array)
#print(array[12,1])
#for i in dicionario:
    #print(i)
####PARA PEGAR VELORES DO DICIONARIO
#chaves = dicionario['agro3']
#print([key for key in dicionario.keys()][1])

#ordenado = {k: v for k, v in
 #           sorted(dicionario.items(), key=lambda item: item[1], reverse=True)}

#print(ordenado)
#print(len(dicionario.keys())-1)
#print(sum(dicionario.values()))

#import glob

#targetPattern = "*.xls"
#glob.glob(targetPattern)
#print(glob.glob(targetPattern))

