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

## Gestión de Usuarios y Seguridad
El sistema implementa un mecanismo de autenticación segura utilizando la base de datos SQLite para persistir la información de los usuarios. 

### Método de Hashing:
Para garantizar la integridad y seguridad de las contraseñas, se utiliza el algoritmo de cifrado **SHA-256** (Secure Hash Algorithm 256-bit). Este método es implementado mediante la librería estándar `hashlib` de Python. 

* **Proceso:** La contraseña ingresada por el usuario es convertida a un hash irreversible antes de ser guardada en la base de datos, evitando así el almacenamiento de credenciales en texto plano.



## Módulo de Automatización NETCONF
Este módulo permite la gestión programática del router CSR1000v utilizando el protocolo NETCONF.

### Prerrequisitos
* **Puerto:** TCP 830 (Debe estar habilitado en el router).
* **Librerías:** `ncclient` (Instalar con `pip install ncclient`).
* **Variables de entorno/configuración:**
    * `host`: IP del router (ej. 192.168.142.10).
    * `username`: Usuario con privilegios de gestión.
    * `password`: Credenciales de acceso.

### Ejecución
El script `netconf_check.py` realiza la conexión, autenticación y solicita al dispositivo la lista de *capabilities* soportadas.



## Ítem 6: Gestión vía API RESTCONF
Este módulo documenta la configuración del router CSR1000v mediante llamadas API desde Postman usando formato JSON.

* **Operación Loopback:** Se creó la interfaz Loopback 22 mediante el método `PUT`, asignando la IP 22.22.22.22 y dejándola administrativamente apagada.
* **Consulta de Interfaces:** Se utilizó el método `GET` hacia el modelo de datos `ietf-interfaces` para extraer la lista de interfaces en formato JSON y validar su estado.
* **Validación Física/Virtual:** Se confirmó mediante el comando `show ip interface brief` en la consola del router que la configuración enviada por la API se aplicó correctamente.
