# --- Diaro de      Digital ---
print("\n" * 2)
from datetime import datetime, date, timedelta
import json 
import os

diario = {}


# Aqui tu funcion menu()
def ver_menu():
    print(" 1. Escribir \n 2. Leer \n 3. Salir")


while True:
  try:
    ver_menu()
    eleccion = int(input("Seleccion: "))
    # Aqui tu if/elif/elif/else statement con las opciones del menu
    if eleccion == 1:
        d_entrada = input("Entrada de hoy:")
        d_fecha = datetime.now()
        f_fecha = d_fecha.strftime("%d/%m/%Y %H:%M:%S")
        dia = {"fecha": f_fecha, "entrada": d_entrada}
        with open("diario.json", "w") as f:
            json.dump(dia, f, indent=4)
    elif eleccion == 2:
        b_fecha = input("Cual fecha deseas leer: dd/mm/yyyy: ")
        bf_fecha = datetime.strptime(b_fecha, "%d/%m/%Y")
        with open("diario.json", "r") as f:
            vista = json.load(f)
            # t_vista = diario[bf_fecha]
            print(f"fecha: {vista['fecha']}")
            print(f"Entrada: {vista['entrada']}")
    elif eleccion == 3:
      print("Hasta pronto...")
      break
    else:
        print("Opcion invalida, elige 1,2 o 3...intentelo de nuevo")
  except FileNotFoundError:
    print("Parece que ha habido un error, intentalo de nuevo...")
  except ValueError:
      print("Opcion invalida, ingrese solo numeros enteros, intentelo de nuevo...")
  
    
      
    
        
    # Entrada de datos
    # Guardar en archivo
    # Leer el archivo

    # Salir de tu ultimo elif con un break
    # else solo para mostrar al usuario que no funciono lo que intentaron ingresar.
