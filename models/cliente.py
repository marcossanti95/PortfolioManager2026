class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.carteras = []

    def agregar_cartera(self, cartera):
        self.carteras.append(cartera)

    def valor_total_cliente(self):
        total = 0
        for cartera in self.carteras:
            total += cartera.valor_total()
        return total

    def __str__(self):
        return f"Cliente: {self.nombre} | Email: {self.email} | Carteras: {len(self.carteras)}"