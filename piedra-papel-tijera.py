import random

opciones = ['Piedra', 'Papel', 'Tijeras']

print("Bienvenido al juego de Piedra, Papel o Tijeras")
eleccion_usuario = int(input("Ingresa tu elección (1: Piedra, 2: Papel, 3: Tijeras): ")) - 1
eleccion_computadora = random.randint(0, 2)

print("Tu elección:", opciones[eleccion_usuario])
print("La elección de la computadora:", opciones[eleccion_computadora])

if eleccion_usuario == eleccion_computadora:
    print("Empate!")
elif (eleccion_usuario - eleccion_computadora) % 3 == 1:
    print("¡Ganaste!")
else:
    print("¡Perdiste!")