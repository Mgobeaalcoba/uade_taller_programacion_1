# Ejercicio 1: Contar Vocales
entrada = "Elefante"
cantidad_a = entrada.lower().count("a")
cantidad_e = entrada.lower().count("e")
cantidad_i = entrada.lower().count("i")
cantidad_o = entrada.lower().count("o")
cantidad_u = entrada.lower().count("u")
cantidad_vocales = cantidad_a + cantidad_e + cantidad_i + cantidad_o + cantidad_u
print("Número de vocales:", cantidad_vocales)

# Ejercicio 2: Palíndromo
entrada = "radar"
es_palindromo = entrada == entrada[::-1]
print("Es palíndromo:", es_palindromo)

# Ejercicio 3: Contar Palabras
entrada = "Hola, ¿cómo estás?"
num_palabras = len(entrada.split())
print("Número de palabras:", num_palabras)

# Ejercicio 4: Reemplazo de Palabras
frase = "El cielo es azul y el mar es azul"
buscar = "azul"
reemplazar = "verde"
nueva_frase = frase.replace(buscar, reemplazar)
print("Frase con reemplazo:", nueva_frase)

# Ejercicio 5: Formato de Texto
nombre = "Juan"
apellido = "Pérez"
nombre_completo = f"{nombre} {apellido}"
print("Nombre completo en mayúsculas:", nombre_completo.upper())
print("Nombre completo en minúsculas:", nombre_completo.lower())

# Ejercicio 6: Calcular Área de un Círculo
radio = 5
area_circulo = 3.14159 * radio**2
print("Área del círculo:", round(area_circulo, 2))

# Ejercicio 7: Conversión de Moneda
dolares = 100
euros = dolares * 0.85
print("Euros:", euros)

# Ejercicio 8: Número Par o Impar
numero = 42
es_par = numero % 2 == 0
print("Número:", es_par)

# Ejercicio 9: Cálculo de Interés Simple
capital = 1000
tasa = 0.05
tiempo = 3
interes = capital * tasa * tiempo
print("Interés simple:", interes)

# Ejercicio 10: Índice de Masa Corporal (IMC)
peso = 70
altura = 1.75
imc = peso / altura**2
print("IMC:", round(imc, 2))
