while True:
    nome = input("Digite um nome completo: ")

    print()

    print(f"O nome completo é: {nome}")

    print(f"O primeiro nome é: {nome.split()[0]}")

    print(f"O ultimo nome é: {nome.split()[len(nome.split()) - 1]}")

    print()
    