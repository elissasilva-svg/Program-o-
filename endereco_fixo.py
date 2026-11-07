class EnderecoFixo:

    def __init__(self, rua, numero, bairro, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cep = cep

    def capturarLocalizacaoFixa(self):
        print("Localização fixa do endereço capturada.")

    def obterEndereco(self):
        return f"{self.rua}, {self.numero} - {self.bairro} - CEP: {self.cep}"