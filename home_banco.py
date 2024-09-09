import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from banco import Banco
from clientes import Cliente
from conta import Conta
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente

b1=Banco('Caixa', 1234)
b2=Banco('Bradesco', 5678)
b3=Banco('Nubank', 9876)
b4=Banco('PicPay', 5432)

#Criação de clientes para teste
cli1=Cliente('Mateus', 'Panorama', '000.111.222.33')
cli2=Cliente('Jocely', 'Rui lino', '444.555.666.77')
cli3=Cliente('Kaleb', 'Algum lugar', '888.999.379.52')



class HomeBanco():
    def __init__ (self, master):
        self.janela = master
        self.janela.title('Banco')
        self.janela.geometry('500x300')
        
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
        self.mnu_clientes.add_command(label='Cadastrar clientes', command=self.cadastrar_clientes)
        
        self.mnu_banco.add_command(label='Listar banco', command=self.listar_banco) #comandos
        self.mnu_banco.add_separator()
        self.mnu_banco.add_command(label='Cadastrar banco', command=self.cadastrar_banco)
        
        self.janela.config(menu=self.mnu_barra)
    
    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
        
    def listar_clientes(self):
        self.limpar_tela()
        self.janela.title('Listar clientes')
        self.janela.geometry('500x300')
        
        self.frame = tk.Frame(self.janela)
        self.frame.pack()
        
        scb = ttk.Scrollbar(self.frame, orient='vertical')
        scb.grid(row=0, column=2, sticky=tk.NS)
        
        colunas = ['id', 'nome', 'endereco', 'cpf']
        self.tree_clientes = ttk.Treeview(self.frame, show='headings', columns=colunas)
        self.tree_clientes.heading('id', text='ID')
        self.tree_clientes.heading('nome', text='Nome')
        self.tree_clientes.heading('endereco', text='Endereço')
        self.tree_clientes.heading('cpf', text='CPF')
        self.tree_clientes.grid(row=0, column=0, columnspan=2)
        
        self.tree_clientes.column('id', width=50)
        self.tree_clientes.column('nome', width=145)
        self.tree_clientes.column('endereco', width=145)
        self.tree_clientes.column('cpf', width=145)
        
        for i in Cliente.clientes:
            self.tree_clientes.insert('', 'end', values=(i.id, i.nome, i.endereco, i.cpf))
        
        self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.voltar)
        self.btn_voltar.grid(row=1, column=0, sticky=tk.NSEW)
        
        self.btn_editarCliente = tk.Button(self.frame, text='Editar', command=self.editar_cliente)
        self.btn_editarCliente.grid(row=1, column=1, sticky=tk.NSEW)
        
        self.tree_clientes.config(yscrollcommand=scb.set)
        scb.config(command=self.tree_clientes.yview)
        
    def cadastrar_clientes(self):
        self.limpar_tela()
        self.janela.title('Cadastrar clientes')
        self.janela.geometry('500x300')
        
        self.frame = tk.Frame(self.janela)
        self.frame.pack()
        
        self.lbl_nome = tk.Label(self.frame, text='Nome:')
        self.lbl_nome.grid(row=1, column=0)
        
        self.ent_nome = tk.Entry(self.frame)
        self.ent_nome.grid(row=1, column=1)
        
        self.lbl_endereco = tk.Label(self.frame, text='Endereço:')
        self.lbl_endereco.grid(row=2, column=0)
        
        self.ent_endereco = tk.Entry(self.frame)
        self.ent_endereco.grid(row=2, column=1)
        
        self.lbl_cpf = tk.Label(self.frame, text='CPF:')
        self.lbl_cpf.grid(row=3, column=0)
        
        self.ent_cpf = tk.Entry(self.frame)
        self.ent_cpf.grid(row=3, column=1)
        
        self.btn_salvar = tk.Button(self.frame, text='Salvar', command=self.salvar_cliente)
        self.btn_salvar.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)
        
        self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.voltar)
        self.btn_voltar.grid(row=5, column=0, columnspan=2, sticky=tk.NSEW)
        
    def salvar_cliente(self):
        cliente = Cliente(self.ent_nome.get(), self.ent_cpf.get(), self.ent_endereco.get())
        if self.ent_nome.get() == '' or self.ent_endereco.get() == '' or self.ent_cpf.get() == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
        else:
            messagebox.showinfo('Sucesso', 'Cliente cadastrado com sucesso')
            self.voltar()
    
    def editar_cliente(self):
        selecionado = self.tree_clientes.selection()
        linha_selecionada = self.tree_clientes.item(selecionado, 'values')      
                     
        self.top_editar = tk.Toplevel(self.janela)
        self.top_editar.title('Editar Cliente')
        self.top_editar.geometry('500x300')
            
        self.frame = tk.Frame(self.top_editar)
        self.frame.pack()
                        
        self.lbl_nome = tk.Label(self.frame, text='Nome:')
        self.lbl_nome.grid(row=1, column=0)
            
        self.ent_nome = tk.Entry(self.frame)
        self.ent_nome.grid(row=1, column=1)
        self.ent_nome.insert('end', linha_selecionada[1])
            
        self.lbl_endereco = tk.Label(self.frame, text='Endereço:')
        self.lbl_endereco.grid(row=2, column=0)
            
        self.ent_endereco = tk.Entry(self.frame)
        self.ent_endereco.grid(row=2, column=1)
        self.ent_endereco.insert('end', linha_selecionada[2])
            
        self.lbl_cpf = tk.Label(self.frame, text='CPF:')
        self.lbl_cpf.grid(row=3, column=0)
            
        self.ent_cpf = tk.Entry(self.frame)
        self.ent_cpf.grid(row=3, column=1)
        self.ent_cpf.insert('end', linha_selecionada[3])
            
        self.btn_salvar = tk.Button(self.frame, text='Salvar', command=self.confirmar_edicaoCliente)
        self.btn_salvar.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)
            
        self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.fechar_janela)
        self.btn_voltar.grid(row=5, column=0, columnspan=2, sticky=tk.NSEW)
            
        self.top_editar.grab_set() # Impede a interação com a janela Tk
        self.janela.protocol("WM_DELETE_WINDOW", self.desabilita_fechar)
        self.top_editar.protocol("WM_DELETE_WINDOW", self.fechar_janela)
    
    def confirmar_edicaoCliente(self):
        selecionado = self.tree_clientes.selection()
        if selecionado:
            linha_selecionada = self.tree_clientes.item(selecionado, 'values')
            id = linha_selecionada[0]
            nome = self.ent_nome.get()
            endereco = self.ent_endereco.get()
            cpf = self.ent_cpf.get()
            if nome == '' or endereco == '' or cpf == '':
                messagebox.showinfo('Aviso', 'Por favor, todos os campos são obrigatórios.')
            else:
                self.tree_clientes.item(selecionado, values=(id, nome, endereco, cpf))
                self.fechar_janela()
    
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
            self.tree_banco.insert('', 'end', values=(i.id, i.numero, i.nome))
            
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
        selecionado = self.tree_banco.selection()
        if selecionado:
            linha_selecionada = self.tree_banco.item(selecionado, 'values')
            
            self.top_editar = tk.Toplevel(self.janela)
            self.top_editar.title('Editar Banco')
            
            self.frame = tk.Frame(self.top_editar)
            self.frame.pack()
                        
            self.lbl_nome = tk.Label(self.frame, text='Nome:')
            self.lbl_nome.grid(row=1, column=0)
            
            self.ent_nome = tk.Entry(self.frame)
            self.ent_nome.grid(row=1, column=1)
            self.ent_nome.insert('end', linha_selecionada[1])
            
            self.lbl_numero = tk.Label(self.frame, text='Número:')
            self.lbl_numero.grid(row=2, column=0)
            
            self.ent_numero = tk.Entry(self.frame)
            self.ent_numero.grid(row=2, column=1)
            self.ent_numero.insert('end', linha_selecionada[2])
            
            self.btn_salvar = tk.Button(self.frame, text='Salvar', command=self.confirmar_edicaoBanco)
            self.btn_salvar.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)
            
            self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.fechar_janela)
            self.btn_voltar.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)
            
            self.top_editar.grab_set() # Impede a interação com a janela Tk
            self.janela.protocol("WM_DELETE_WINDOW", self.desabilita_fechar)
            self.top_editar.protocol("WM_DELETE_WINDOW", self.fechar_janela)
        
    def confirmar_edicaoBanco(self):
        selecionado = self.tree_banco.selection()
        if selecionado:
            linha_selecionada = self.tree_banco.item(selecionado, 'values')
            id = linha_selecionada[0]
            nome = self.ent_nome.get()
            numero = self.ent_numero.get()
            if nome == '' or numero == '':
                messagebox.showinfo('Aviso', 'Por favor, todos os campos são obrigatórios.')
            else:
                self.tree_banco.item(selecionado, values=(id, nome, numero))
                self.fechar_janela()
    
    def listar_contas(self):
        self.limpar_tela()
        self.janela.title('Listar contas')
        self.janela.geometry('650x300')
        self.frame = tk.Frame(self.janela)
        self.frame.pack()
                
        colunas = ['tipo','id', 'titular', 'saldo']
        self.tree_contas = ttk.Treeview(self.frame, show='headings', columns=colunas)
        self.tree_contas.heading('tipo', text='tipo')
        self.tree_contas.heading('id', text='ID')
        self.tree_contas.heading('titular', text='Titular')        
        self.tree_contas.heading('saldo', text='Saldo')
        self.tree_contas.grid(row=0, column=0)
        
        for i in Conta.listar_contas:
            self.tree_contas.insert('', tk.END, values=(i.titular, i.saldo))
        
        self.tree_contas.column('tipo', width=145)
        self.tree_contas.column('id', width=50)
        self.tree_contas.column('titular', width=145)
        self.tree_contas.column('saldo', width=145)
        
        self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.voltar)
        self.btn_voltar.grid(row=1, column=0, sticky=tk.NSEW)
    
                
    def cadastrar_conta(self):
            self.limpar_tela()
            self.janela.title('Cadastrar conta')
            self.janela.geometry('500x300')
            
            self.frame = tk.Frame(self.janela)
            self.frame.pack()
            
            self.lbl_titular = tk.Label(self.frame, text='Titular:')
            self.lbl_titular.grid(row=1, column=0)
                        
            listar_clientes = Cliente.listar_clientes()
            titular = [f"{titular.nome}" for titular in listar_clientes]
            self.cbx_titular = ttk.Combobox(self.frame, values=titular, state="readonly")
            self.cbx_titular.grid(row=1, column=1)
            
            self.lbl_banco = tk.Label(self.frame, text='Banco:')
            self.lbl_banco.grid(row=2, column=0)
            
            listar_banco = Banco.listar_banco()
            banco = [f"{banco.nome}" for banco in listar_banco]
            self.cbx_banco = ttk.Combobox(self.frame, values=banco, state="readonly")
            self.cbx_banco.grid(row=2, column=1)
            
            self.lbl_tipoConta = tk.Label(self.frame, text='Tipo de conta:')
            self.lbl_tipoConta.grid(row=3, column=0)
            
            self.cbx_tipoConta = ttk.Combobox(self.frame, values=['Corrente', 'Poupança'], state="readonly")
            self.cbx_tipoConta.grid(row=3, column=1)
            
            self.lbl_saldo = tk.Label(self.frame, text='Saldo:')           
            self.lbl_saldo.grid(row=4, column=0)
            
            self.ent_saldo = tk.Entry(self.frame)
            self.ent_saldo.grid(row=4, column=1)
            
            self.btn_salvar = tk.Button(self.frame, text='Salvar', command=self.salvar_conta)
            self.btn_salvar.grid(row=5, column=0, columnspan=2, sticky=tk.NSEW)
            
            self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.voltar)
            self.btn_voltar.grid(row=6, column=0, columnspan=2, sticky=tk.NSEW)
            
    def salvar_conta(self):
        conta = Conta(self.cbx_titular, self.cbx_banco.get())
        if self.cbx_titular.get() == '' or self.cbx_banco.get() == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
        else:
            messagebox.showinfo('Sucesso', 'Banco cadastrado com sucesso')
            self.voltar()
        
    def desabilita_fechar(self):
        pass
        
    def fechar_janela(self):
            self.top_editar.destroy()
            self.janela.protocol("WM_DELETE_WINDOW", self.janela.destroy)
    
    def voltar(self):
            self.limpar_tela()
            self.__init__(self.janela)
    
        
janela = tk.Tk()
app = HomeBanco(janela)
janela.mainloop()