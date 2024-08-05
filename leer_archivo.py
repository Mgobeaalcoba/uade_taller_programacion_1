def main():
  # Abrir el archivo en modo lectura
  try:
    with open("texto.txt", "r") as archivo:
      # Leer el contenido del archivo
      contenido = archivo.read()
      # Imprimir el contenido
      print(contenido)
  except Exception as e:
    print(f"Ocurrió un error: {e}")


if __name__ == '__main__':
  main()
