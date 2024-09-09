from clientes import Cliente
from banco import Banco

class Conta:
    id_conta = 0
    contas = []
    def __init__(self, cli, sal=0.0):
        self.__id = Conta.id_conta + 1
        self.__titular = cli
        self.__saldo = sal
        Conta.id_conta += 1
        Conta.contas.append(self)
        
    def adicionar_conta(self, contas):
        self.contas.append(contas)
        
    @classmethod
    def listar_contas(cls):
        return cls.contas
            
    @property
    def id(self):
        return self.__id
        
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, cli):
        self.__titular = cli
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, sal):
        self.__saldo = sal
        
    
    
    