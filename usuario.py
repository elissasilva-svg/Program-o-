from abc import ABC, abstractmethod


# Classe abstrata
class Usuario(ABC):

    def __init__(self, nome, email, senha, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone

    def login(self):
        return True

    def recuperarSenha(self):
        print("Processo de recuperação de senha iniciado.")