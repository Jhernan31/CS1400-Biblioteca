"""
Este programa debe darle al usuario la opción de elegir una comida de una lista.
El código asegura que lo ingresado sea legible (en minúsculas) y lo compara con una lista usando lógica if/else.
Al final, muestra un mensaje explicando de dónde es originaria esa comida.
"""
# TODO #1:
# Imprime un mensaje de bienvenida al programa de comidas de Latinoamérica.
print("Bienvenido al programa de comidas de Latinoamerica")
# TODO #2:
# Muestra al usuario una lista de al menos 5 opciones de comidas para elegir.
print("Elija uno de los menus disponibles:")
print("Opcion 1 : Tacos")
print("Opcion 2 : Arepas")
print("Opcion 3 : Ceviche")
print("Opcion 4 : Churrasco")
print("Opcion 5 : Pupusas")
# TODO #3:
# Guarda lo que el usuario escribió en una variable llamada `comida`.
comida = input("Escriba su menu elegido: ")
# TODO #4:
# Convierte lo ingresado a minúsculas para asegurar la comparación correcta.
comida_minuscula = comida.lower()
# TODO #5:
# Usa una estructura if / elif / else para verificar la comida elegida.
# Imprime un mensaje con el país de origen para cada comida.

if comida_minuscula == "tacos":
   print("Los tacos son tipicos de Mexico")
elif comida_minuscula == "arepas":
    print("Las arepas son tipicas de Venezuela y Colombia")
elif comida_minuscula == "ceviche":
    print("El ceviche es tipico del Peru")
elif comida_minuscula == "churrasco":
    print("El Asado/Churrasco es muy tipico de Argentina")
elif comida_minuscula == "pupusas":
    print("Las Pupusas son la comida tipica de El Salvador")
else:
    print("Opcion no valida")
## Ejemplo de salida esperada:


"""
Bienvenido al programa de comidas de Latinoamérica.
Opciones: tacos, arepas, ceviche, pupusas, empanadas
¿Qué comida quieres conocer? Tacos
Los tacos son típicos de México.
"""