import random

print("===========================")
print("   ¡Bienvenido al juego!   ")
print("===========================")

print("El objetivo del juego es adivinar cual es el número"+"\n")

inicio = int(1)
final = int(10)

numero = random.randint(inicio,final)
print(numero)
adivinado = 0


while numero != adivinado:
    adivinado = input(f"Adivina un número entre {inicio} y {final}: ")

    while adivinado.isnumeric() == False:
        print("El valor ingresado no es un número")
        adivinado = input(f"Adivina un número entre {inicio} y {final}: ")

    adivinado = int(adivinado)
    if numero < adivinado:
        print("Este número es muy alto")
    elif numero > adivinado:
        print("Este número es muy pequeño")

print("¡Felicidades! Adivinaste el número")
