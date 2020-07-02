# Dar bienvenida al usuario
print( "Este programa sirve para sumar 2 cantidades." )
print( '-' * 10 )

# Solicitar al usuario que escriba los numeros a sumar
numero1 = input("Escribe un número: ")
numero2 = input("Escribr otro número: ")

# Hay que convertir el numero a entero
resultado = int(numero1) + int(numero2)

# Mostrar resultado
print ( f'El resultado es: {resultado}' )