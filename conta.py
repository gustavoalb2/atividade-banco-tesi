import datetime

class Conta:
    id_conta = 0
    contas = []

    def __init__(self, titular, saldo, banco):
        self._id = Conta.id_conta + 1
        self._titular = titular
        self._saldo = float(saldo)
        self._banco = banco
        self.operacoes = []  # Lista para armazenar as operações
        Conta.id_conta += 1
        Conta.contas.append(self)

    def sacar(self, valor):
        if valor > self._saldo:
            return False
        self._saldo -= valor
        self.registrar_operacao('Saque:', valor)
        return True

    def depositar(self, valor):
        self._saldo += valor
        self.registrar_operacao('Deposito:', valor)

    def registrar_operacao(self, tipo, valor):
        data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.operacoes.append({'data': data, 'tipo': tipo, 'valor': valor})

    def gerar_relatorio(self):
        nome_arquivo = f'{self._id}.txt'
        with open(nome_arquivo, 'w') as arquivo:
            for operacao in self.operacoes:
                linha = f"{operacao['data']} {operacao['tipo']} {operacao['valor']}\n"
                arquivo.write(linha)
            arquivo.write(f'Saldo final: {self._saldo}\n')
        return nome_arquivo

    @property
    def id(self):
        return self._id

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self,valor):
        self._saldo = valor

    @property
    def titular(self):
        return self._titular

    @property
    def banco(self):
        return self._banco

class ContaCorrente(Conta):
    def __init__(self, titular, saldo, banco, desconto_fixo=5.0):
        super().__init__(titular, saldo, banco)
        self.desconto_fixo = desconto_fixo

    def sacar(self, valor):
        valor_com_desconto = valor + self.desconto_fixo
        return super().sacar(valor_com_desconto)

    def depositar(self, valor):
        valor_com_desconto = valor - self.desconto_fixo
        super().depositar(valor_com_desconto)

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, banco, taxa_juros=0.01):
        super().__init__(titular, saldo, banco)
        self.taxa_juros = taxa_juros

    def atualizar_saldo_mensal(self):
        self._saldo += self._saldo * self.taxa_juros