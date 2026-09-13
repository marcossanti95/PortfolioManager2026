# Portfolio Analyzer

Proyecto final del curso de Python (Coderhouse). Aplicación web desarrollada con **Django** que permite a un usuario registrarse, crear carteras de inversión y cargar activos financieros (renta variable y renta fija), calculando automáticamente el valor de cada uno y el valor total de la cartera.

El proyecto nació como un ejercicio de consola en Python puro, aplicando Programación Orientada a Objetos (clases, herencia, herencia múltiple, polimorfismo, encapsulamiento, agregación y asociación), y fue migrado a Django reutilizando esa misma lógica de negocio como base de los modelos.

**🔗 URL pública:** https://arcemarcos95.pythonanywhere.com

## Descripción del proyecto

- **Propósito:** ofrecer una herramienta simple para registrar y calcular el valor de una cartera de inversión compuesta por distintos tipos de activos.
- **Problema que resuelve:** llevar el control manual de una cartera (en Excel u otro medio) es propenso a errores, sobre todo al mezclar instrumentos con distinta lógica de valuación (por ejemplo, acciones vs. bonos, donde estos últimos cotizan cada 100 nominales en Argentina).
- **Funcionalidades principales:** registro y login de usuarios, creación de múltiples carteras por usuario, carga de activos de renta variable y renta fija con validación de datos, cálculo automático del valor de cada activo y del total de la cartera, panel de administración para gestión completa de los datos.
- **Usuario objetivo:** cualquier persona que quiera llevar un registro simple y ordenado de su cartera de inversión, sin necesidad de planillas de cálculo.

## Estructura del proyecto

```
trabajo_final_coder/
│
├── manage.py                 # Punto de entrada de Django
├── config/                   # Configuración del proyecto (settings, urls)
├── portfolio/                 # App principal
│   ├── models.py              # Perfil, Cartera, Activo, ActivoRentaVariable, ActivoRentaFija
│   ├── views.py                # Registro, dashboard, alta de carteras y activos
│   ├── forms.py                # Formularios con validación
│   ├── admin.py                # Registro de modelos en el panel admin
│   └── urls.py
├── templates/                 # Templates HTML (Bootstrap)
│
├── main.py                    # Versión previa en Python puro (POO), sin Django
├── models/                    # Clases originales: Activo, Cartera, Cliente
├── utils/                      # Validaciones reutilizadas en el proyecto Django
│
├── requirements.txt
└── README.md
```

## Funcionalidades principales

### Panel de administración
Acceso completo a los cuatro modelos del proyecto (Perfiles, Carteras, Activos de renta variable y renta fija) para gestión y auditoría de datos. Disponible en `/admin/`.

### Registro y autenticación de usuarios
Cualquier persona puede crear una cuenta desde `/registro/`. Al registrarse, se crea automáticamente un `Perfil` asociado. El sistema de login/logout usa la autenticación estándar de Django.

### Dashboard y carteras
Cada usuario ve únicamente sus propias carteras. Desde el dashboard puede crear nuevas carteras y acceder al detalle de cada una.

### Carga de activos con validación
Dentro de cada cartera se pueden agregar activos de dos tipos:
- **Renta Variable:** el valor se calcula como `cantidad × precio`.
- **Renta Fija:** el valor se calcula como `(cantidad × precio) / 100`, replicando la convención argentina de cotización de bonos cada 100 nominales.

Los formularios validan que cantidad y precio sean valores positivos, rechazando datos inválidos con un mensaje de error claro.

## Diseño de clases (heredado del proyecto de POO)

```
Activo (clase abstracta)
├── ActivoRentaVariable
└── ActivoRentaFija       → sobreescribe calcular_valor() (polimorfismo)

Cartera
└── contiene Activos (agregación)

Perfil (extiende User de Django)
└── asociado a Carteras (asociación)
```

| Concepto de POO | Dónde se aplica |
|---|---|
| Clase / Atributo / Objeto | Modelos de `portfolio/models.py` |
| Herencia | `ActivoRentaVariable` y `ActivoRentaFija` heredan de `Activo` |
| Polimorfismo | `calcular_valor()` se comporta distinto según el tipo de activo |
| Encapsulamiento | Validadores en los campos del modelo (`MinValueValidator`) |
| Agregación | `Cartera` contiene una lista de `Activo` |
| Asociación | `Perfil` vinculado a `Cartera` |

*(La versión original en Python puro, con herencia múltiple explícita mediante una clase `Exportable`, se conserva en `main.py`, `models/` y `utils/` como referencia del proceso de aprendizaje previo a la migración a Django.)*

## Cómo ejecutar el proyecto localmente

**Requisitos previos:** Python 3.10 o superior.

1. Cloná el repositorio:
   ```
   git clone https://github.com/marcossanti95/PortfolioManager2026.git
   cd PortfolioManager2026
   ```

2. Creá y activá un entorno virtual:
   ```
   python -m venv env
   .\env\Scripts\activate      # Windows
   source env/bin/activate     # Linux/Mac
   ```

3. Instalá las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Aplicá las migraciones:
   ```
   python manage.py migrate
   ```

5. Creá un superusuario (opcional, para acceder al panel admin):
   ```
   python manage.py createsuperuser
   ```

6. Ejecutá el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

7. Abrí en el navegador:
   ```
   http://127.0.0.1:8000/
   ```

## Despliegue

La aplicación está desplegada en **PythonAnywhere** (plan gratuito), corriendo con Python 3.12 sobre un entorno virtual dedicado. El proyecto se despliega clonando el repositorio directamente desde GitHub, configurando el entorno virtual, aplicando migraciones y sirviendo los archivos estáticos mediante `collectstatic`.

**URL pública:** https://arcemarcos95.pythonanywhere.com

## Capturas de pantalla

*(Agregar aquí las capturas: panel de administración, pantalla de login, registro de usuario, dashboard con carteras, formulario de carga de activo, detalle de cartera con valores calculados.)*