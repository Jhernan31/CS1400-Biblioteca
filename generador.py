# programa generador de contraseñas
import random

long_pass = int(input("ingrese la longitud de su password: "))
opciones = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z","0","1","2","3","4","5","6","7","8","9"]
password = ""
for i in range(long_pass):
    password += random.choice(opciones)

print(f"Su password es : {password}")