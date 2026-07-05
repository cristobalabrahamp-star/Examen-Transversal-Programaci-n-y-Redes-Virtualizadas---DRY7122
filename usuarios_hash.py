import sqlite3
import hashlib
from flask import Flask

app = Flask(__name__)

# Función para encriptar la contraseña en formato SHA-256
def crear_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def configurar_base_datos():
    # Conectar a la base de datos (se creará el archivo si no existe)
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    
    # Crear la tabla solicitada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    
    # Limpiar la tabla por si ejecutamos el script varias veces
    cursor.execute('DELETE FROM usuarios')
    
    # Lista de integrantes y contraseñas a elección
    integrantes = [
        ("Cristobal Villagra", "cisco123"),
        ("Companero Dos", "redes456"),
        ("Companero Tres", "admin789")
    ]
    
    # Insertar los usuarios con la contraseña ya convertida a hash
    for usuario, password in integrantes:
        hash_pw = crear_hash(password)
        cursor.execute('INSERT INTO usuarios (usuario, password_hash) VALUES (?, ?)', (usuario, hash_pw))
        print(f"Usuario {usuario} registrado con hash exitosamente.")
        
    conexion.commit()
    conexion.close()
    print("\nBase de datos 'usuarios.db' generada correctamente.")

# Configurar el sitio web solicitado
@app.route('/')
def inicio():
    return "<h1>Examen Transversal DRY7122</h1><p>Servidor web y base de datos corriendo correctamente.</p>"

if __name__ == '__main__':
    print("--- Configurando Base de Datos SQLite ---")
    configurar_base_datos()
    
    print("\n--- Iniciando Sitio Web ---")
    print("El sitio web estara disponible en http://127.0.0.1:5800")
    # Iniciar el servidor en el puerto 5800 como pide el requerimiento
    app.run(host='0.0.0.0', port=5800)
