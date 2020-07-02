def is_prime(number):

    if number < 2:
        return False
    elif number == 2:
        return True

    # Square root
    root = number**0.5

    # Exact root
    if root == int(root):
        return False
    else:
        maximum = int(root)

    # Try to detect it the hard way
    counter = 0
    for i in range(1, maximum):
        if i == 1:
            continue
        if number % i == 0:
            counter += 1

    if counter == 0:
        return True
    else:
        return False

    return False


def run():
    number = int(input('Escribe un numero: '))
    if is_prime(number):
        print('Es primo.')
    else:
        print('No es primo.')


if __name__ == '__main__':
    run()