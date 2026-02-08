# Practicando lógica booleana en Python aprendiendo a usar "and", "or" y "not"

# Declaracion de valores o inicialización de Valores para probar diferentes combinaciones
edad = 16
tiene_permiso = True
es_finde = False

# TODO 1: Usa una expresión booleana con "and"
# Por ejemplo: ¿Puede salir hoy solo si tiene 18 años o más Y si tiene permiso?
print("***Uso de AND***")
if edad >= 18 and tiene_permiso == True:
    print("puede salir")
else:
    print("No puede salir")

# TODO 2: Usa una expresión booleana con "or" para permitir salir si es fin de semana o tiene permiso
print("***Uso de OR***")
if es_finde == True >= 18 or tiene_permiso == True:
    print("puede salir")
else:
    print("No puede salir")


# TODO 3: Usa una expresión booleana con "not" para negar una condición
# Por ejemplo: De ninguna manera tiene permiso

print("***Uso de NOT***")
if not edad >= 18 and not tiene_permiso == True:
    print("puede salir")
else:
    print("No puede salir")

# TODO 5: Escribe tu propia condición con and, or o not e imprimelo a la pantalla.
# Ejemplo: ¿Puede conducir si tiene 18 o más y tiene permiso? u cualquier otra idea. 

print("*** EJEMPLO PROPIO ***")
if edad >= 18 and tiene_permiso == True:
    print("puede conducir")
else:
    print("No puede conducir")



