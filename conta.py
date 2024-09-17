class Conta:
    id_conta = 0
    contas = []
    def __init__(self, cli, saldo, banco):
        self._id = Conta.id_conta + 1
        self._titular = cli
        self._saldo = float(saldo)
        self._banco = banco
        Conta.id_conta += 1
        Conta.contas.append(self)
        
    def adicionar_conta(self, contas):
        self.contas.append(contas)
        
    @classmethod
    def listar_contas(cls):
        return cls.contas
    
    @classmethod
    def encerrar_conta(cls, conta_id):
        conta = next((c for c in cls.contas if c.id == conta_id), None)
        if conta:
            if conta.saldo == 0:
                cls.contas.remove(conta)
                return True
            else:
                return False
        return None
          
    @property
    def id(self):
        return self._id
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def banco(self):
        return self._banco
        
    @property
    def titular(self):
        return self._titular
    
    def sacar(self, valor):
        if valor > self._saldo:
            return False
        self._saldo -= valor
        return True
    
    def depositar(self, valor):
        self._saldo += valor
        return True
