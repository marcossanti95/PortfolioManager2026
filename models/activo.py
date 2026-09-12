class Activo:
    def __init__(self, ticker, cantidad, precio, moneda):
        self.ticker = ticker
        self.moneda = moneda
        self.set_cantidad(cantidad)
        self.set_precio(precio)

    def set_precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser positivo.")
        self.__precio = valor

    def get_precio(self):
        return self.__precio

    def set_cantidad(self, valor):
        if valor <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        self.__cantidad = valor

    def get_cantidad(self):
        return self.__cantidad

    def calcular_valor(self):
        return self.get_cantidad() * self.get_precio()

    def __str__(self):
        return f"{self.ticker} | Cantidad: {self.get_cantidad()} | Precio: {self.get_precio()} | Valor: {self.calcular_valor()} | Moneda: {self.moneda}"


class ActivoRentaVariable(Activo):
    def __init__(self, ticker, cantidad, precio, moneda):
        super().__init__(ticker, cantidad, precio, moneda)


class ActivoRentaFija(Activo):
    def __init__(self, ticker, cantidad, precio, moneda):
        super().__init__(ticker, cantidad, precio, moneda)

    def calcular_valor(self):
        return (self.get_precio() * self.get_cantidad()) / 100