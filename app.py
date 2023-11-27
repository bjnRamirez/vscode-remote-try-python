#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("hello world")

import random

def obtener_opcion_oponente():
    opciones = ['rock', 'paper', 'scissors']
    return random.choice(opciones)

# Determinar el ganador
def determinar_ganador(opcion_jugador, opcion_oponente):
    if opcion_jugador == opcion_oponente:
        return 'tie'
    elif (
        (opcion_jugador == 'rock' and opcion_oponente == 'scissors') or
        (opcion_jugador == 'scissors' and opcion_oponente == 'paper') or
        (opcion_jugador == 'paper' and opcion_oponente == 'rock')
    ):
        return 'win'
    else:
        return 'lose'

# Jugar una ronda
def jugar_ronda():
    opcion_jugador = input("Elige rock, paper o scissors: ").lower()

    # Validar la entrada del usuario
    if opcion_jugador not in ['rock', 'paper', 'scissors']:
        print("Opción no válida. Por favor, elige rock, paper o scissors.")
        return

    opcion_oponente = obtener_opcion_oponente()
    resultado = determinar_ganador(opcion_jugador, opcion_oponente)

    # Mostrar resultado al jugador
    print(f"Tú elegiste {opcion_jugador}. El oponente eligió {opcion_oponente}.")

    if resultado == 'win':
        print("¡Ganaste!")
    elif resultado == 'lose':
        print("Perdiste.")
    else:
        print("Es un empate.")

# Lógica principal del juego y bucle de repetición
def main():
    # Inicializar puntuación
    victorias = 0
    rondas = 0

    while True:
        jugar_ronda()
        respuesta = input("¿Quieres jugar de nuevo? (yes/no): ").lower()

        if respuesta != 'yes':
            break

        # Incrementar la puntuación
        rondas += 1
        if resultado == 'win':
            victorias += 1

    # Mostrar la puntuación al final del juego
    print(f"Juego terminado. Ganaste {victorias} de {rondas} rondas.")

# Ejecución del juego
if __name__ == "__main__":
    main()