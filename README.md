# Financial Portfolio Analyzer

Proyecto final del curso de Python (Coderhouse). Programa de consola que permite cargar activos financieros, agruparlos en una cartera, asociarla a un cliente y exportar un resumen a un archivo de texto.

El proyecto está pensado como base para una futura migración a **Django**, por lo que la organización en paquetes (`models/`, `utils/`) replica intencionalmente las convenciones de ese framework.

## Estructura del proyecto

```
trabajo_final_coder/
│
├── main.py                  # Punto de entrada. Orquesta la carga de datos y el flujo del programa.
│
├── utils/
│   └── validaciones.py      # Funciones de validación de entrada por teclado (pedir_numero).
│
├── models/
│   ├── activo.py             # Clases Activo, ActivoRentaVariable, ActivoRentaFija.
│   ├── cartera.py            # Clases Cartera, Exportable, CarteraExportable.
│   └── cliente.py            # Clase Cliente.
│
├── cartera.txt               # Archivo generado al exportar la cartera (se sobreescribe en cada ejecución).
└── requirements.txt
```

## Cómo ejecutarlo

1. Activar el entorno virtual:
   ```
   .\env\Scripts\activate
   ```
2. Ejecutar el programa:
   ```
   python main.py
   ```
3. Cargar activos ingresando ticker, tipo (Renta Variable / Renta Fija), cantidad, precio y moneda. Escribir `salir` para terminar la carga.
4. Al finalizar, el programa muestra el resumen por consola y genera/actualiza `cartera.txt`.

## Diseño de clases

```
Activo (clase base)
├── ActivoRentaVariable   → hereda de Activo
└── ActivoRentaFija       → hereda de Activo, sobreescribe calcular_valor()

Exportable                → clase independiente, aporta exportar_txt()

Cartera
└── CarteraExportable     → hereda de Cartera y de Exportable (herencia múltiple)

Cliente                   → asociado a una o más Carteras
```

### Activo

Clase base con los datos comunes a cualquier instrumento financiero: `ticker`, `cantidad`, `precio` y `moneda`. Los atributos `cantidad` y `precio` están encapsulados (`__cantidad`, `__precio`) y solo se modifican a través de `set_cantidad()` / `set_precio()`, que validan que el valor sea positivo antes de guardarlo.

- `calcular_valor()`: devuelve `cantidad * precio`.
- `__str__()`: representación legible del activo.

### ActivoRentaVariable

Hereda todo de `Activo` sin modificar ningún comportamiento. Representa acciones u otros instrumentos donde el precio se cotiza por unidad.

### ActivoRentaFija

Hereda de `Activo` pero **sobreescribe `calcular_valor()`**, ya que en Argentina los bonos cotizan cada 100 nominales (por ejemplo, un precio de 58 significa USD 58 cada 100 nominales, no USD 58 por unidad). El cálculo queda `(precio * cantidad) / 100`.

Esta diferencia de comportamiento entre `ActivoRentaVariable` y `ActivoRentaFija` bajo el mismo método `calcular_valor()` es el ejemplo de **polimorfismo** del proyecto: al recorrer una cartera con activos mezclados, cada objeto resuelve su propio cálculo sin necesidad de preguntar de qué tipo es.

### Cartera

Contiene una lista de objetos `Activo` (o subclases). Un activo puede existir de forma independiente a una cartera, por lo que la relación es de **agregación**.

- `agregar_activo(activo)`: agrega un activo ya creado a la lista interna.
- `valor_total()`: suma `calcular_valor()` de todos los activos.
- `mostrar_resumen()`: imprime la cartera por consola.
- `__str__()`: representación completa de la cartera, usada también al exportar.

### Exportable

Clase independiente, sin relación con la jerarquía de `Activo` ni con `Cartera`. Aporta un único método, `exportar_txt(nombre_archivo)`, que escribe `str(self)` en un archivo de texto (codificado en UTF-8).

### CarteraExportable

Hereda simultáneamente de `Cartera` y de `Exportable`, combinando ambos comportamientos sin que ninguna de las dos clases originales dependa de la otra. Es el ejemplo de **herencia múltiple** del proyecto.

### Cliente

Mantiene una lista de carteras asociadas. A diferencia de la relación `Cartera`-`Activo`, una `Cartera` no depende de un `Cliente` para existir ni es "parte" de él — por eso esta relación es de **asociación** y no de agregación.

- `agregar_cartera(cartera)`: vincula una cartera existente al cliente.
- `valor_total_cliente()`: suma `valor_total()` de todas las carteras asociadas.

## Conceptos de POO cubiertos

| Concepto | Dónde se aplica |
|---|---|
| Clase / Atributo / Objeto | `Activo`, `Cartera`, `Cliente`, `Exportable` y sus instancias |
| Constructor (`__init__`) | En todas las clases |
| Instanciación | Creación de objetos en `main.py` (ej: `ActivoRentaFija(...)`) |
| Encapsulamiento | Atributos `__precio` / `__cantidad` en `Activo`, accedidos vía `get_/set_` |
| Herencia | `ActivoRentaVariable` y `ActivoRentaFija` heredan de `Activo` |
| Herencia múltiple | `CarteraExportable` hereda de `Cartera` y `Exportable` |
| Polimorfismo | `calcular_valor()` se comporta distinto en renta variable vs. renta fija |
| Agregación | `Cartera` contiene una lista de `Activo` |
| Asociación | `Cliente` está vinculado a `Cartera` sin contenerla |

## Validaciones

`utils/validaciones.py` centraliza la función `pedir_numero(mensaje, permitir_negativos=False)`, que valida por consola que el dato ingresado sea numérico (`ValueError`) y que cumpla la regla de negocio correspondiente (no acepta valores menores o iguales a cero, salvo que se indique explícitamente `permitir_negativos=True`).

La carga de moneda (`ARS` / `USD`) se valida con su propio bucle en `main.py`, rechazando cualquier valor fuera de esas dos opciones.

## Próximos pasos

La organización actual en `models/` y `utils/` está pensada para facilitar la migración a Django: las clases de `models/` se convertirían en modelos de Django (`models.Model`), reutilizando gran parte de la lógica y validaciones ya definidas.
