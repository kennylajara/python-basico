# CONVERSOR DE MONEDAS

menu = """
Bienvenido al conversor de monedas

1 - Pesos argentinos
2 - Pesos colombianos
3 - Pesos dominicanos
4 - Pesos mexicanos

Elige tu moneda base:
"""

option = int(input(menu))


if option == 1:
    currency = "argentinos"
    rate = 65
    amount = int(input(f"Indique la cantidad de {currency} a convertir: "))
    result = int( amount * rate )
    print ( f'{amount} pesos {currency} equivalen a {result} a dólares' )
elif option == 2:
    currency = "colombianos"
    rate = 3875
    amount = int(input(f"Indique la cantidad de {currency} a convertir: "))
    result = int( amount * rate )
    print ( f'{amount} pesos {currency} equivalen a {result} a dólares' )
elif option == 3:
    currency = "dominicanos"
    rate = 59
    amount = int(input(f"Indique la cantidad de {currency} a convertir: "))
    result = int( amount * rate )
    print ( f'{amount} pesos {currency} equivalen a {result} a dólares' )
elif option == 4:
    currency = "mexicanos"
    rate = 24
    amount = int(input(f"Indique la cantidad de {currency} a convertir: "))
    result = int( amount * rate )
    print ( f'{amount} pesos {currency} equivalen a {result} a dólares' )
else:
    print ('Esta no es una opción válida')