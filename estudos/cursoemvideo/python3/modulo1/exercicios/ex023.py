while True:
    n1 = float(input("Um número: "))

    if int(n1) < 0:
        print()
        print("Um número maior, por favor")
        print()
        continue

    if int(n1) > 9999:
        print()
        print("Um número menor, por favor")
        print()
        continue

    if float(n1) - int(n1) != 0:
        print()
        print("Um número quebrado não")
        print()
        continue

    n1 = str(int(n1))

    if len(n1) == 1:
        print(f"Unidade: {n1[0]}")
    elif len(n1) == 2:
        print(f"Unidade: {n1[1]}")
        print(f"Dezena: {n1[0]}")
    elif len(n1) == 3:
        print(f"Unidade: {n1[2]}")
        print(f"Dezena: {n1[1]}")
        print(f"Centena: {n1[0]}")
    elif len(n1) == 4:
        print(f"Unidade: {n1[3]}")
        print(f"Dezena: {n1[2]}")
        print(f"Centena: {n1[1]}")
        print(f"Milhar: {n1[0]}")


