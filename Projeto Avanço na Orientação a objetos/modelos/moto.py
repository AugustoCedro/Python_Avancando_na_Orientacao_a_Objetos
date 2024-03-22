from .veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, marca, ano, cor, preco):
        super().__init__(modelo, marca, ano, cor, preco)
    