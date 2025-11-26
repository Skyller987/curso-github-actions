def main():
    nombre = os.getenv("USERNAME")
    language = os.getenv("LANGUAGE")
    
    print(f"¡Hola, {nombre} tu lenguaje de programación favorito es {language}!")

if __name__ == "__main__":
    main()
