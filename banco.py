
class Banco:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def cadastrar_banco(self):
        # Lógica para cadastrar o banco no sistema
        # Aqui você pode adicionar o código necessário para armazenar as informações do banco

        print("Banco cadastrado com sucesso!")

# Exemplo de uso da classe
novo_banco = Banco("Meu Banco", "Rua Principal, 123", "(00) 1234-5678")
novo_banco.cadastrar_banco()