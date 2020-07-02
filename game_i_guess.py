import random


def run():
    my_guess = None
    minimum = 1
    maximum = 100
    print('Piensa un número del 1 al 100')
    input('Presiona ENTER para continuar ')

    while True:
        
        my_guess = random.randint(minimum, maximum - 1)

        print('')
        print(f'¿Tu número es mayor a {my_guess}?')
        answer = input(f'(s/n): ').lower()
        
        while answer != 's' and answer != 'n':
            answer = input('Responde "s" para "sí" o "n" para "no": ')

        if answer == 's':
            minimum = my_guess + 1
        else:
            maximum = my_guess

        if minimum == maximum:
            print('')
            print(f'¡Ajá! Tu número es el {minimum}')
            break


if __name__ == "__main__":
    run()