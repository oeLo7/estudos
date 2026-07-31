nome = input("Identifique-se: ")

print(f"Maiúsculas: {nome.upper()}")
print(f"Minúsculas: {nome.lower()}")
print(f"Quantidade de letras(desconsiderando espaços): {len(nome.replace(" ", ""))}")
print(f"Primeiro nome tem {len(nome.split()[0])} letras")

