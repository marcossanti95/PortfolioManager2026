class Exportable:
    def exportar_txt(self, nombre_archivo):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(str(self))
        print(f"Exportado a {nombre_archivo}")


class Cartera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.activos = []

    def agregar_activo(self, activo):
        self.activos.append(activo)

    def valor_total(self):
        total = 0
        for activo in self.activos:
            total += activo.calcular_valor()
        return total

    def mostrar_resumen(self):
        print(f"Cartera: {self.nombre}")
        for activo in self.activos:
            print(activo)
        print(f"Valor total: {self.valor_total()}")

    def __str__(self):
        resultado = f"Cartera: {self.nombre}\n"
        for activo in self.activos:
            resultado += f"{activo}\n"
        resultado += f"Valor total: {self.valor_total()}"
        return resultado


class CarteraExportable(Cartera, Exportable):
    def __init__(self, nombre):
        super().__init__(nombre)