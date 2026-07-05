# Examen Transversal - Programación y Redes Virtualizadas (DRY7122)

Este repositorio contiene los scripts desarrollados para el Examen Transversal, demostrando la integración de Python con APIs externas, bases de datos SQLite y servidores web básicos.

## Objetivo de cada módulo

1. **`script_vlan.py`**: Evalúa si una VLAN ingresada pertenece al rango normal o extendido según los estándares de Cisco.
2. **`ruta_graphhopper.py`**: Se conecta a la API de GraphHopper para calcular la distancia (en km y millas), tiempo y la narrativa de ruta paso a paso entre dos ciudades.
3. **`usuarios_hash.py`**: Genera una base de datos SQLite (`usuarios.db`) para almacenar contraseñas encriptadas en formato SHA-256 y levanta un servidor web en el puerto 5800.

## Dependencias requeridas
* Python 3.8+
* Librería requests
* Librería Flask

## Ejecución
Cada script se puede ejecutar de forma independiente desde la terminal:
* Verificador de VLAN: python3 script_vlan.py
* Calculadora de rutas: python3 ruta_graphhopper.py
* Base de datos y Servidor Web: python3 usuarios_hash.py

* 
## Módulo de Geolocalización (ruta_graphhopper.py)
Este script permite calcular la ruta entre dos puntos geográficos (Santiago y Mendoza por defecto) consumiendo el endpoint `/route` de la API de GraphHopper.

### Configuración:
1. Crea un archivo `.env` en la raíz del proyecto.
2. Agrega tu clave: `GRAPHOPPER_API_KEY=tu_clave_aqui`.
3. Instala las dependencias: `pip install requests python-dotenv`.

### Ejecución:
Ejecuta el script con el comando: `python3 ruta_graphhopper.py`
