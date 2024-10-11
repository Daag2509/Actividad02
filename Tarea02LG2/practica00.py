class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"Vehículo: {self.marca} {self.modelo}, Año: {self.año}"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, numeroPuertas):
        super().__init__(marca, modelo, año)
        self.numeroPuertas = numeroPuertas

    def descripcion(self):
        return f"Coche: {self.marca} {self.modelo}, Año: {self.año}, Puertas: {self.numeroPuertas}"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipoBicicleta):
        super().__init__(marca, modelo, año)
        self.tipoBicicleta = tipoBicicleta

    def descripcion(self):
        return f"Bicicleta: {self.marca} {self.modelo}, Año: {self.año}, Tipo: {self.tipoBicicleta}"

#Uso
if __name__ == "__main__":
    coche1 = Coche("Toyota", "Corolla", 1998, 4)
    bicicleta1 = Bicicleta("Greco", "Modelo 3", 2021, "Carretera")

    print(coche1.descripcion())
    print(bicicleta1.descripcion())