from usuario import Usuario
from endereco_fixo import EnderecoFixo

# Relacionamento de herança: Usuaria herda de Usuario
class Usuaria(Usuario):

    def __init__(self, nome, email, senha, telefone, cpf, rua, numero, bairro, cep):
        super().__init__(nome, email, senha, telefone)

        self.cpf = cpf
        self.contatos = []
        self.historico = []
        self.localizacao = None
        self.gravacoes = []

    # Composição: Usuaria possui um EnderecoFixo
        self.endereco = EnderecoFixo(rua, numero, bairro, cep)

    def acionarPanico(self):
        print("Botão de pânico acionado.")

    def iniciarGravacao(self):
        print("Gravação de áudio iniciada.")

    def adicionarGravacao(self, gravacao):
        # Associação entre Usuaria e GravacaoAudio
        self.gravacoes.append(gravacao)

    def getCpf(self):
        return self.cpf

    def setLocalizacao(self, localizacao):
        self.localizacao = localizacao