import requests
import urllib.parse
import os
def cargar_env():
    try:
        with open('.env', 'r') as file:
            for linea in file:
                if linea.strip() and not linea.startswith('#'):
                    clave, valor = linea.strip().split('=', 1)
                    os.environ[clave] = valor
    except FileNotFoundError:
        print("Error: Archivo .env no encontrado. Asegúrese de crearlo.")

cargar_env()
API_KEY = os.environ.get('GRAPHHOPPER_API_KEY')

GEOCODE_URL = "https://graphhopper.com/api/1/geocode"
ROUTE_URL = "https://graphhopper.com/api/1/route"

def obtener_coordenadas(ciudad):
    url = f"{GEOCODE_URL}?q={urllib.parse.quote(ciudad)}&key={API_KEY}"
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            if datos["hits"]:
                lat = datos["hits"][0]["lat"]
                lng = datos["hits"][0]["lng"]
                return lat, lng
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    print(f"No se pudieron obtener las coordenadas para: {ciudad}")
    return None

def principal():
    if not API_KEY or API_KEY == "tu_clave_api_aqui":
        print("Error: Debe configurar una API Key válida en el archivo .env.")
        return

    while True:
        print("\n--- Calculadora de Rutas Chile-Argentina ---")
        origen = input("Ingrese la Ciudad de Origen (o 's' para salir): ")
        if origen.lower() == 's':
            print("Saliendo del programa...")
            break
        
        destino = input("Ingrese la Ciudad de Destino (o 's' para salir): ")
        if destino.lower() == 's':
            print("Saliendo del programa...")
            break
        
        print("Tipos de transporte disponibles: car (auto), bike (bicicleta), foot (a pie)")
        transporte = input("Elija el tipo de medio de transporte a utilizar: ").lower()
        
        if transporte not in ['car', 'bike', 'foot']:
            print("Medio de transporte no válido. Se utilizará 'car' por defecto.")
            transporte = 'car'

        coord_origen = obtener_coordenadas(origen)
        coord_destino = obtener_coordenadas(destino)

        if coord_origen and coord_destino:
            url_ruta = (f"{ROUTE_URL}?point={coord_origen[0]},{coord_origen[1]}"
                        f"&point={coord_destino[0]},{coord_destino[1]}"
                        f"&vehicle={transporte}&locale=es&calc_points=true&instructions=true&key={API_KEY}")
            
            try:
                respuesta_ruta = requests.get(url_ruta)
                if respuesta_ruta.status_code == 200:
                    datos_ruta = respuesta_ruta.json()
                    camino = datos_ruta["paths"][0]
                    
                    distancia_km = camino["distance"] / 1000
                    distancia_mi = distancia_km * 0.621371
                    tiempo_ms = camino["time"]
                    
                    # Formatear el tiempo de ms a horas, minutos y segundos
                    segundos = int((tiempo_ms / 1000) % 60)
                    minutos = int((tiempo_ms / (1000 * 60)) % 60)
                    horas = int((tiempo_ms / (1000 * 60 * 60)) % 24)
                    
                    print("\n=== RESUMEN DEL VIAJE ===")
                    print(f"De: {origen} -> A: {destino}")
                    print(f"Medio de transporte: {transporte}")
                    print(f"Distancia: {distancia_km:.2f} km / {distancia_mi:.2f} millas")
                    print(f"Duración estimada: {horas:02d}:{minutos:02d}:{segundos:02d}")
                    
                    print("\n=== NARRATIVA DEL VIAJE ===")
                    for instruccion in camino["instructions"]:
                        dist_instruccion = instruccion['distance'] / 1000
                        print(f"- {instruccion['text']} ({dist_instruccion:.2f} km)")
                    
                else:
                    print(f"Error al calcular la ruta. Código HTTP: {respuesta_ruta.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error al consultar la ruta: {e}")
        else:
            print("Verifique los nombres de las ciudades e intente nuevamente.")

if __name__ == "__main__":
    principal()
