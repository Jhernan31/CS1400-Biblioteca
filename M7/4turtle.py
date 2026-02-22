# ================================
# Proyecto: Dibujar una tarta con Turtle
# ================================
# En este ejercicio vas a:
# 1. Usar trigonometría para calcular la base de un triángulo isósceles.
# 2. Dibujar un triángulo con turtle.
# 3. Repetir el triángulo varias veces para formar una "tarta".
#
# ¡Lee cada paso con atención y completa los TODO!

# Importaciones necesarias
import math

import turtle
turtle.setup(width=400, height=400) 
ventana = turtle.Screen()
# from turtle import make_turtle, forward, left, right, penup, pendown

def triangulo(longitud, angulo):
    t = turtle.Turtle()

    """
    TODO Paso 1:
    Escribe aquí qué hace esta función.
    Esta funcion tiene como objetivo crear un triangulo cuando es invocada
    la longitud y el angulo son pasados como parametrosx

    Pista:
    - ¿Qué representa 'longitud'?
    - ¿Qué representa 'angulo'?
    - ¿Qué debería dibujar esta función?
    """
    
    # --------------------------------
    # Paso 2: Cálculos matemáticos
    # --------------------------------
    
    # Convierte el ángulo a radianes para poder usar funciones trigonométricas.
    angulo_rad = math.radians(angulo)
    
    # TODO:
    # Calcula la longitud de la base del triángulo isósceles.
    # Pista: estás trabajando con dos lados iguales (longitud)
    # y el ángulo central entre ellos.
    # Puedes usar math.sin().
    base =  2 * longitud * math.sin(angulo_rad/2) # Escribe aquí el cálculo
    
    # TODO:
    # Calcula el ángulo que debe girar la tortuga en las esquinas
    # para que el triángulo se cierre correctamente.
    # Escribe aquí el cálculo
    
    t.forward(base + base * 0.35)
    t.left(180 - 70)
    t.forward(base * 2)
    t.left(180 - 40)
    t.forward(base * 2)
    t.left(180 - 70)
    t.forward(base + base * 0.35)
    
    # --------------------------------
    # Paso 3: Dibujo del triángulo
    # --------------------------------
    
    # Dibuja el triángulo usando forward() y left().
    # Recuerda:
    # - Debes dibujar dos lados iguales (longitud).
    # - Debes dibujar la base.
    # - La tortuga debe volver al punto inicial.
    
    # TODO:
    # Escribe aquí los movimientos necesarios.

        

    # pass  # ⚠️ Borra esta línea cuando completes el código



def dibujar_tarta(n_porciones, longitud):
    """
    TODO:
    Explica qué hace esta función.
    
    Pista:
    - ¿Qué es n_porciones?
        Es el numero de porciones de la tarta
    - ¿Qué representa longitud?
        El largo de cada porcion
    """
    
    # --------------------------------
    # Paso 4: Calcular el ángulo de cada porción
    # --------------------------------
    
    # TODO:
    # Calcula el ángulo central de cada porción.
    # Pista: un círculo completo tiene 360 grados.
    angulo_porcion =  n_porciones / 360 # Divide 360 entre el número de porciones
    
    # --------------------------------
    # Paso 5: Dibujar todas las porciones
    # --------------------------------
    
    # TODO:
    # Escribe un bucle for que:
    # 1. Llame a la función triangulo(...)
    # 2. Gire la tortuga el ángulo necesario
    #    para dibujar la siguiente porción.
    
    for porciones in range(n_porciones):
        triangulo(longitud, angulo_porcion)
        
        


    #pass  # ⚠️ Borra esta línea cuando completes el código



# ==================================
# Bloque para probar la función
# ==================================

# make_turtle(height=400, width=600)

# ----------------------------------
# Prueba 1
# ----------------------------------

#print("Dibujando una tarta de 5 porciones...")
#dibujar_tarta(8, 60 )
#triangulo(50, 100)
# ----------------------------------
# TODO EXTRA
# ----------------------------------
# 1. Levanta el lápiz (penup()).
# 2. Muévete a otra posición.
# 3. Baja el lápiz (pendown()).
# 4. Dibuja otra tarta con diferentes valores.


# ----------------------------------
# Prueba 2
# ----------------------------------

#print("Dibujando una tarta de 8 porciones...")
#dibujar_tarta(8, 60)


ventana.exitonclick()