while True:
    frase = input("Digite uma frase: ")

    print()

    print(f"A letra 'A' aparece {frase.lower().count("a")} vezes")

    print(f"Sua primeira aparição é na posição {frase.lower().find("a")}")

    print(f"Sua ultima aparição é na posição {frase.lower().rfind("a")}")

    print()
