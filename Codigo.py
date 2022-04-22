import random
import time

print("=========================================")
print("          ¡Bienvenido al juego!          ")
print("=========================================")

print("El objetivo del juego es adivinar cual es el número"+"\n")

inicio = int(1)
final = int(10)

print(f"El juego escoge el número {inicio} como el límite inicial y el número {final} como el límite final para escoger el número aleatorio a adivinar"
          f", si desea cambiar los números correspondientes:"+"\n"+"Pulsar el número 0 para empezar a jugar"+"\n"+"Pulsar el valor 1 para cambiar los valores."+"\n")

while True:
    clave = input("Ingresa el número correspondiente a tu decisión: ")

    while clave.isnumeric() == False:
        print("El valor ingresado no es un número")
        clave = input("Ingresa el número correspondiente a tu decisión: ")

    clave = int(clave)
    if clave == 0:
        clave = int(clave)
        print("¡Empecemos a jugar!")
        break

    elif clave == 1:
        inicio = input("Ingresa el valor de inicio: ")

        while inicio.isnumeric() == False:
            print("El valor ingresado no es un número positivo")
            inicio = input("Ingresa el valor de inicio: ")

        inicio = int(inicio)

        final = input("Ingresa el valor final: ")

        while final.isnumeric() == False:
            print("El valor ingresado no es un número positivo")
            final = input("Ingresa el valor final: ")

        final = int(final)

        print(f"El juego escoge el número {inicio} como el límite inicial y el número {final} como el límite final para escoger el número aleatorio a adivinar"
            f", si desea cambiar los números correspondientes:" + "\n" + "Pulsar el número 0 para empezar a jugar" + "\n" + "Pulsar el valor 1 para cambiar los valores." + "\n")

    else:
        print("El valor ingresado no es válido, solo ingresar 0 o 1")



numero = random.randint(inicio,final)
print(numero)
adivinado = 0


while numero != adivinado:
    tiempo_inicio=time.time()
    adivinado = input(f"Adivina un número entre {inicio} y {final}: ")

    while adivinado.isnumeric() == False:
        print("El valor ingresado no es un número")
        adivinado = input(f"Adivina un número entre {inicio} y {final}: ")

    adivinado = int(adivinado)
    if numero < adivinado:
        print("Este número es muy alto")
    elif numero > adivinado:
        print("Este número es muy pequeño")

print("¡Felicidades! Adivinaste el número"+"\n")
tiempo_final= time.time()
tiempo_transcurrido=tiempo_final - tiempo_inicio
print("Tiempo transcurrido: %0.10f segundos." % tiempo_transcurrido)
