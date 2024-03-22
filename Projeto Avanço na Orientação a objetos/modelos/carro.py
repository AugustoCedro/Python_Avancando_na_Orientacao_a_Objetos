from .veiculo import Veiculo
import random
class Carro(Veiculo):
    def __init__(self, modelo, marca, ano, cor, preco):
        super().__init__(modelo, marca, ano, cor, preco)
        self._hibrido = 'Não'
        self._eletrico = 'Não'


    def __str__(self):
        return f'{super().__str__()} | Hibrido: {(self._hibrido).ljust(5)} | Elétrico: {(self._eletrico).ljust(4)} |'
    

    


