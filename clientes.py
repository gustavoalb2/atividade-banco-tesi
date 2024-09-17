from conta import Conta

class Cliente:
    id_cliente = 0    
    clientes = []
    def __init__(self, nome, endereco, cpf):
        self._id = Cliente.id_cliente + 1
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        Cliente.id_cliente += 1
        Cliente.clientes.append(self)
    
    def adicionar_cliente(self, cliente):
        Cliente.clientes.append(cliente)
    
    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
        
    @property
    def cpf(self):
        return self.__cpf
    
    @classmethod
    def listar_clientes(cls):
        return cls.clientes
    
    @classmethod
    def remover_cliente(cls, cliente_id):
        cliente = next((c for c in cls.clientes if c.id == cliente_id), None)
        if cliente:
            if not any(isinstance(conta.titular, Cliente) and conta.titular.id == cliente_id for conta in Conta.contas):
                cls.clientes.remove(cliente)
                return True
            else:
                return False
        return None