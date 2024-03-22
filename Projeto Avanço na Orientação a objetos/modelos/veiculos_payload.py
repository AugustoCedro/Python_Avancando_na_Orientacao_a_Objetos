from .carro import Carro
from .moto import Moto
import random
class Payload:

    def __init__(self):
        self._lista_veiculos = self.carregar_lista()
        


    def carregar_lista(self):
        carros_data = [
            {'marca': 'volkswagen', 'modelo': 'golf', 'ano': 2018, 'cor': 'azul', 'preco': 50000},
            {'marca': 'toyota', 'modelo': 'corolla', 'ano': 2017, 'cor': 'prata', 'preco': 60000},
            {'marca': 'ford', 'modelo': 'mustang', 'ano': 2020, 'cor': 'vermelho', 'preco': 70000},
            {'marca': 'chevrolet', 'modelo': 'camaro', 'ano': 2019, 'cor': 'preto', 'preco': 80000},
            {'marca': 'bmw', 'modelo': 'série 3', 'ano': 2016, 'cor': 'branco', 'preco': 90000},
            {'marca': 'mercedes-benz', 'modelo': 'classe c', 'ano': 2015, 'cor': 'cinza', 'preco': 100000},
            {'marca': 'honda', 'modelo': 'civic', 'ano': 2018, 'cor': 'azul', 'preco': 55000},
            {'marca': 'audi', 'modelo': 'a4', 'ano': 2017, 'cor': 'prata', 'preco': 85000},
            {'marca': 'nissan', 'modelo': 'altima', 'ano': 2019, 'cor': 'vermelho', 'preco': 65000},
            {'marca': 'tesla', 'modelo': 'model 3', 'ano': 2020, 'cor': 'preto', 'preco': 120000}
        ]

        motos_data = [
            {'marca': 'honda', 'modelo': 'cb 500f', 'ano': 2021, 'cor': 'vermelho', 'preco': 20000},
            {'marca': 'yamaha', 'modelo': 'mt-07', 'ano': 2020, 'cor': 'preto', 'preco': 25000},
            {'marca': 'kawasaki', 'modelo': 'ninja 400', 'ano': 2019, 'cor': 'verde', 'preco': 22000},
            {'marca': 'bmw', 'modelo': 's 1000 rr', 'ano': 2022, 'cor': 'azul', 'preco': 30000},
            {'marca': 'ducati', 'modelo': 'panigale v4', 'ano': 2021, 'cor': 'branco', 'preco': 35000},
            {'marca': 'suzuki', 'modelo': 'gsx-r750', 'ano': 2020, 'cor': 'amarelo', 'preco': 27000},
            {'marca': 'triumph', 'modelo': 'street triple', 'ano': 2021, 'cor': 'laranja', 'preco': 28000},
            {'marca': 'harley-davidson', 'modelo': 'sportster iron 883', 'ano': 2020, 'cor': 'prata', 'preco': 32000},
            {'marca': 'indian', 'modelo': 'scout sixty', 'ano': 2019, 'cor': 'marrom', 'preco': 40000}
        ]

        lista_carros = [Carro(**carros_data) for carros_data in carros_data]
        lista_motos = [Moto(**motos_data) for motos_data in motos_data]
        lista_veiculos = lista_carros + lista_motos
        for veiculo in lista_veiculos:
            veiculo._disponivel = self.randomizar_disponibilidade()
            if hasattr(veiculo,'_hibrido'):
                self.randomizar_tipagem_do_carro(veiculo)
        return lista_veiculos
    
    @property
    def listar_veiculos(self):
        for veiculo in self._lista_veiculos:
            if hasattr(veiculo,'_hibrido'):
                print(veiculo)
            else:
                print(f'{veiculo} |{'X'.rjust(8)}{('|'.rjust(9))}{'X'.rjust(8)}{('|'.rjust(9))}')
    
    @classmethod
    def randomizar_disponibilidade(self):
        num = random.choice([1,2,3])
        if num == 1 or num == 2:
           return 'Disponível'
        else:
           return 'Indisponível'
    
    @classmethod
    def randomizar_tipagem_do_carro(self,carro):
        tipo = random.choice([1,2,3])
        if tipo == 1:
           carro._hibrido = 'Sim'
           carro._eletrico = 'Não'
        elif tipo == 2:
           carro._hibrido = 'Não'
           carro._eletrico = 'Sim'
        else:
            carro._hibrido = 'Não'
            carro._eletrico = 'Não'  
    
    def procurar_veiculo(self,marca,modelo,ano):
        for veiculo in self._lista_veiculos:
            if modelo == veiculo._modelo and marca == veiculo._marca and ano == veiculo._ano:
               print(veiculo)
            
    
            
    def verificar_disponibilidade(self,marca,modelo,ano):
        for veiculo in self._lista_veiculos:
            if modelo == veiculo._modelo and marca == veiculo._marca and ano == veiculo._ano:
               if veiculo._disponivel == 'Disponível':
                   veiculo._disponivel = 'Indisponível'
                   return True
               else:
                   return False
    
   
    
