import random


def run():
    my_number = random.randint(1, 101)
    guess = None
    print('Adivina el número que estoy pensando.')

    while guess != 0:
        your_number = int(input('Escribe un número: '))
        guess = my_number - your_number

        if guess > 0:
            print('Hmm... No, el número es más alto')
        elif guess < 0:
            print('Hmm... No, el número es más pequeño')
    
    print(f'Ganaste! Pensé en el {my_number}')


if __name__ == "__main__":
    run()