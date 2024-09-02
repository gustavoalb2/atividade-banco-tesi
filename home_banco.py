import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from banco import Banco

class HomeBanco():
    def __init__ (self, master):
        self.janela = master
        self.janela.title('Banco')
        self.janela.geometry('500x300')
        self.janela.resizable(False, False)
        
        self.mnu_barra = tk.Menu(self.janela)
        self.mnu_contas = tk.Menu(self.mnu_barra, tearoff=0)
        self.mnu_banco = tk.Menu(self.mnu_barra, tearoff=0)
        self.mnu_clientes = tk.Menu(self.mnu_barra, tearoff=0)
        
        self.mnu_barra.add_cascade(label='Conta', menu=self.mnu_contas) #label
        self.mnu_barra.add_cascade(label='Clientes', menu=self.mnu_clientes) #label
        self.mnu_barra.add_cascade(label='Bancos', menu=self.mnu_banco) #label
        self.mnu_contas.add_command(label='Listar contas', command=self.listar_contas) #comandos
        self.mnu_contas.add_separator()
        self.mnu_contas.add_command(label='Cadastrar conta', command=self.cadastrar_conta)
        
        self.mnu_clientes.add_command(label='Listar clientes', command=self.listar_clientes) #comandos
        self.mnu_clientes.add_separator()
        self.mnu_clientes.add_command(label='Cadastrar clientes')
        
        self.mnu_banco.add_command(label='Listar banco', command=self.listar_banco) #comandos
        self.mnu_banco.add_separator()
        self.mnu_banco.add_command(label='Cadastrar banco', command=self.cadastrar_banco)
        
        self.janela.config(menu=self.mnu_barra)
    
    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
            
    
    def listar_contas(self):
        self.limpar_tela()
        self.janela.title('Listar contas')
        self.janela.geometry('500x300')
        
        self.frame = tk.Frame(self.janela)
        self.frame.pack()
                
        self.tree_contas = ttk.Treeview(self.frame, columns=('Número', 'Titular', 'Saldo'))
        self.tree_contas.heading('#0', text='ID')
        self.tree_contas.heading('#1', text='Número')
        self.tree_contas.heading('#2', text='Titular')
        self.tree_contas.heading('#3', text='Saldo')
        self.tree_contas.grid(row=0, column=0)
        
        self.tree_contas.insert('', 'end', text='0', values=('123', 'Fulano', '1000'))
        self.tree_contas.insert('', 'end', text='1', values=('123', 'Fulano', '1000'))
        self.tree_contas.insert('', 'end', text='2', values=('456', 'Ciclano', '2000'))
        self.tree_contas.insert('', 'end', text='3', values=('789', 'Beltrano', '3000'))
        
        self.tree_contas.column('#0', width=50)
        self.tree_contas.column('#1', width=145)
        self.tree_contas.column('#2', width=145)
        self.tree_contas.column('#3', width=145)
        
        self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.voltar)
        self.btn_voltar.grid(row=1, column=0, sticky=tk.NSEW)
    
    def listar_clientes(self):
        self.limpar_tela()
        self.janela.title('Listar clientes')
        self.janela.geometry('500x300')
        
        self.frame = tk.Frame(self.janela)
        self.frame.pack()
        
        self.tree_clientes = ttk.Treeview(self.frame, columns=('Nome', 'Endereço', 'CPF'))
        self.tree_clientes.heading('#0', text='ID')
        self.tree_clientes.heading('#1', text='Nome')
        self.tree_clientes.heading('#2', text='Endereço')
        self.tree_clientes.heading('#3', text='CPF')
        self.tree_clientes.grid(row=0, column=0)
        
        self.tree_clientes.insert('', 'end', text='0', values=('Fulano', 'Rua A', '123'))
        self.tree_clientes.insert('', 'end', text='1', values=('Ciclano', 'Rua B', '456'))
        self.tree_clientes.insert('', 'end', text='2', values=('Beltrano', 'Rua C', '789'))
        
        self.tree_clientes.column('#0', width=50)
        self.tree_clientes.column('#1', width=145)
        self.tree_clientes.column('#2', width=145)
        self.tree_clientes.column('#3', width=145)
        
        self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.voltar)
        self.btn_voltar.grid(row=1, column=0, sticky=tk.NSEW)
        
    def cadastrar_banco(self):
        self.limpar_tela()
        self.janela.title('Cadastrar banco')
        self.janela.geometry('500x300')
        
        self.frame = tk.Frame(self.janela)
        self.frame.pack()
        
        self.lbl_nome = tk.Label(self.frame, text='Nome:')
        self.lbl_nome.grid(row=1, column=0)
        
        self.ent_nome = tk.Entry(self.frame)
        self.ent_nome.grid(row=1, column=1)
        
        self.lbl_numero = tk.Label(self.frame, text='Agencia:')
        self.lbl_numero.grid(row=2, column=0)
        
        self.ent_numero = tk.Entry(self.frame)
        self.ent_numero.grid(row=2, column=1)
        
        self.btn_salvar = tk.Button(self.frame, text='Salvar', command=self.salvar_banco)
        self.btn_salvar.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)
        
        self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.voltar)
        self.btn_voltar.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)
        

    def listar_banco(self):
        self.limpar_tela()
        self.janela.title('Listar banco')
        self.janela.geometry('500x300')
        
        self.frame = tk.Frame(self.janela)
        self.frame.pack()
        
        scb = ttk.Scrollbar(self.frame, orient='vertical')
        scb.grid(row=0, column=2, sticky=tk.NS)
        
        colunas = ['id','numero', 'nome']
        self.tree_banco = ttk.Treeview(self.frame, show='headings', columns=colunas)
        self.tree_banco.heading('id', text='ID')
        self.tree_banco.heading('numero', text='Agencia')
        self.tree_banco.heading('nome', text='Nome')
        self.tree_banco.grid(row=0, column=0, columnspan=2)
        
        for i in Banco.bancos:
            self.tree_banco.insert('', 'end', values=(i.get_id, i.get_numero, i.get_nome))
            
        self.tree_banco.column('id', width=50)
        self.tree_banco.column('numero', width=100)
        self.tree_banco.column('nome', width=220)
        
        self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.voltar)
        self.btn_voltar.grid(row=1, column=0, sticky=tk.NSEW)
        
        self.btn_editar = tk.Button(self.frame, text='Editar', command=self.editar_banco)
        self.btn_editar.grid(row=1, column=1, sticky=tk.NSEW)
        
        self.tree_banco.config(yscrollcommand=scb.set)
        scb.config(command=self.tree_banco.yview)
                
                
    def salvar_banco(self):
        banco = Banco(self.ent_nome.get(), self.ent_numero.get())
        if self.ent_nome.get() == '' or self.ent_numero.get() == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
        else:
            messagebox.showinfo('Sucesso', 'Banco cadastrado com sucesso')
            self.voltar()
    
    def editar_banco(self):
        self.limpar_tela()
        self.janela.title('Editar banco')
        self.janela.geometry('500x300')
        
        linha = self.tree_banco.selection()
        linha_selecionada = self.tree_banco.item(linha, 'values')
        
        self.frame = tk.Frame(self.janela)
        self.frame.pack()
        
        self.lbl_id = tk.Label(self.frame, text='ID:')
        self.lbl_id.grid(row=0, column=0)
        
        self.ent_id = tk.Entry(self.frame)
        self.ent_id.grid(row=0, column=1)
        self.ent_id.insert('end', values=linha_selecionada[0])
        
        self.lbl_nome = tk.Label(self.frame, text='Nome:')
        self.lbl_nome.grid(row=1, column=0)
        
        self.ent_nome = tk.Entry(self.frame)
        self.ent_nome.grid(row=1, column=1)
        self.ent_nome.insert('end', values=linha_selecionada[1])
        
        self.lbl_numero = tk.Label(self.frame, text='Agencia:')
        self.lbl_numero.grid(row=2, column=0)
        
        self.ent_numero = tk.Entry(self.frame)
        self.ent_numero.grid(row=2, column=1)
        self.ent_numero.insert('end', values=linha_selecionada[2])
        
        self.btn_salvar = tk.Button(self.frame, text='Salvar', command=self.confirmar_edicao)
        self.btn_salvar.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)
        
        self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.voltar)
        self.btn_voltar.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)
        
    def confirmar_edicao(self):
        id = self.ent_id.get()
        nome = self.ent_nome.get()
        numero = self.ent_numero.get()
        selecionado = self.tree_banco.selection()
        if id == '' or nome == '' or numero == '':
            messagebox.showinfo('Aviso', 'Por favor, todos os campos são obrigatórios.')
        else:
            self.tree_banco.item(selecionado, values=(id, nome, numero))
            self.voltar()
            
    def cadastrar_conta(self):
        self.limpar_tela()
        self.janela.title('Cadastrar conta')
        self.janela.geometry('500x300')
        
        self.frame = tk.Frame(self.janela)
        self.frame.pack()
        
        self.lbl_numero = tk.Label(self.frame, text='Número:')
        self.lbl_numero.grid(row=0, column=0)
        
        self.ent_numero = tk.Entry(self.frame)
        self.ent_numero.grid(row=0, column=1)
        
        self.lbl_titular = tk.Label(self.frame, text='Titular:')
        self.lbl_titular.grid(row=1, column=0)
        
        self.ent_titular = tk.Entry(self.frame)
        self.ent_titular.grid(row=1, column=1)
        
        self.lbl_saldo = tk.Label(self.frame, text='Saldo:')
        self.lbl_saldo.grid(row=2, column=0)
        
        self.ent_saldo = tk.Entry(self.frame)
        self.ent_saldo.grid(row=2, column=1)
        
        self.btn_salvar = tk.Button(self.frame, text='Salvar', command=self.salvar_conta)
        self.btn_salvar.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)
        
        self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.voltar)
        self.btn_voltar.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)
    
    def salvar_conta(self):
        pass
  
    def voltar(self):
        self.limpar_tela()
        self.__init__(self.janela)
    
        
janela = tk.Tk()
app = HomeBanco(janela)
janela.mainloop()