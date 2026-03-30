# utils.py

def limpiar_y_tokenizar(texto):
    """
    Limpia el texto convirtiéndolo a minúsculas y eliminando ruido básico.
    Devuelve una lista de palabras (tokens).
    """
    # Paso 1: Convertir a minúsculas con .lower()
    
    text_min = texto.lower()
        
    # Paso 2: Reemplazos . con espacio y , con espacio usando .replace() (puedes añadir más si es necesario)
    
    text_esp = text_min.replace("."," ").replace(","," ")
    
    # Paso 3: Dividir en palabras usando .split()
    
    palabras = text_esp.split()
    
    # Devuelve la lista de palabras
    return palabras