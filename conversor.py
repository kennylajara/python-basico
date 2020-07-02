# Funcion para convertir monedas
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

# Realizar conversion de moneda
if option == 1:
    convert ( "argentinos", 65 )
elif option == 2:
    convert ( "colombianos", 3875 )
elif option == 3:
    convert ( "dominicanos", 59 )
elif option == 4:
    convert ( "mexicanos", 24 )
else:
    print ('Esta no es una opción válida.')