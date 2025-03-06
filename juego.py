# https://colab.research.google.com/drive/1yXuITtdhc4HEFnYMW92fpmewRNLc6NZO?usp=sharing
import random
top=50
while True:
  try:
    diff = int(input("Selecciona un nivel de dificultad (1/2):\nFácil\t(1)\nDifícil\t(2)\n"))
    if diff != 1 and diff != 2:
      raise ValueError("Por favor, elige entre (1) y (2)")
    else:
      if diff == 1:
        top=50
      if diff == 2:
        top=100
      break
  except ValueError as e:
    print(f"Error: {e}")

# Almacenamos la informacion en un diccionario
juego = {
    'numero_secreto': random.randrange(1, top),
    'intentos': [],
    'nIntentos': 0,
    'jugador': input("Ingresa tu nombre: ")  # Agregando nombre del jugador
}

intentos=10
# Bucle principal del juego con manejo de errores
while True:
    try:
        if intentos == 0:  # Verificación de intentos restantes
            print("¡Perdiste!, trata de adivinar en menos de 10 intentos :c")
            print(f"El número secreto era: {juego['numero_secreto']}")
            break  # Salir del bucle si se acaban los intentos
        numero = int(input(f"Dime un numero entre 1 y {top}: "))
        if not 1 <= numero <= top+1:
            raise ValueError(f"El número debe estar entre 1 y {top}: ")

        juego['intentos'].append(numero)
        juego['nIntentos'] += 1
        intentos-=1

        if numero > juego['numero_secreto']:
            print(f"El numero secreto es menor, te quedan {intentos} intentos")
        elif numero < juego['numero_secreto']:
            print(f"El numero secreto es mayor, te quedan {intentos} intentos")
        else:
            print(f"¡{juego['jugador']}! Adivinaste el número secreto ({juego['numero_secreto']}) en {juego['nIntentos']} intentos.")
            print("Tus intentos fueron:", juego['intentos'])
            break  # Salir del bucle si se adivina el número

    except ValueError as e:
        print(f"Error: {e}")