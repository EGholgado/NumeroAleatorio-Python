import random
import time

first_decision = 0

def menu_principal():
    print("=====================================================")
    print("  Escribe el número correspondiente a tu decisión:   ")
    print("1: Empezar a jugar")
    print("2: Instrucciones")
    print("0: Salir del juego")
    print("=====================================================")

    first_decision = input("Ingresa el número correspondiente a tu decisión: ")
    while first_decision.isnumeric() == False:
        print("El valor ingresado no es un número")
        first_decision = input("Ingresa el número correspondiente a tu decisión: ")

    while int(first_decision) > 2:
        print("El valor ingresado no esta dentro de los parámetros")
        first_decision = input("Ingresa el número correspondiente a tu decisión: ")

    return first_decision

def instruccion():
    inicio = int(1)
    final = int(10)
    print(
        f"El programa escoge un número al azar entre {inicio} y {final}; también tienes la opción de establecer los límites tú mismo."+"\n"+
        f"Tú tienes como objetivo encontrar el número que la computadora escogio al azar." + "\n")

def menu_instruccion():
    print("=====================================================")
    print("  Escribe el número correspondiente a tu decisión:   ")
    print("1: Empezar a jugar")
    print("2: Regresar al menu")
    print("0: Salir del juego")
    print("=====================================================")

    second_decision = input("Ingresa el número correspondiente a tu decisión: ")
    while second_decision.isnumeric() == False:
        print("El valor ingresado no es un número")
        second_decision = input("Ingresa el número correspondiente a tu decisión: ")

    while int(second_decision) > 2:
        print("El valor ingresado no esta dentro de los parámetros")
        second_decision = input("Ingresa el número correspondiente a tu decisión: ")

    return second_decision

def juego():
    inicio = int(1)
    final = int(10)
    print(" ")
    print(
        f"El juego escoge el número {inicio} como el límite inicial y el número {final} como el límite final para escoger el número aleatorio a adivinar"
        f", si desea cambiar los números correspondientes:" + "\n" +
        "0: Empezar a jugar"+"\n"+
        "1: Cambiar los valores"+"\n")

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

            print(" ")
            print(
                f"El juego escoge el número {inicio} como el límite inicial y el número {final} como el límite final para escoger el número aleatorio a adivinar"
                f", si desea cambiar los números correspondientes:" + "\n" +
                "0: Empezar a jugar" + "\n" +
                "1: Cambiar los valores" + "\n")

        else:
            print("El valor ingresado no es válido, solo ingresar 0 o 1")

    numero = random.randint(inicio, final)
    paso = 0
    adivinado = ""
    while numero != adivinado:
        tiempo_inicio = time.time()
        paso += 1
        adivinado = input(f"Adivina un número entre {inicio} y {final}: ")

        while adivinado.isnumeric() == False:
            print("El valor ingresado no es un número")
            adivinado = input(f"Adivina un número entre {inicio} y {final}: ")

        adivinado = int(adivinado)
        if numero < adivinado:
            print("Este número es muy alto")
        elif numero > adivinado:
            print("Este número es muy pequeño")

    print("¡Felicidades! Adivinaste el número" + "\n")
    tiempo_final = time.time()
    tiempo_transcurrido = tiempo_final - tiempo_inicio
    print(f"El numero adivinado es: {adivinado}")
    print("Tiempo transcurrido: %0.10f segundos." % tiempo_transcurrido)
    print(f"El número de pasos realizados hasta adivinar el número es: {paso}")

first_decision = 0

while True:
    if first_decision == 0:
        print("=====================================================")
        print("               ¡Bienvenido al juego!                 ")
        print("=====================================================")
        first_decision = menu_principal()
    else:
        first_decision = first_decision

    #Salir del juego
    if int(first_decision) == 0:
        print("Fin del juego")
        break

    #Empezar juego
    elif int(first_decision) == 1:
        juego()
        first_decision = 0
        print(" ")

    #Instrucciones
    elif int(first_decision) == 2:
        print(" ")
        instruccion()
        time.sleep(2)
        second_decision = menu_instruccion()

        if int(second_decision) == 1:
            juego()
            first_decision = 0
            print(" ")
        elif int(second_decision) == 2:
            first_decision = 0
        elif int(second_decision) == 0:
            print("Fin del juego")
            break

