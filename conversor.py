def convert ( currency, rate ):
    amount = int(input(f"Indique la cantidad de pesos {currency} a convertir: "))
    result = round( amount / rate, 2 )
    print ( f'{amount} pesos {currency} equivalen a {result} a dólares' )

# CONVERSOR DE MONEDAS

menu = """
Bienvenido al conversor de monedas

1 - Pesos argentinos
2 - Pesos colombianos
3 - Pesos dominicanos
4 - Pesos mexicanos

Elige tu moneda base: """

option = int(input(menu))


if option == 1:
    currency = "argentinos"
    rate = 65
    convert ( currency, rate )
elif option == 2:
    currency = "colombianos"
    rate = 3875
    convert ( currency, rate )
elif option == 3:
    currency = "dominicanos"
    rate = 59
    convert ( currency, rate )
elif option == 4:
    currency = "mexicanos"
    rate = 24
    convert ( currency, rate )
else:
    print ('Esta no es una opción válida')