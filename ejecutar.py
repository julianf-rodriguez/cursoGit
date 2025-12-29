def ejecutar():
    try:
        with open("resultado.txt", "w", encoding="utf-8") as archivo:
            archivo.write("se ejecuto correctamente GitHub Actions")
        print("Archivo creado con éxito.")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")

if __name__ == "__main__":
    ejecutar()