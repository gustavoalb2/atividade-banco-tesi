import tkinter as tk
from tkinter import ttk

class HomeBanco():
    def __init__ (self, master):
        self.master = master
        self.master.title('Banco')
        self.master.geometry('800x600')
        self.master.resizable(False, False)

        self.frame = ttk.Frame(self.master)
        self.frame.pack(fill='both', expand=True)

        self.label = ttk.Label(self.frame, text='Bienvenido al Banco')
        self.label.pack()

        self.button = ttk.Button(self.frame, text='Clientes', command=self.clientes)
        self.button.pack()

        self.button = ttk.Button(self.frame, text='Cuentas', command=self.cuentas)
        self.button.pack()

        self.button = ttk.Button
    
    def clientes(self):
        self.label['text'] = 'Clientes'

    def cuentas(self):
        self.label['text'] = 'Cuentas'

janela = tk.Tk()
app = HomeBanco(janela)
janela.mainloop()