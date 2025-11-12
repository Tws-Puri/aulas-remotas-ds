
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def exibir_informacoes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Portas: {self.numero_portas}"