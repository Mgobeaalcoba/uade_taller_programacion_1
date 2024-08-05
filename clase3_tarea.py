# Ejercicio 5: Contar el Número de Caracteres
# Escribe un programa que tome una cadena de texto y cuente el número total de caracteres (incluyendo espacios).
cadena = "Contando caracteres"
# Calcula el número de caracteres usando la función len()
num_caracteres = len(cadena)
print("Número de caracteres:", num_caracteres)

# Ejercicio 6: Reverso de una Cadena
# Escribe un programa que invierta una cadena de texto.
cadena = "Python"
# Invierte la cadena usando slicing con paso negativo
reverso_cadena = cadena[::-1]
print("Cadena invertida:", reverso_cadena)

# Ejercicio 7: Extraer Subcadena
# Escribe un programa que extraiga una subcadena de una cadena de texto, dado un índice de inicio y un índice de fin.
cadena = "Extraer subcadena"
inicio = 8
fin = 18
# Extrae la subcadena usando slicing
subcadena = cadena[inicio:fin]
print("Subcadena extraída:", subcadena)

# Ejercicio 8: Convertir Números a String y Viceversa
# Convierte un número a una cadena de texto y una cadena de texto a un número.
numero = 123
# Convierte el número a cadena usando str()
cadena_numero = str(numero)
print("Número como cadena:", cadena_numero)

cadena = "456"
# Convierte la cadena a número usando int()
numero_cadena = int(cadena)
print("Cadena como número:", numero_cadena)

# Ejercicio 9: Operaciones Aritméticas Básicas
# Realiza operaciones aritméticas básicas (suma, resta, multiplicación, división) con dos números.
a = 10
b = 5
# Realiza las operaciones aritméticas básicas
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
