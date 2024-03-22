
class Cliente:
    def __init__(self,nome,sobrenome,telefone,email):
        self._nome = nome
        self._sobrenome = sobrenome
        self._telefone = telefone
        self._email = email
    
    def __str__(self):
        return f'| {(self._nome)} {(self._sobrenome).ljust(10)} | {str(self._telefone).ljust(10)} | {(self._email).ljust(15)} | '
    