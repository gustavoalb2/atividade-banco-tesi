class Banco:
    id_banco = 0
    bancos = []
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
    @id.setter
    def set_id(self, id):
        self._id = id
    
    @property    
    def numero(self):
        return self.__numero
    @numero.setter
    def set_numero(self, numero):
        self.__numero = numero
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def set_nome(self, nome):
        self.__nome = nome
    
    @property
    def contas(self):
        return self.__contas