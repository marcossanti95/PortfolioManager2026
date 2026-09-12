# ticker = input("Ingrese el ticker del activo: ")

# while True:
#     try:
#         precio = float(input("Ingrese el precio del activo: ")) 
#         break
#     except ValueError:
#         print("Error: El precio debe ser un número.")
    

# moneda = input("Ingrese la moneda del activo: ")

# while True:
#     try:
#         cantidad = float(input("Ingrese la cantidad del activo: "))
#         break
#     except ValueError:
#         print("Error: La cantidad debe ser un número.")
    

# valor = cantidad * precio

# print("activo:", ticker)
# print("precio:", precio)
# print("moneda:", moneda)
# print("valor:", valor)

# if moneda == "ARS":
#     print("Activo en pesos argentinos")
# elif moneda == "USD":
#     print("Activo en dólares estadounidenses")
# else:
#     print("Moneda no reconocida")
    
#### Funciones ####

# def pedir_numero(mensaje, permitir_negativos=False):
#     while True:
#         try:
#             num = float(input(mensaje))
#             if not permitir_negativos and num <= 0:
#                 print("Error: El número debe ser positivo.")
#             else:
#                 return num
#         except ValueError:
#             print("Error: Debe ingresar un número válido.")
            
# ticker = input("Ingrese el ticker del activo: ")
# precio = pedir_numero("Ingrese el precio del activo: ")
# moneda = input("Ingrese la moneda del activo: ")
# cantidad = pedir_numero("Ingrese la cantidad del activo: ")
# valor = cantidad * precio

# print("activo:", ticker)
# print("precio:", precio)
# print("moneda:", moneda)
# print("valor:", valor)

# if moneda == "ARS":
#     print("Activo en pesos argentinos")
# elif moneda == "USD":
#     print("Activo en dólares estadounidenses")
# else:
#     print("Moneda no reconocida")

#### DICCIONARIOS ####

# cartera = []

# while True:
#     activo = input("Ingrese un activo (o 'salir' para terminar): ")
#     if activo.lower() == "salir":
#         break
#     cantidad_activo = pedir_numero(f"Ingrese la cantidad de {activo}: ")
#     precio_activo = pedir_numero(f"Ingrese el precio de {activo}: ") 
#     valor_activo = cantidad_activo * precio_activo
#     while True:
#         moneda = input(f"Ingrese la moneda de {activo} (ARS/USD): ")
#         if moneda in ["ARS", "USD"]:
#             break
#         else:
#             print("Moneda no reconocida. Por favor ingrese 'ARS' o 'USD'.")
        
#     cartera.append({"activo": activo, "cantidad": cantidad_activo, "precio": precio_activo, "valor": valor_activo, "moneda": moneda})
    
# print(cartera)

# for activo in cartera:
#     print(f"Activo: {activo['activo']}, Cantidad: {activo['cantidad']}, Precio: {activo['precio']}, Valor: {activo['valor']}, Moneda: {activo['moneda']}")
    
##### POO #####

# class Activo:
#     def __init__(self, ticker, cantidad, precio, moneda):
#         self.ticker = ticker
#         self.moneda = moneda
#         self.set_cantidad(cantidad)
#         self.set_precio(precio)

#     def set_precio(self, valor):
#         if valor <= 0:
#             raise ValueError("El precio debe ser positivo.")
#         self.__precio = valor

#     def get_precio(self):
#         return self.__precio

#     def set_cantidad(self, valor):
#         if valor <= 0:
#             raise ValueError("La cantidad debe ser positiva.")
#         self.__cantidad = valor

#     def get_cantidad(self):
#         return self.__cantidad

#     def calcular_valor(self):
#         return self.get_cantidad() * self.get_precio()

#     def __str__(self):
#         return f"{self.ticker} | Cantidad: {self.get_cantidad()} | Precio: {self.get_precio()} | Valor: {self.calcular_valor()} | Moneda: {self.moneda}"
    
# class ActivoRentaVariable(Activo):
#     def __init__(self, ticker, cantidad, precio, moneda, sector):
#         super().__init__(ticker, cantidad, precio, moneda)
#         self.sector = sector

#     def __str__(self):
#         return super().__str__() + f" | Sector: {self.sector}"


# class ActivoRentaFija(Activo):
#     def __init__(self, ticker, cantidad, precio, moneda, tasa):
#         super().__init__(ticker, cantidad, precio, moneda)
#         self.tasa = tasa

#     def calcular_valor(self):
#         valor_base = super().calcular_valor()
#         return valor_base * (1 + self.tasa / 100)

#     def __str__(self):
#         return super().__str__() + f" | Tasa: {self.tasa}%"

# class ActivoRentaVariable(Activo):
#     def __init__(self, ticker, cantidad, precio, moneda):
#         super().__init__(ticker, cantidad, precio, moneda)


# class ActivoRentaFija(Activo):
#     def __init__(self, ticker, cantidad, precio, moneda):
#         super().__init__(ticker, cantidad, precio, moneda)

#     def calcular_valor(self):
#         return (self.get_precio() * self.get_cantidad()) / 100

# class Cartera:
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.activos = []

#     def agregar_activo(self, activo):
#         self.activos.append(activo)

#     def valor_total(self):
#         total = 0
#         for activo in self.activos:
#             total += activo.calcular_valor()
#         return total

#     def mostrar_resumen(self):
#         print(f"Cartera: {self.nombre}")
#         for activo in self.activos:
#             print(activo)
#         print(f"Valor total: {self.valor_total()}")
    
#     def __str__(self):
#         resultado = f"Cartera: {self.nombre}\n"
#         for activo in self.activos:
#             resultado += f"{activo}\n"
#         resultado += f"Valor total: {self.valor_total()}"
#         return resultado
        
# class Cliente:
#     def __init__(self, nombre, email):
#         self.nombre = nombre
#         self.email = email
#         self.carteras = []

#     def agregar_cartera(self, cartera):
#         self.carteras.append(cartera)

#     def valor_total_cliente(self):
#         total = 0
#         for cartera in self.carteras:
#             total += cartera.valor_total()
#         return total

#     def __str__(self):
#         return f"Cliente: {self.nombre} | Email: {self.email} | Carteras: {len(self.carteras)}"
    
# a1 = ActivoRentaVariable("AAPL", 10, 180.0, "USD") ### EJEMPLO DE PRUEBA ###
# a2 = ActivoRentaFija("AL30", 100, 58.0, "USD")

# mi_cartera = Cartera("Cartera Principal")
# mi_cartera.agregar_activo(a1)
# mi_cartera.agregar_activo(a2)

# mi_cartera.mostrar_resumen()

# cartera_ahorro = Cartera("Ahorro largo plazo")
# cartera_trading = Cartera("Trading especulativo")

# cartera_ahorro.agregar_activo(a2)       # el bono AL30
# cartera_trading.agregar_activo(a1)      # la acción AAPL

# cartera_ahorro.mostrar_resumen()
# cartera_trading.mostrar_resumen()

# cliente1 = Cliente("Juan Pérez", "juan@mail.com")
# cliente1.agregar_cartera(cartera_ahorro)
# cliente1.agregar_cartera(cartera_trading)

# print(cliente1)
# print(cliente1.valor_total_cliente()) ### FIN EJEMPLO DE PRUEBA ###

# class Exportable:
#     def exportar_txt(self, nombre_archivo):
#         with open(nombre_archivo, "w", encoding="utf-8") as archivo:
#             archivo.write(str(self))
#         print(f"Exportado a {nombre_archivo}")

# class CarteraExportable(Cartera, Exportable):
#     def __init__(self, nombre):
#         super().__init__(nombre)

# cartera_final = CarteraExportable("Cartera para exportar")
# cartera_final.agregar_activo(ActivoRentaVariable("AAPL", 10, 180.0, "USD"))
# cartera_final.agregar_activo(ActivoRentaFija("AL30", 100, 58.0, "USD"))

# cartera_final.mostrar_resumen() ### PRUEBA EXPORTABLE ###
# cartera_final.exportar_txt("cartera.txt")

### MAIN ### 

from utils.validaciones import pedir_numero
from models.activo import ActivoRentaVariable, ActivoRentaFija
from models.cartera import CarteraExportable
from models.cliente import Cliente


cartera = CarteraExportable("Mi Cartera")

while True:
    ticker = input("Ingrese un ticker (o 'salir' para terminar): ")
    if ticker.lower() == "salir":
        break

    tipo = input("Tipo de activo (1: Renta Variable, 2: Renta Fija): ")

    cantidad = pedir_numero(f"Ingrese la cantidad de {ticker}: ")
    precio = pedir_numero(f"Ingrese el precio de {ticker}: ")

    while True:
        moneda = input(f"Ingrese la moneda de {ticker} (ARS/USD): ")
        if moneda in ["ARS", "USD"]:
            break
        else:
            print("Moneda no reconocida. Por favor ingrese 'ARS' o 'USD'.")

    if tipo == "1":
        activo = ActivoRentaVariable(ticker, cantidad, precio, moneda)
    elif tipo == "2":
        activo = ActivoRentaFija(ticker, cantidad, precio, moneda)
    else:
        print("Tipo no reconocido, se cargará como Renta Variable por defecto.")
        activo = ActivoRentaVariable(ticker, cantidad, precio, moneda)

    cartera.agregar_activo(activo)

cartera.mostrar_resumen()

cliente = Cliente("Marcos Arce", "marcos@mail.com")
cliente.agregar_cartera(cartera)
print(cliente)
print(f"Valor total del cliente: {cliente.valor_total_cliente()}")

cartera.exportar_txt("cartera.txt")