from tkinter import *
import tkinter as tk
import yfinance as yf

class interface:
    inicio = tk.Tk()
    inicio.title("CORRELAÇÃO")

    inicio.geometry("500x500+300+100")
    #inicio.resizable(0, 0)
    #inicio.state("zoomed")

class localizacao_q2:

    frame_informativos_q2 = Frame(interface.inicio)
    frame_cima_q2 = Frame(interface.inicio)
    frame_meio_q2 = Frame(interface.inicio)
    frame_baixo_q2 = Frame(interface.inicio)
    frame_botao_q2_q2 = Frame(interface.inicio)

    frame_informativos_q2.grid(row=0, column=1)
    frame_cima_q2.grid(row=1, column=1)
    frame_meio_q2.grid(row=2, column=1)
    frame_baixo_q2.grid(row=3, column=1)
    frame_botao_q2_q2.grid(row=4, column=1)

class informacoes_q2:

    colocarAtivo_q2 = Label(localizacao_q2.frame_informativos_q2,
                   text='COLOQUE AQUI OS ATIVOS QUE DESEJA COMPARAR')

    colocarAtivo_q2.grid(row=0, column=1)

    ativo1_q2 = Label(localizacao_q2.frame_cima_q2,
                   text='Valores ativo x')

    ativo1_q2.grid(row=0, column=0, pady=10, padx=10)

    ativo2_q2 = Label(localizacao_q2.frame_cima_q2,
                   text='Valores ativo y')

    ativo2_q2.grid(row=0, column=2, pady=10, padx=10)

class ativos_q2:
    global entrada1_q2
    global entrada2_q2

    entrada1_q2 = Entry(localizacao_q2.frame_cima_q2)
    entrada2_q2 = Entry(localizacao_q2.frame_cima_q2)

    entrada1_q2.grid(row=1, column=0, padx=30)
    entrada2_q2.grid(row=1, column=2, padx=30)

class botao_q2:

    pegarValores_q2 = Button(localizacao_q2.frame_meio_q2, text="Buscar informações",
                          anchor=CENTER,
                          command=lambda: funcao_q2.buscarInformacao()
                          )

    pegarValores_q2.grid(row=0, pady=10)

    clear_q2 = Button(localizacao_q2.frame_meio_q2, text="Limpar",
                          anchor=CENTER,
                          command=lambda: funcao_q2.limpar_q2()
                          )

    clear_q2.grid(row=1, pady=10)

    back_q2 = Button(localizacao_q2.frame_baixo_q2, text="Voltar",
                   anchor=CENTER,
                   command=lambda: funcao_q2.voltar_q2()
                   )

    back_q2.grid(row=1, pady=10)

class funcao_q2:

    def buscarInformacao():

        x = entrada1_q2.get().upper()
        y = entrada2_q2.get().upper()

        if x != '':

            dados1 = yf.download(tickers=x+'.SA', period='2y')['Adj Close']
            nome1 = x
            dados1.to_excel(nome1 + '.xls')

        if y != '':

            dados2 = yf.download(tickers=y + '.SA', period='2y')['Adj Close']
            nome2 = y
            dados2.to_excel(nome2 + '.xls')

    def limpar_q2():

        entrada1_q2.delete(0, END)
        entrada2_q2.delete(0,END)

    def voltar_q2():

        interface.inicio.destroy()
        import correlacao

interface.inicio.mainloop()