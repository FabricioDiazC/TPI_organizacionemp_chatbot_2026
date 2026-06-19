# Chatbot de Gestión de Solicitud de Vacaciones
Trabajo Práctico Integrador — Organización Empresarial — UTN

## Descripción
El presente proyecto consiste en una simulación mediante consola de un chatbot diseñado para automatizar el proceso de solicitud de vacaciones de los empleados. La arquitectura del sistema utiliza una máquina de estados para gestionar el flujo de la interacción y emplea persistencia de datos a través de archivos CSV, simulando el comportamiento de una base de datos.

## Estructura del repositorio
```text
.
├── README.md
├── TPI_organizacionemp_chatbot.py
├── empleados.csv (se genera automáticamente si no existe)
└── solicitudes.csv (se genera automáticamente si no existe)
```

## Cómo ejecutarlo
1. Clonar el repositorio en su entorno local ejecutando: `git clone <URL_DEL_REPOSITORIO>`
2. Ingresar a la carpeta del proyecto.
3. Ejecutar el script principal con el comando: `python TPI_organizacionemp_chatbot.py`

Al iniciar, el programa crea automáticamente el archivo `empleados.csv` (incluyendo tres empleados de ejemplo) y el archivo `solicitudes.csv` (vacío) en caso de que no existan en el sistema. Por lo tanto, no es necesario crearlos manualmente para poder probar el funcionamiento del bot.

## Datos de prueba(empleados.csv)

| legajo | nombre | dias_disponibles |
| :--- | :--- | :--- |
| 1001 | Juan Perez | 14 |
| 1002 | Ana Gomez | 5 |
| 1003 | Carlos Diaz | 21 |

## Recomendaciones para probar el programa
1. Ingresar un legajo válido (ej. 1001).
2. Pedir una cantidad de días dentro del saldo disponible (ej. 3) y comprobar la correcta aprobación de la solicitud.
3. Volver a ejecutar el script y probar ingresando un legajo inexistente o utilizando letras para verificar el manejo de errores y validaciones del sistema.
4. Probar solicitar una cantidad de días superior al saldo disponible (ej. con el legajo 1002, pedir 10 días) para evaluar la lógica de rechazo.
