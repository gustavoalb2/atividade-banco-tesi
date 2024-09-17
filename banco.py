from conta import Conta
class Banco:
    id_banco = 0
    bancos = []
    taxaCC = 0.08
    taxaCP = 0.03
    def __init__(self, nome, numero):
        self._id = Banco.id_banco + 1
        self.__numero = numero
        self.__nome = nome
        Banco.id_banco += 1
        Banco.bancos.append(self)
    
    def adicionar_banco(self, banco):
        Banco.bancos.append(banco)
        
    @classmethod
    def listar_banco(cls):
        return cls.bancos
    
    @property
    def id(self):
        return self._id
    
    @property    
    def numero(self):
        return self.__numero
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def contas(self):
        return [conta for conta in Conta.contas if conta.banco == self]