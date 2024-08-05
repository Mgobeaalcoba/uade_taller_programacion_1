from sys import argv


def main():
    if len(argv) != 2:
        print("Uso: python cuadrado.py <número>")
        return

    try:
        print(len(argv)) # 2
        print(argv) # ['argumentos.py', '-20']
        print(argv[0]) # argumentos.py
        print(argv[1]) # -20
        numero = int(argv[1])
        if numero > 0:
            print(f"El cuadrado de {numero} es {numero ** 2}.")
        else:
            print("El argumento debe ser un número entero positivo.")
    except ValueError:
        print(f"El argumento '{sys.argv[1]}' no es un número entero válido.")


if __name__ == "__main__":
    main()
