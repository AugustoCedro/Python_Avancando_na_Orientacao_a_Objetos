from modelos.carro import Carro
from modelos.moto import Moto
from modelos.cliente import Cliente
from modelos.veiculos_payload import Payload
import os

def main():
    inventario = Payload()
    lista_clientes = []

                      
    def menu():
        while True:
            try:
                print('BEM VINDO A CONCESSIONÁRIA VELOCIDADE MAX\n')
                print('oque você deseja fazer?\n')
                print('1 - Realizar Cadastro na loja')
                print('2 - Ver tabela de Veículos')
                print('3 - Comprar um Veículo')
                print('4 - Sair do programa')

                escolha = int(input('\n'))
                if escolha == 1:
                    cadastro_cliente()
                elif escolha == 2:
                    lista_de_veiculos()
                elif escolha == 3:
                    comprar_veiculo()
                elif escolha == 4:
                    sair_do_programa()
                    break
                else:
                    input('Escolha inválida tente novamente')
                    limpar_terminal()
            except ValueError:
                    input('Escolha inválida tente novamente')
                    limpar_terminal()
                    
                
    
    def lista_de_veiculos():
        limpar_terminal()
        print(f'| {'Modelo'.ljust(20)} | {'Marca'.ljust(20)} | {'Ano'.ljust(5)} | {'Cor'.ljust(10)} | R$ {'Preço'.ljust(7)} | {('Disponibilidade').ljust(15)} |{'Tipo'.rjust(18)} {'|'.rjust(15)}')
        inventario.listar_veiculos

        voltar_ao_menu()


    def voltar_ao_menu():
        input(f'\n Aperte uma tecla para voltar ao menu principal')
        limpar_terminal()
        menu()
    
    def cadastro_cliente():
        limpar_terminal()
        print('Sistema de Cadastro')
        while True:
            try:
                nome_usuario = input('Escreva seu nome: ')
                sobrenome_usuario = input('Escreva seu sobrenome: ')
                telefone_usuario = int(input('Escreva seu telefone com DDD: '))
                email_usuario = input('Escreva seu email: ')

                print('Seus dados estão corretos?')
                print(f'{nome_usuario} {sobrenome_usuario} | {telefone_usuario} | {email_usuario}\n')
                print('0 - Sim')
                print('1 - Não\n')
                escolha = int(input(''))
                if escolha == 0:
                    cliente_data = {'nome':nome_usuario,'sobrenome':sobrenome_usuario,'telefone':telefone_usuario,'email':email_usuario}
                    lista_clientes.append(Cliente(**(cliente_data)))
                    break
                else:
                    limpar_terminal()
            except:
                input('\nInformações inválidas, tente novamente')
        
        voltar_ao_menu()

    def limpar_terminal():
        os.system('cls')

    def comprar_veiculo():
        limpar_terminal()
        print('Digite seu EMAIL de Cadastro da loja\n')
        email = input('')
        for cliente in lista_clientes:
            if email == cliente._email:
                print('Email encontrado com sucesso, prosseguindo com o cadastro')
                print('Qual o modelo do veiculo que você quer comprar: ')
                modelo = input('').lower()
                print('Qual a marca do veiculo que você quer comprar: ')
                marca = input('').lower()
                print('Qual o ano do veiculo que você quer comprar: ')
                ano = int(input(''))
                
                inventario.procurar_veiculo(marca,modelo,ano)
        
                print('Esse é o veiculo que você quer comprar?')
                print('0 - Sim')
                print('1 - Não')
                escolha = int(input(''))
                if escolha == 0:
                    if inventario.verificar_disponibilidade(marca,modelo,ano):
                        print('Veículo disponivel, efetuando a compra...')
                        print('COMPRA EFETUADA COM SUCESSO')
                    else:
                        print('Veículo Indisponível no momento')
                voltar_ao_menu()
            
            else:
                print('Email não encontrado, tente novamente ou realize o cadastro na loja')
                voltar_ao_menu()

    def sair_do_programa():
        limpar_terminal()
    
    menu()

        
if __name__ == '__main__':
    main()