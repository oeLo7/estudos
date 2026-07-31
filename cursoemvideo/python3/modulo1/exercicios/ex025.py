while True:
    nome = input("Digite o nome de uma pessoa: ")

    print()

    if "silva" in nome.lower().split():
        print(f"{nome} tem Silva")

    else:
        print(f"{nome} não tem Silva")

    print()
