# CONVERSOR DE MONEDAS
moneda_local = int( input( "¿Cuánto dinero tienes en tu moneda local? " ))
tasa_del_dia = int( input ( "¿Cuál es la tasa del día? " ))

resultado = round( moneda_local / tasa_del_dia, 2)

print ( f'Equivale a {resultado} en la moneda a que deseas convertir')