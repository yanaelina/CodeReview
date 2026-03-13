import random

def player_guess():
    """Solicita un número al usuario y valida que sea un entero."""
    while True:
        try:
            guess = int(input("Ingresa tu intento: "))
            return guess
        except ValueError:
            print("Ingresar un número válido")
    

def evaluate_attempt(guess, number):
    """Verifica si el intento del jugador es menor, mayor o igual al número correcto.

    Args:
        guess: Número ingresado por el jugador.
        number: Número que debe adivinarse.
    """
    if guess < number:
        print("Muy bajo")
    elif guess > number:
        print("Muy alto")
    elif guess == number:
        print("¡Correcto!")
    else:
        print("Error")


def start_game():
    """Inicia la partida del juego de adivinar el número."""
    number = random.randint(1, 20)
    guess = 0
    attempts = 0
    print("Bienvenido al juego de adivinar el número.\nEstoy pensando en un número entre el 1 y 20.\nIntenta adivinarlo. Te diré si tu intento es muy alto o muy bajo")
    while guess != number:
        guess = player_guess()
        attempts += 1
        evaluate_attempt(guess, number)
    print("Número de intentos:", attempts)

def game_menu():
    """Muestra un menú que permite jugar nuevamente o salir."""
    while True:
        start_game()
        option = input("\n¿Quiéres jugar de nuevo? (si, no): ")
        if option == "si":
            continue
        elif option == "no":
            print("Gracias por jugar :)")
            break
        else:
            print("Opción inválida")

game_menu()