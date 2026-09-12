def pedir_numero(mensaje, permitir_negativos=False):
    while True:
        try:
            num = float(input(mensaje))
            if not permitir_negativos and num <= 0:
                print("Error: El número debe ser positivo.")
            else:
                return num
        except ValueError:
            print("Error: Debe ingresar un número válido.")