class Cliente:
    """Classe que representa um cliente de uma loja."""

    def __init__(self, nome: str, idade: int, saldo: float):
        # Atributos privados (encapsulamento)
        self.__nome = nome
        self.__idade = idade
        self.__saldo = saldo

    def mostrar_informacoes(self):
        """Exibe nome, idade e saldo do cliente."""
        print(f"Cliente: {self.__nome}, Idade: {self.__idade}, Saldo: R$ {self.__saldo:.2f}")

    def atualizar_saldo(self, valor: float):
        """Atualiza o saldo (pode ser depósito ou retirada)."""
        self.__saldo += valor
        print(f"Saldo atualizado: R$ {self.__saldo:.2f}")