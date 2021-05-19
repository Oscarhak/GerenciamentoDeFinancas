import ax as ax
from openpyxl import Workbook, load_workbook
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt, pyplot
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
dadosQuantidade = (100,50,80,2,15)
data = (1,2,3,4,5,6,7,8,9,10)
valor = (10,20,30,40,50,60,70,80,90,100)
valor2 = (100,90,80,70,60,50,40,30,20,10)


canvas_width = 300
canvas_height = 300
nomenclatura1 = 'primeiro'
nomenclatura2 = 'segundo'
fig =plt.figure()
plt.rcParams['xtick.labelsize'] = 2
#plt.rcParams.update({'font.size':2})
plt.plot(data, valor, c='#363636', label=nomenclatura1)
#plt.plot(data, valor2, c='#3CB371', label=nomenclatura2)

plt.legend()
plt.title('Cotação ativos: ' + nomenclatura1 + ' ' + nomenclatura2, font='Finance',
              color='#363636')
plt.xticks([data[0],data[5]])

#i.get_xticklabels().set_visible(False)

#fig = plt.gcf()
#fig.savefig('teste.png', edgecolor='none')
print('deu')
plt.show()
