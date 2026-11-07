class Localizacao:

    def __init__(self, latitude, longitude, endereco):
        self.latitude = latitude
        self.longitude = longitude
        self.endereco = endereco

    def capturarLocalizacao(self):
        print("Localização atual capturada.")

    def obterEndereco(self):
        return self.endereco