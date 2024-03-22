
class Veiculo:
    def __init__(self,modelo,marca,ano,cor,preco):
        self._modelo = modelo
        self._marca = marca
        self._ano = ano
        self._cor = cor
        self._preco = preco
        self._disponivel = 'Disponivel'

    def __str__(self):
        return f'| {(self._modelo).ljust(20)} | {(self._marca).ljust(20)} | {str(self._ano).ljust(5)} | {(self._cor).ljust(10)} | R$ {str(self._preco).ljust(7)} | {(self._disponivel).ljust(15)}'
    
   

    
    