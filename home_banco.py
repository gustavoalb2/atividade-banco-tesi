import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import tkinter.font as tkFont
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
cli1=Cliente('Gustavo', 'Alto Alegre', '000.111.222.33')
cli2=Cliente('Jocely', 'Rui lino', '444.555.666.77')

class HomeBanco():
    def __init__ (self, master):
        self.janela = master
        self.janela.title('Banco')
        self.janela.geometry('500x300')
        
        self.fonte_titulo = tkFont.Font(size=25)
        self.frame = tk.Frame(self.janela)
        self.frame.pack()
        
        lbl_titulo = tk.Label(self.frame, text='Bem vindo ao Banco', font=self.fonte_titulo)
        lbl_titulo.pack(fill=tk.X, pady=10, padx=10, ipadx=10, ipady=10, expand=True, side=tk.TOP)
        
        self.btn_cadastrarCliente = tk.Button(self.frame, text='Cadastrar Cliente', command=self.cadastrar_clientes)
        self.btn_cadastrarCliente.pack(fill=tk.X, pady=10, padx=10, ipadx=10, ipady=10, expand=True, side=tk.TOP)
        
        self.btn_cadastrarBanco = tk.Button(self.frame, text='Cadastrar Banco', command=self.cadastrar_banco)
        self.btn_cadastrarBanco.pack(fill=tk.X, pady=10, padx=10, ipadx=10, ipady=10, expand=True, side=tk.TOP)
        
        self.btn_cadastrarConta = tk.Button(self.frame, text='Cadastrar Conta', command=self.cadastrar_conta)
        self.btn_cadastrarConta.pack(fill=tk.X, pady=10, padx=10, ipadx=10, ipady=10, expand=True, side=tk.TOP)
        
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
        
        self.btn_remover_cliente = tk.Button(self.frame, text='Remover Cliente', command=self.remover_cliente)
        self.btn_remover_cliente.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)
        
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
        if not selecionado:
            messagebox.showerror('Erro', 'Nenhuma linha selecionada')
            return    
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
        if not selecionado:
            messagebox.showerror('Erro', 'Nenhuma linha selecionada')
            return
        
        linha_selecionada = self.tree_clientes.item(selecionado, 'values')
        id = linha_selecionada[0]
        nome = self.ent_nome.get()
        endereco = self.ent_endereco.get()
        cpf = self.ent_cpf.get()

        for cliente in Cliente.clientes:
            if cliente.id == id:
                cliente.nome = nome
                cliente.endereco = endereco
                cliente.cpf = cpf
                break
        
        # Atualize a Treeview com os novos valores
        self.tree_clientes.item(selecionado, values=(id, nome, endereco, cpf))
        
        messagebox.showinfo('Sucesso', 'Cliente atualizado com sucesso')
        self.fechar_janela()
    
    def remover_cliente(self):
        selecionado = self.tree_clientes.selection()
        if not selecionado:
            messagebox.showerror('Erro', 'Nenhuma linha selecionada')
            return
        
        linha_selecionada = self.tree_clientes.item(selecionado, 'values')
        cliente_id = int(linha_selecionada[0])
        
        resultado = Cliente.remover_cliente(cliente_id)
        if resultado is None:
            messagebox.showerror('Erro', 'Cliente não encontrado')
        elif resultado:
            self.tree_clientes.delete(selecionado)
            messagebox.showinfo('Sucesso', 'Cliente removido com sucesso')
        else:
            messagebox.showerror('Erro', 'Cliente está vinculado a uma conta e não pode ser removido')
    
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
            
    def listar_contas(self):
        self.limpar_tela()
        self.janela.title('Listar contas')
        self.janela.geometry('800x500')
        self.frame = tk.Frame(self.janela)
        self.frame.pack()
                
        colunas = ['id', 'titular', 'tipo', 'saldo', 'banco']
        self.tree_contas = ttk.Treeview(self.frame, show='headings', columns=colunas)
        self.tree_contas.heading('id', text='ID')
        self.tree_contas.heading('titular', text='Titular')
        self.tree_contas.heading('tipo', text='Tipo')
        self.tree_contas.heading('saldo', text='Saldo')
        self.tree_contas.heading('banco', text='Banco')
        self.tree_contas.grid(row=0, column=0)
                
        for i in Conta.contas:
            titular_nome = i.titular if isinstance(i.titular, str) else i.titular.get()
            banco_nome = i.banco if isinstance(i.banco, str) else i.banco.get()
            self.tree_contas.insert('', tk.END, values=(i.id, titular_nome, 'Conta Poupança' if isinstance(i, ContaPoupanca) else 'Conta Corrente', i.saldo, banco_nome))
        
        self.tree_contas.column('id', width=50)
        self.tree_contas.column('titular', width=145)
        self.tree_contas.column('tipo', width=145)
        self.tree_contas.column('saldo', width=145)
        self.tree_contas.column('banco', width=145)
        
        self.btn_sacar = tk.Button(self.frame, text='Sacar', command=self.sacar)
        self.btn_sacar.grid(row=5, column=0, sticky=tk.NSEW)
        
        self.btn_depositar = tk.Button(self.frame, text='Depositar', command=self.depositar)
        self.btn_depositar.grid(row=6, column=0, sticky=tk.NSEW)
        
        self.btn_encerrar_conta = tk.Button(self.frame, text='Encerrar Conta', command=self.encerrar_conta)
        self.btn_encerrar_conta.grid(row=7, column=0, columnspan=2, sticky=tk.NSEW)
        
        self.btn_voltar = tk.Button(self.frame, text='Voltar', command=self.voltar)
        self.btn_voltar.grid(row=8, column=0, sticky=tk.NSEW)
        
    
    def salvar_conta(self):
        titular = self.cbx_titular.get()
        banco = self.cbx_banco.get()
        tipo_conta = self.cbx_tipoConta.get()
        saldo = self.ent_saldo.get()

        if titular == '' or banco == '' or tipo_conta == '' or saldo == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

        try:
            saldo = float(saldo)
        except ValueError:
            messagebox.showerror('Erro', 'Saldo deve ser um número válido')
            return

        if tipo_conta == 'Corrente':
            conta = ContaCorrente(titular, saldo, banco)  
        elif tipo_conta == 'Poupança':
            conta = ContaPoupanca(titular, saldo, banco)  
        else:
            messagebox.showerror('Erro', 'Tipo de conta inválido')
            return

        Conta.contas.append(conta)
        messagebox.showinfo('Sucesso', 'Conta criada com sucesso')
        self.voltar()
        
    def encerrar_conta(self):
        selecionado = self.tree_contas.selection()
        if not selecionado:
            messagebox.showerror('Erro', 'Nenhuma linha selecionada')
            return
        
        linha_selecionada = self.tree_contas.item(selecionado, 'values')
        conta_id = int(linha_selecionada[0])
        
        resultado = Conta.encerrar_conta(conta_id)
        if resultado is None:
            messagebox.showerror('Erro', 'Conta não encontrada')
        elif resultado:
            self.tree_contas.delete(selecionado)
            messagebox.showinfo('Sucesso', 'Conta encerrada com sucesso')
        else:
            messagebox.showerror('Erro', 'Conta não pode ser encerrada, tem dinheiro na conta')
    
    def sacar(self):
        item_selecionado = self.tree_contas.selection()
        if not item_selecionado:
            messagebox.showerror('Erro', 'Selecione uma conta')
            return
        
        valor = simpledialog.askfloat('Sacar', 'Digite o valor do saque:')
        if valor is None or valor <= 0:
            messagebox.showerror('Erro', 'Valor inválido')
            return
        
        item = self.tree_contas.item(item_selecionado)
        conta_id = item['values'][0]
        conta = next((conta for conta in Conta.contas if conta.id == conta_id), None)
        
        if conta:
            if conta.sacar(valor):
                self.tree_contas.item(item_selecionado, values=(conta.id, conta.titular, 'Conta Poupança' if isinstance(conta, ContaPoupanca) else 'Conta Corrente', conta.saldo, conta.banco))
                messagebox.showinfo('Sucesso', 'Saque realizado com sucesso')
            else:
                messagebox.showerror('Erro', 'Saldo insuficiente')
        else:
            messagebox.showerror('Erro', 'Conta não encontrada')

    def depositar(self):
        item_selecionado = self.tree_contas.selection()
        if not item_selecionado:
            messagebox.showerror('Erro', 'Selecione uma conta')
            return
        
        valor = simpledialog.askfloat('Depositar', 'Digite o valor do depósito:')
        if valor is None or valor <= 0:
            messagebox.showerror('Erro', 'Valor inválido')
            return
        
        item = self.tree_contas.item(item_selecionado)
        conta_id = item['values'][0]
        conta = next((conta for conta in Conta.contas if conta.id == conta_id), None)
        
        if conta:
            conta.depositar(valor)
            self.tree_contas.item(item_selecionado, values=(conta.id, conta.titular, 'Conta Poupança' if isinstance(conta, ContaPoupanca) else 'Conta Corrente', conta.saldo, conta.banco))
            messagebox.showinfo('Sucesso', 'Depósito realizado com sucesso')
        else:
            messagebox.showerror('Erro', 'Conta não encontrada')
            
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