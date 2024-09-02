class Banco:
    id_banco = 0
    bancos = []
    def __init__(self, nome, numero):
        self._id = Banco.id_banco + 1
        self.__numero = numero
        self.__nome = nome
        self.__contas = []
        Banco.id_banco += 1
        Banco.bancos.append(self)
    
    def adicionar_banco(self, banco):
        Banco.bancos.append(banco)
        
    def adicionar_conta(self, conta):
        self.__contas.append(conta)
    
    @property
    def get_id(self):
        return self._id
    
    @property    
    def get_numero(self):
        return self.__numero
    
    @property
    def get_nome(self):
        return self.__nome
    
    @property
    def get_contas(self):
        return self.__contas