import random


def guess_number (mine, yours):
    return mine - yours


def run():
    my_number = random.randint(1, 101)
    guess = None
    print('Adivina el número que estoy pensando.')

    while guess != 0:
        
        your_number = int(input('Escribe un número: '))
        guess = guess_number( my_number, your_number )

        if guess > 0:
            print('Hmm... No, el número es más alto')
        elif guess < 0:
            print('Hmm... No, el número es más pequeño')
        else:
            print(f'Ganaste! Pensé en el {my_number}')
            break


if __name__ == "__main__":
    run()