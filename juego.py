import random
def player_guess():
    while True:
        try:
            guess = int(input("Ingresa tu intento: "))
            return guess
        except ValueError:
            print("Ingresar un número válido")
    

def evaluate_attempt(guess, number):
    if guess < number:
        print("Muy bajo")
    elif guess > number:
        print("Muy alto")
    elif guess == number:
        print("¡Correcto!")
    else:
        print("Error")


def start_game():
    number = random.randint(1, 20)
    guess = 0
    attempts = 0
    print("Adivina el número entre 1 y 20")
    while guess != number:
        guess = player_guess()
        attempts += 1
        evaluate_attempt(guess, number)
    print("Número de intentos:", attempts)

start_game()