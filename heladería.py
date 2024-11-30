
from restaurante import Restaurante

class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores = sabores

    def mostrar_sabores(self):
        print(f"Sabores disponibles en {self.restaurante_nombre}:")
        for sabor in self.sabores:
            print(f"- {sabor}")
