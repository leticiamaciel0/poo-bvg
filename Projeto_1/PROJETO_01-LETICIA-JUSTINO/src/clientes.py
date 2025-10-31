class Cliente:
    def __init__(self, nome, idade, saldo):
        self.nome = nome
        self.idade = idade
        self.saldo = saldo

    def mostrar_informacoes(self):
        print(f"Cliente: {self.nome}, idade: {self.idade}, saldo: {self.saldo}")

    def atualizar_saldo(self, valor):
        self.saldo += valor
