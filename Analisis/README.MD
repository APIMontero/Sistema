# Análisis

Se pide crear un sistema que ingresado Nombre y apellido, el cargo dell trabajador y su sueldo bruto, calcule los descuentos y el sueldo liquido. Este sistema debera ser capaz de imprimir todos los trabajadores por pantalla. También se pide que imprima a archivo de texto plano por cargo y por todos los trabajadores la palnilla de sueldos de los mismos. Para ello, ofrecerá un menu con las opciones explicadas anteriormente. Los datos de entrada deben estar validados correctamente antes de ser usados. El editor a usar será VSCode.

## Funcionalidades Pedidas

### 1. Registrar Trabajador 

Datos Entrada

    - nombre y apellidos
    - Cargo
    - Sueldo Bruto
Tareas
1. Calcular los siguientes Valores
   
   - Descuento Salud por 7 %
   - Descuento AFP por 12%
   - Liquido A pagar <- Sueldo Bruto - Descuentos

2. Validar Datos Ingresados

   - Nombre: Nombre y apellido
   - Cargo: CEO o Desarrollador o Analista de datos
   - Sueldo Bruto: Datos de tipo entero, sin punto decimal.

3. Listar Todos Los Trabajadores

    Listar cada trabajador de la colección.

4. Imprimir Planilla De Sueldos
    1. Todos los trabajadores.
    2. Por cargo especificado por usuario.
    3. Debe ser impreso a archivo de texto, opciones a usar:
        1. texto Plano -> txt
        2. separado por comas -> csv
        3. JSON -> json

5. Salir del programa
    salir de la aplicación.

## Requisitos

1. Opciones deben ser desarrolladas con funciones en lenguaje python.
2. Estar funciones deberán ser llamada de un programa principal.
3. El programa funcionará hasta que el usuario decida finalizar el programa.
4. Subir la carpeta completa a github.
5. Compartir Vinculo del repositorio.

## Proceso

### Estructura de archivos

Crear carpeta contenedora del proyecto con los archivos pedidos.
    1. principal.py
        Crear menu y llamar las funciones.
    2. metodos.py
        Funciones propias para manejar las colecciones y otros propósitos.
    3. modelo.py
        Estructura de datos para uso en memoria.

### Creacion del código para cada archivo, funcion principal y funciones de apoyo

El código estará disponible en los archivos antes mencionados.

### Test

Se realizarán  los siguientes test:

1. Unitario: cada funcion y archivo será probada por separado.

2. de caja negra: Sistema completo se testeará a fin de saber si las entradas y salidas son las correctas.

3. formato de entradas y salidas de datos.
4. De integración: se probarán todos los componentes como uno solo.

### Administración de Versionado

El proyecto se generará con git en modo local, para luego ser subido a la nuve usando github.com en la cuenta personal del creador de este sistema.

    Producido por:

    David Erwin Montero Urrutia.
    Ingeniero Informatico DUOC UC, Chile.
    Analista de sistemas, Jhon F. Kennedy, Chile
    david.montero.urrutia@gmail.com
    +56974809847
    https://github.com/APIMontero
