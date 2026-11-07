from usuario import Usuario


# Relacionamento de herança: ContatoDeConfianca herda de Usuario
class ContatoDeConfianca(Usuario):

    def __init__(self, nome, email, senha, telefone, afinidade):
        super().__init__(nome, email, senha, telefone)
        self.afinidade = afinidade

    def receberAlerta(self):
        print("Alerta de emergência recebido.")

    def confirmarRecebimento(self):
        print("Recebimento do alerta confirmado.")