class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} {self.modelo} foi ligado.")
        else:
            print(f"{self.marca} {self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.marca} {self.modelo} foi desligado.")
        else:
            print(f"{self.marca} {self.modelo} já está desligado.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        # chama o construtor da classe pai
        super().__init__(marca, modelo)
        self.portas = portas

    def buzinar(self):
        print(f"{self.marca} {self.modelo} está buzinando: BEEP BEEP!")

carro1 = Carro("Toyota", "Corolla", 4)

carro1.ligar()
carro1.buzinar()
carro1.desligar()