while True:
    cidade = input("Digite o nome de uma cidade: ")

    corte = cidade.lower().split()

    print()

    if "santo" in corte[0]:
        print(f"{cidade} começa com Santo")
    else:
        print(f"{cidade} não começa com Santo")

    print()
