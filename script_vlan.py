def verificar_vlan():
    try:
        vlan = int(input("Ingrese el número de la VLAN: "))
        
        if 1 <= vlan <= 1005:
            print(f"La VLAN {vlan} corresponde a una VLAN del rango normal.")
        elif 1006 <= vlan <= 4094:
            print(f"La VLAN {vlan} corresponde a una VLAN del rango extendido.")
        else:
            print("El número ingresado está fuera de los rangos válidos de VLAN (1-4094).")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    verificar_vlan()
